import numpy as np
from scipy.signal import welch
from scipy.io import wavfile
import pandas as pd
import os

def calculate_var_s(f_hz: np.ndarray, P_f: np.ndarray) -> float:
    """
    Calculates the Log-Variance (Var_s[ln P]) from a power spectrum P(f).
    This transforms the spectrum from Hertz-gauge (f) to Scale-gauge (s=ln f).

    :param f_hz: Frequency vector (Hz).
    :param P_f: Power Spectral Density vector (P(f)).
    :return: Variance in the log-amplitude/log-frequency domain (s-gauge).
    """
    # Gauge Transformation: f -> s = ln(f)
    valid = (f_hz > 0) & np.isfinite(P_f)
    if not np.any(valid):
        return 0.0
    f_hz = f_hz[valid]
    P_f = P_f[valid]
    s_gauge = np.log(f_hz)
    A_s = np.log(P_f)
    valid_indices = np.isfinite(A_s) & np.isfinite(s_gauge)
    if not np.any(valid_indices):
        return 0.0
    A_s = A_s[valid_indices]
    return float(np.var(A_s))

def clean_rr_intervals(rr_ms: np.ndarray, min_ms=300, max_ms=2000) -> np.ndarray:
    rr_clean = rr_ms[(rr_ms >= min_ms) & (rr_ms <= max_ms)]
    return rr_clean

def process_hrv_data(rr_ms: np.ndarray) -> dict:
    """
    Calculates time-domain (RMSSD, RMSLR) and spectral (LF/HF, Var_s) metrics.

    :param rr_ms: Array of RR intervals in milliseconds.
    :return: Dictionary of computed HRV metrics.
    """
    rr_ms = clean_rr_intervals(rr_ms)
    if len(rr_ms) < 2:
        return {'rmssd_ms': 0.0, 'rmslr': 0.0, 'lfv': 0.0, 'lf_peak_hz': 0.0, 'varlog_rr': 0.0}
    
    # RMSSD
    rmssd = np.sqrt(np.mean(np.diff(rr_ms)**2))
    
    # RMSLR
    rr_s = rr_ms / 1000.0
    delta_s = np.diff(np.log(rr_s))
    rmslr = np.sqrt(np.mean(delta_s**2))
    
    # Spectral (Welch PSD)
    f, Pxx = welch(rr_s, fs=1.0, nperseg=min(256, len(rr_s)))
    valid = (f > 0) & np.isfinite(Pxx)
    f, Pxx = f[valid], Pxx[valid]
    
    # LF Power and Peak
    lf_band = (f >= 0.04) & (f < 0.15)
    lfv = np.sum(Pxx[lf_band]) if np.any(lf_band) else 0.0
    lf_peak = f[lf_band][np.argmax(Pxx[lf_band])] if np.any(lf_band) else 0.0
    
    # Var_s
    varlog_rr = calculate_var_s(f, Pxx)
    
    return {
        'rmssd_ms': float(rmssd),
        'rmslr': float(rmslr),
        'lfv': float(lfv),
        'lf_peak_hz': float(lf_peak),
        'varlog_rr': varlog_rr
    }

def audio_log_psd(wav_path: str) -> float:
    if not os.path.exists(wav_path):
        return 0.0
    sr, data = wavfile.read(wav_path)
    if data.ndim > 1:
        data = data.mean(axis=1).astype(float)
    data = data / np.max(np.abs(data))
    f, Pxx = welch(data, fs=sr, nperseg=1024)
    return calculate_var_s(f, Pxx)

def resp_rate_variance(csv_path: str) -> float:
    if not os.path.exists(csv_path):
        return 0.0
    df = pd.read_csv(csv_path)
    if 'bpm' in df.columns:
        bpm = df['bpm'].values
        return float(np.var(bpm))
    return 0.0

def parse_block_files(input_dir: str = 'input', output_dir: str = 'data') -> str:
    """
    Minimal parser: Ingest field files, compute metrics, output metrics.lua.
    
    Expected files in input_dir:
    - rr_intervals_pre.csv / rr_intervals_post.csv (column: RR_ms)
    - voice_pre.wav / voice_post.wav
    - ir_pre.wav / ir_post.wav
    - resp_rates_pre.csv / resp_rates_post.csv (column: bpm)
    
    :param input_dir: Directory with input files.
    :param output_dir: Directory for metrics.lua.
    :return: Lua string (also written to file).
    """
    os.makedirs(output_dir, exist_ok=True)
    
    metrics = {}
    
    # HRV Pre
    pre_csv = os.path.join(input_dir, 'rr_intervals_pre.csv')
    if os.path.exists(pre_csv):
        rr_pre = pd.read_csv(pre_csv)['RR_ms'].values
        hrv_pre = process_hrv_data(rr_pre)
        metrics['rmssd_pre_ms'] = hrv_pre['rmssd_ms']
        metrics['lfv_base'] = hrv_pre['lfv']
        metrics['varlog_rr_pre'] = hrv_pre['varlog_rr']
    
    # HRV Post
    post_csv = os.path.join(input_dir, 'rr_intervals_post.csv')
    if os.path.exists(post_csv):
        rr_post = pd.read_csv(post_csv)['RR_ms'].values
        hrv_post = process_hrv_data(rr_post)
        metrics['rmssd_post_ms'] = hrv_post['rmssd_ms']
        metrics['lfv_post'] = hrv_post['lfv']
        metrics['lf_peak_hz_post'] = hrv_post['lf_peak_hz']
        metrics['varlog_rr_post'] = hrv_post['varlog_rr']
    
    # Voice
    metrics['varlog_voice_pre'] = audio_log_psd(os.path.join(input_dir, 'voice_pre.wav'))
    metrics['varlog_voice_post'] = audio_log_psd(os.path.join(input_dir, 'voice_post.wav'))
    
    # IR
    metrics['varlog_ir_pre'] = audio_log_psd(os.path.join(input_dir, 'ir_pre.wav'))
    metrics['varlog_ir_post'] = audio_log_psd(os.path.join(input_dir, 'ir_post.wav'))
    
    # Resp
    metrics['resp_var_base'] = resp_rate_variance(os.path.join(input_dir, 'resp_rates_pre.csv'))
    metrics['resp_var_post'] = resp_rate_variance(os.path.join(input_dir, 'resp_rates_post.csv'))
    
    # Write Lua
    lua_string = "return {\n"
    for k, v in sorted(metrics.items()):
        lua_string += f"  {k} = {v:.3f},\n"
    lua_string += "}\n"
    
    lua_path = os.path.join(output_dir, 'metrics.lua')
    with open(lua_path, 'w') as f:
        f.write(lua_string)
    
    return lua_string

# Minimal Test Run (with empty inputs; outputs defaults 0.0)
lua_output = parse_block_files()
print(lua_output)
