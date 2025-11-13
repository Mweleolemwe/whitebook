#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pedagogy_pipeline.py — MWƐN / Onu Ledger cross-facet analysis toolkit

A single-file, replication-ready pipeline that computes the pedagogy’s core metrics:
- Voice: Var_s[ln P] on a log-frequency grid (pre/post)
- HRV: RMSSD, RMSLR (ledger-consistent), LF power + peak, Var_s[ln S_RR]
- Respiration (optional): instantaneous-rate variance via Hilbert phase
- Room acoustics (optional): Var_s[ln P_IR] (pre/post) and RT60 via Schroeder
- Cross-facet deltas and metrics.lua export for the LuaLaTeX “self-check” in your paper

Usage (examples)
---------------
# Voice + HRV + export metrics.lua
python pedagogy_pipeline.py \
  --voice-pre fig/voice_pre.wav --voice-post fig/voice_post.wav \
  --ibi-pre data/rr_base.csv --ibi-post data/rr_post.csv \
  --outdir results/

# Include respiration + IR (clap test wavs)
python pedagogy_pipeline.py \
  --voice-pre fig/voice_pre.wav --voice-post fig/voice_post.wav \
  --ibi-pre data/rr_base.csv --ibi-post data/rr_post.csv \
  --resp-pre fig/resp_base.wav --resp-post fig/resp_post.wav \
  --ir-pre fig/ir_pre.wav --ir-post fig/ir_post.wav \
  --outdir results/

Input formats
-------------
- Voice/IR/Resp files: WAV (mono or stereo). Other formats not guaranteed.
- RR CSVs: single column named one of ["RR_ms","rr_ms","RR","rr"] in milliseconds.

Outputs
-------
- results/metrics.json         # all computed scalars
- results/metrics.lua          # keys expected by the LaTeX self-check
- results/*.png                # spectra and quicklook figures
- stdout                       # brief summary table

Requires
--------
numpy, scipy, pandas, matplotlib

(c) Yay — Super Lumina OC Pedagogy. MIT-like spirit; use responsibly.
"""

from __future__ import annotations
import argparse
import json
import math
import os
from dataclasses import dataclass
from typing import Dict, Optional, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import welch, butter, filtfilt, hilbert, coherence
from scipy.interpolate import interp1d
from scipy.io import wavfile


# ---------------------------
# Utilities
# ---------------------------

def ensure_outdir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def read_wav_mono(path: str) -> Tuple[int, np.ndarray]:
    fs, x = wavfile.read(path)
    x = x.astype(np.float64)
    # Normalize integer PCM to [-1,1] if needed
    if x.dtype.kind in ("i", "u"):
        maxv = np.iinfo(x.dtype).max
        x = x / maxv
    if x.ndim == 2:
        x = x.mean(axis=1)
    return fs, x


def stabilized_log(x: np.ndarray, eps_frac: float = 0.01) -> np.ndarray:
    """slog_epsilon(x) = ln(x + epsilon), epsilon = eps_frac * median(nonzero x)"""
    x = np.asarray(x, dtype=np.float64)
    pos = x[x > 0]
    if pos.size == 0:
        eps = 1e-12
    else:
        eps = eps_frac * np.median(pos)
        eps = max(eps, 1e-12)
    return np.log(x + eps)


def uniform_log_grid(fmin: float, fmax: float, nbins: int = 256) -> np.ndarray:
    return np.exp(np.linspace(np.log(fmin), np.log(fmax), nbins))


def psd_log_variance(
    x: np.ndarray,
    fs: float,
    fmin: float,
    fmax: float,
    nperseg: int = 2048,
    noverlap: int = 1024,
    eps_frac: float = 0.01,
    nbins: int = 256,
) -> Tuple[float, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Welch PSD -> interpolate onto uniform s=ln f grid -> Var_s[ln P]
    Returns:
      var_logpower, f (Welch), Pxx, s_grid, a_grid (ln power on log-f grid)
    """
    f, Pxx = welch(
        x,
        fs=fs,
        nperseg=nperseg,
        noverlap=noverlap,
        window="hann",
        detrend="constant",
        scaling="density",
    )
    # keep band
    mask = (f >= fmin) & (f <= fmax)
    f_band = f[mask]
    P_band = Pxx[mask]
    if f_band.size < 8:
        return float("nan"), f, Pxx, np.array([]), np.array([])
    # interpolate ln P onto uniform log-f grid
    s_grid = np.log(uniform_log_grid(fmin, fmax, nbins))
    # interp requires strictly increasing f; stabilize zeros before log
    a = stabilized_log(P_band, eps_frac=eps_frac)
    interp = interp1d(np.log(f_band), a, kind="linear", fill_value="extrapolate", bounds_error=False)
    a_grid = interp(s_grid)
    var_logpower = float(np.var(a_grid, ddof=1))
    return var_logpower, f_band, P_band, s_grid, a_grid


def rmssd(rr_ms: np.ndarray) -> float:
    rr = np.asarray(rr_ms, dtype=np.float64)
    d = np.diff(rr)
    return float(np.sqrt(np.mean(d * d))) if d.size else float("nan")


def rmslr(rr_ms: np.ndarray) -> float:
    rr = np.asarray(rr_ms, dtype=np.float64)
    if rr.size < 2:
        return float("nan")
    ds = np.diff(np.log(rr))
    return float(np.sqrt(np.mean(ds * ds)))


def ibi_tachogram(rr_ms: np.ndarray, fs_out: float = 4.0) -> Tuple[np.ndarray, np.ndarray]:
    """Construct a uniformly sampled IBI (heart period) time series from RR intervals."""
    rr_s = np.asarray(rr_ms, dtype=np.float64) / 1000.0
    if rr_s.size < 3:
        return np.array([]), np.array([])
    t_beats = np.concatenate([[0.0], np.cumsum(rr_s)[:-1]])
    ibi = rr_s  # instantaneous period (s)
    t_uniform = np.arange(0.0, t_beats[-1] + 1.0 / fs_out, 1.0 / fs_out)
    f = interp1d(t_beats, ibi, kind="cubic", fill_value="extrapolate", bounds_error=False)
    ibi_uniform = f(t_uniform)
    return t_uniform, ibi_uniform


def hrv_psd(
    rr_ms: np.ndarray,
    fs_tach: float = 4.0,
    fmin: float = 0.003,
    fmax: float = 0.5,
    nperseg: int = 512,
    noverlap: int = 256,
) -> Tuple[np.ndarray, np.ndarray]:
    t, ibi = ibi_tachogram(rr_ms, fs_out=fs_tach)
    if ibi.size < 8:
        return np.array([]), np.array([])
    f, P = welch(
        ibi,
        fs=fs_tach,
        nperseg=nperseg,
        noverlap=noverlap,
        window="hann",
        detrend="constant",
        scaling="density",
    )
    mask = (f >= fmin) & (f <= fmax)
    return f[mask], P[mask]


def band_power(f: np.ndarray, P: np.ndarray, band: Tuple[float, float]) -> float:
    if f.size == 0:
        return float("nan")
    lo, hi = band
    m = (f >= lo) & (f <= hi)
    if not np.any(m):
        return float("nan")
    # trapezoidal integrate
    return float(np.trapz(P[m], f[m]))


def peak_frequency(f: np.ndarray, P: np.ndarray, band: Tuple[float, float]) -> float:
    if f.size == 0:
        return float("nan")
    lo, hi = band
    m = (f >= lo) & (f <= hi)
    if not np.any(m):
        return float("nan")
    idx = np.argmax(P[m])
    return float(f[m][idx])


def butter_bandpass(lo, hi, fs, order=4):
    return butter(order, [lo / (fs / 2), hi / (fs / 2)], btype="band")


def respiration_rate_variance_from_signal(resp: np.ndarray, fs: float) -> float:
    """Bandpass -> Hilbert -> instantaneous frequency -> variance."""
    if resp.size < int(fs * 5):
        return float("nan")
    b, a = butter_bandpass(0.05, 0.8, fs, order=4)
    y = filtfilt(b, a, resp)
    analytic = hilbert(y)
    phase = np.unwrap(np.angle(analytic))
    inst_freq = np.diff(phase) * fs / (2 * np.pi)  # Hz
    if inst_freq.size < 8:
        return float("nan")
    return float(np.var(inst_freq, ddof=1))


def rr_resp_coherence(rr_ms: np.ndarray, resp: np.ndarray, fs_resp: float, fs_tach: float = 4.0) -> Tuple[np.ndarray, np.ndarray]:
    t_rr, ibi = ibi_tachogram(rr_ms, fs_out=fs_tach)
    if ibi.size == 0:
        return np.array([]), np.array([])
    # resample resp to fs_tach
    t_resp = np.arange(resp.size) / fs_resp
    t_uniform = np.arange(0.0, min(t_resp[-1], t_rr[-1]), 1.0 / fs_tach)
    fr = interp1d(t_resp, resp, kind="linear", fill_value="extrapolate", bounds_error=False)
    rr = interp1d(t_rr, ibi, kind="linear", fill_value="extrapolate", bounds_error=False)
    resp_u = fr(t_uniform)
    ibi_u = rr(t_uniform)
    f, Cxy = coherence(ibi_u, resp_u, fs=fs_tach, nperseg=256, noverlap=128)
    return f, Cxy


def ir_rt60_schroeder(ir: np.ndarray, fs: float) -> float:
    """Estimate RT60 via Schroeder integration (approximate)."""
    if ir.size < 1024:
        return float("nan")
    e = ir.astype(np.float64)
    edc = np.cumsum(e[::-1] ** 2)[::-1]  # reverse integrate energy
    edc_db = 10.0 * np.log10(edc / np.max(edc) + 1e-15)
    # Fit linear region between -5 dB and -35 dB
    t = np.arange(edc_db.size) / fs
    m = (edc_db >= -35.0) & (edc_db <= -5.0)
    if m.sum() < 50:
        return float("nan")
    # linear fit y = a + b t
    coef = np.polyfit(t[m], edc_db[m], 1)
    slope = coef[0]  # dB/s (negative)
    if slope >= 0:
        return float("nan")
    return float(-60.0 / slope)  # seconds


# ---------------------------
# I/O helpers
# ---------------------------

def load_rr_csv(path: str) -> np.ndarray:
    df = pd.read_csv(path)
    for col in ["RR_ms", "rr_ms", "RR", "rr"]:
        if col in df.columns:
            rr = df[col].to_numpy(dtype=float)
            # clip to plausible range (300..2000 ms) and drop big jumps
            m = (rr >= 300.0) & (rr <= 2000.0)
            rr = rr[m]
            return rr
    raise ValueError(f"No RR column found in {path} (expected one of RR_ms, rr_ms, RR, rr)")


def save_metrics_lua(metrics: Dict[str, float], outpath: str) -> None:
    with open(outpath, "w", encoding="utf-8") as f:
        f.write("return {\n")
        for k, v in metrics.items():
            if isinstance(v, (int, float)) and math.isfinite(v):
                f.write(f"  {k} = {v:.6f},\n")
            else:
                f.write(f"  {k} = nil,\n")
        f.write("}\n")


def quick_plot(f, P, title, outpng, fmin=None, fmax=None, logx=True):
    plt.figure(figsize=(7.0, 4.0))
    if logx:
        plt.semilogx(f, 10 * np.log10(P + 1e-20))
    else:
        plt.plot(f, 10 * np.log10(P + 1e-20))
    if fmin and fmax:
        plt.xlim([fmin, fmax])
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power (dB)")
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(outpng, dpi=150)
    plt.close()


# ---------------------------
# Main analysis
# ---------------------------

@dataclass
class Args:
    voice_pre: Optional[str]
    voice_post: Optional[str]
    ibi_pre: Optional[str]
    ibi_post: Optional[str]
    resp_pre: Optional[str]
    resp_post: Optional[str]
    ir_pre: Optional[str]
    ir_post: Optional[str]
    outdir: str
    eps_frac: float
    nbins: int


def analyze(args: Args) -> Dict[str, float]:
    ensure_outdir(args.outdir)
    metrics: Dict[str, float] = {}

    # ----- VOICE -----
    if args.voice_pre and args.voice_post:
        fs0, vpre = read_wav_mono(args.voice_pre)
        fs1, vpost = read_wav_mono(args.voice_post)
        if fs0 != fs1:
            # resampling would be ideal; for simplicity we only warn
            print("[warn] voice fs mismatch; proceeding with individual fs for PSD.")
        # Compute PSD log-variance in 100..4000 Hz band
        vvar_pre, fvp, Pvp, svp, avp = psd_log_variance(
            vpre, fs0, fmin=100.0, fmax=4000.0, eps_frac=args.eps_frac, nbins=args.nbins
        )
        vvar_post, fvo, Pvo, svo, avo = psd_log_variance(
            vpost, fs1, fmin=100.0, fmax=4000.0, eps_frac=args.eps_frac, nbins=args.nbins
        )
        metrics["varlog_voice_pre"] = vvar_pre
        metrics["varlog_voice_post"] = vvar_post
        quick_plot(fvp, Pvp, "Voice PSD (pre)", os.path.join(args.outdir, "voice_psd_pre.png"), fmin=100, fmax=4000)
        quick_plot(fvo, Pvo, "Voice PSD (post)", os.path.join(args.outdir, "voice_psd_post.png"), fmin=100, fmax=4000)

    # ----- HRV -----
    if args.ibi_pre and args.ibi_post:
        rr_pre = load_rr_csv(args.ibi_pre)
        rr_post = load_rr_csv(args.ibi_post)

        metrics["rmssd_pre_ms"] = rmssd(rr_pre)
        metrics["rmssd_post_ms"] = rmssd(rr_post)
        metrics["rmslr_pre"] = rmslr(rr_pre)
        metrics["rmslr_post"] = rmslr(rr_post)

        f_pre, P_pre = hrv_psd(rr_pre)
        f_post, P_post = hrv_psd(rr_post)
        if f_pre.size:
            quick_plot(f_pre, P_pre, "HRV PSD (pre)", os.path.join(args.outdir, "hrv_psd_pre.png"), fmin=0.003, fmax=0.5, logx=False)
        if f_post.size:
            quick_plot(f_post, P_post, "HRV PSD (post)", os.path.join(args.outdir, "hrv_psd_post.png"), fmin=0.003, fmax=0.5, logx=False)

        # LF band metrics
        lf_band = (0.04, 0.15)
        if f_pre.size:
            metrics["lf_power_base"] = band_power(f_pre, P_pre, lf_band)
        if f_post.size:
            metrics["lf_power_post"] = band_power(f_post, P_post, lf_band)
            metrics["lf_peak_hz_post"] = peak_frequency(f_post, P_post, lf_band)

        # For LaTeX expectations: lfv_base/lfv_post map to LF powers
        metrics["lfv_base"] = metrics.get("lf_power_base", float("nan"))
        metrics["lfv_post"] = metrics.get("lf_power_post", float("nan"))

        # Log-variance of HRV PSD (Var_s[ln S_RR])
        if f_pre.size:
            vrr_pre = psd_var_on_log_grid_given(f_pre, P_pre, fmin=0.003, fmax=0.5, eps_frac=args.eps_frac, nbins=args.nbins)
            metrics["varlog_rr_pre"] = vrr_pre
        if f_post.size:
            vrr_post = psd_var_on_log_grid_given(f_post, P_post, fmin=0.003, fmax=0.5, eps_frac=args.eps_frac, nbins=args.nbins)
            metrics["varlog_rr_post"] = vrr_post

    # ----- Respiration (optional) -----
    if args.resp_pre and args.resp_post:
        fsr0, rpre = read_wav_mono(args.resp_pre)
        fsr1, rpost = read_wav_mono(args.resp_post)
        metrics["resp_var_base"] = respiration_rate_variance_from_signal(rpre, fsr0)
        metrics["resp_var_post"] = respiration_rate_variance_from_signal(rpost, fsr1)

        # Coherence RR-Resp (post as example)
        if args.ibi_post:
            rr_post = load_rr_csv(args.ibi_post)
            fC, Cxy = rr_resp_coherence(rr_post, rpost, fs_resp=fsr1, fs_tach=4.0)
            if fC.size:
                # coherence at resp peak (estimate via Hilbert-derived median)
                # We'll just report max coherence in 0.05..0.4 Hz window
                m = (fC >= 0.05) & (fC <= 0.4)
                if np.any(m):
                    metrics["c_rr_resp_at_fresp"] = float(np.max(Cxy[m]))
                plt.figure(figsize=(7,4))
                plt.plot(fC, Cxy)
                plt.xlim([0.0, 0.5]); plt.ylim([0,1])
                plt.xlabel("Frequency (Hz)"); plt.ylabel("Coherence")
                plt.title("RR–Resp Coherence (post)")
                plt.grid(True, alpha=0.3)
                plt.tight_layout()
                plt.savefig(os.path.join(args.outdir, "coherence_rr_resp_post.png"), dpi=150)
                plt.close()

    # ----- IR / Room acoustics (optional) -----
    if args.ir_pre and args.ir_post:
        fsip, ir_pre = read_wav_mono(args.ir_pre)
        fsio, ir_post = read_wav_mono(args.ir_post)
        # Treat IR wavs as impulse responses or clap recordings (approximate)
        # PSD variance on 100..4000 Hz band
        ivar_pre, fip, Pip, sip, aip = psd_log_variance(ir_pre, fsip, fmin=100.0, fmax=4000.0, eps_frac=args.eps_frac, nbins=args.nbins)
        ivar_post, fio, Pio, sio, aio = psd_log_variance(ir_post, fsio, fmin=100.0, fmax=4000.0, eps_frac=args.eps_frac, nbins=args.nbins)
        metrics["varlog_IR_pre"] = ivar_pre
        metrics["varlog_IR_post"] = ivar_post
        quick_plot(fip, Pip, "IR PSD (pre)", os.path.join(args.outdir, "ir_psd_pre.png"), fmin=100, fmax=4000)
        quick_plot(fio, Pio, "IR PSD (post)", os.path.join(args.outdir, "ir_psd_post.png"), fmin=100, fmax=4000)

        # RT60
        metrics["rt60_pre"] = ir_rt60_schroeder(ir_pre, fsip)
        metrics["rt60_post"] = ir_rt60_schroeder(ir_post, fsio)

    # ----- Export metrics -----
    with open(os.path.join(args.outdir, "metrics.json"), "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    # Lua export for LaTeX self-check
    ensure_outdir(os.path.join(args.outdir, "..", "data"))
    lua_out = os.path.join(args.outdir, "..", "data", "metrics.lua")
    save_metrics_lua(metrics, lua_out)

    # ----- Console summary -----
    pretty_summary(metrics)

    return metrics


def psd_var_on_log_grid_given(
    f: np.ndarray,
    P: np.ndarray,
    fmin: float,
    fmax: float,
    eps_frac: float = 0.01,
    nbins: int = 256,
) -> float:
    """Var_s[ln P] when PSD already computed; resample onto uniform log-f grid."""
    mask = (f >= fmin) & (f <= fmax)
    if not np.any(mask):
        return float("nan")
    f_band = f[mask]
    P_band = P[mask]
    s_grid = np.log(uniform_log_grid(fmin, fmax, nbins))
    a = stabilized_log(P_band, eps_frac=eps_frac)
    interp = interp1d(np.log(f_band), a, kind="linear", fill_value="extrapolate", bounds_error=False)
    a_grid = interp(s_grid)
    return float(np.var(a_grid, ddof=1))


def pretty_summary(metrics: Dict[str, float]) -> None:
    def g(k): 
        v = metrics.get(k, None)
        return f"{v:.3f}" if isinstance(v, (int,float)) and math.isfinite(v) else "NA"
    print("\n=== Pedagogy Metrics Summary ===")
    print(f"Voice Var_s[ln P] pre→post: {g('varlog_voice_pre')} → {g('varlog_voice_post')}  Δ={delta_str(metrics, 'varlog_voice_pre', 'varlog_voice_post')}")
    print(f"HRV RMSSD (ms)   pre→post: {g('rmssd_pre_ms')} → {g('rmssd_post_ms')}")
    print(f"HRV RMSLR        pre→post: {g('rmslr_pre')} → {g('rmslr_post')}")
    print(f"LF power         base→post: {g('lfv_base')} → {g('lfv_post')}  peak_post={g('lf_peak_hz_post')} Hz")
    print(f"HRV Var_s[ln S]  pre→post: {g('varlog_rr_pre')} → {g('varlog_rr_post')}")
    print(f"Resp var (Hz²)   base→post: {g('resp_var_base')} → {g('resp_var_post')}")
    print(f"IR Var_s[ln P]   pre→post: {g('varlog_IR_pre')} → {g('varlog_IR_post')}  RT60: {g('rt60_pre')} → {g('rt60_post')}")
    print("metrics.lua written under ../data/ (relative to outdir)\n")


def delta_str(metrics: Dict[str, float], k0: str, k1: str) -> str:
    v0 = metrics.get(k0, None); v1 = metrics.get(k1, None)
    if all(isinstance(v, (int,float)) and math.isfinite(v) for v in (v0, v1)):
        return f"{(v1 - v0):+.3f}"
    return "NA"


# ---------------------------
# CLI
# ---------------------------

def parse_args() -> Args:
    p = argparse.ArgumentParser(description="MWƐN / Onu Ledger cross-facet analysis pipeline")
    p.add_argument("--voice-pre", type=str, default=None, help="Voice WAV (pre)")
    p.add_argument("--voice-post", type=str, default=None, help="Voice WAV (post)")
    p.add_argument("--ibi-pre", type=str, default=None, help="RR (ms) CSV (pre)")
    p.add_argument("--ibi-post", type=str, default=None, help="RR (ms) CSV (post)")
    p.add_argument("--resp-pre", type=str, default=None, help="Respiration WAV (pre) (optional)")
    p.add_argument("--resp-post", type=str, default=None, help="Respiration WAV (post) (optional)")
    p.add_argument("--ir-pre", type=str, default=None, help="Impulse response WAV (pre) (optional)")
    p.add_argument("--ir-post", type=str, default=None, help="Impulse response WAV (post) (optional)")
    p.add_argument("--outdir", type=str, default="results", help="Output directory")
    p.add_argument("--eps-frac", type=float, default=0.01, help="epsilon fraction for stabilized log (1%% of median nonzero by default)")
    p.add_argument("--nbins", type=int, default=256, help="log-frequency bins for Var_s computation")
    a = p.parse_args()
    return Args(
        voice_pre=a.voice_pre,
        voice_post=a.voice_post,
        ibi_pre=a.ibi_pre,
        ibi_post=a.ibi_post,
        resp_pre=a.resp_pre,
        resp_post=a.resp_post,
        ir_pre=a.ir_pre,
        ir_post=a.ir_post,
        outdir=a.outdir,
        eps_frac=a.eps_frac,
        nbins=a.nbins,
    )


if __name__ == "__main__":
    args = parse_args()
    analyze(args)
