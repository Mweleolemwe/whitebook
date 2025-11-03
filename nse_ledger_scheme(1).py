#!/usr/bin/env python3
import numpy as np
from numpy.fft import fft2, ifft2
import matplotlib.pyplot as plt
import csv

def arakawa_J(psi, omega, dx, dy):
    psi_xp = np.roll(psi, -1, axis=1); psi_xm = np.roll(psi, 1, axis=1)
    psi_yp = np.roll(psi, -1, axis=0); psi_ym = np.roll(psi, 1, axis=0)
    om_xp  = np.roll(omega, -1, axis=1); om_xm  = np.roll(omega, 1, axis=1)
    om_yp  = np.roll(omega, -1, axis=0); om_ym  = np.roll(omega, 1, axis=0)

    psi_xpyp = np.roll(psi_xp, -1, axis=0)
    psi_xmyp = np.roll(psi_xm, -1, axis=0)
    psi_xpym = np.roll(psi_xp,  1, axis=0)
    psi_xmym = np.roll(psi_xm,  1, axis=0)

    om_xpyp = np.roll(om_xp, -1, axis=0)
    om_xmyp = np.roll(om_xm, -1, axis=0)
    om_xpym = np.roll(om_xp,  1, axis=0)
    om_xmym = np.roll(om_xm,  1, axis=0)

    dx2 = 2.0*dx; dy2 = 2.0*dy

    J1 = ( (psi_xp-psi_xm)*(om_yp-om_ym) - (psi_yp-psi_ym)*(om_xp-om_xm) )/(dx2*dy2)

    J2 = ( psi_xp*(om_xp-om_xpym) - psi_xm*(om_xmyp-om_xm) -
           psi_yp*(om_yp-om_xpyp) + psi_ym*(om_xmym-om_ym) )/(dx2*dy2)

    J3 = ( psi_xpyp*(om_yp-om_xp) - psi_xmym*(om_xm-om_ym) -
           psi_xmyp*(om_xpyp-om_xm) + psi_xpym*(om_xp-om_xmym) )/(dx2*dy2)

    return (J1 + J2 + J3)/3.0

def laplacian(f, dx, dy):
    return (np.roll(f,-1,1)+np.roll(f,1,1)+np.roll(f,-1,0)+np.roll(f,1,0)-4*f)/(dx*dx)

def poisson_solve_periodic_rhs_minus_omega(omega, Lx, Ly):
    ny, nx = omega.shape
    kx = 2*np.pi*np.fft.fftfreq(nx, d=Lx/nx)
    ky = 2*np.pi*np.fft.fftfreq(ny, d=Ly/ny)
    kx2 = kx**2
    ky2 = ky**2
    K2 = ky2[:,None] + kx2[None,:]
    omhat = fft2(omega)
    psik = np.zeros_like(omhat, dtype=complex)
    mask = (K2!=0)
    psik[mask] = omhat[mask]/K2[mask]
    psik[0,0] = 0.0
    psi = np.real(ifft2(psik))
    return psi

def Dx(f, dx): return (np.roll(f,-1,1)-np.roll(f,1,1))/(2*dx)
def Dy(f, dy): return (np.roll(f,-1,0)-np.roll(f,1,0))/(2*dy)

def energy(psi, dx, dy):
    ux = Dy(psi, dy)
    vy = -Dx(psi, dx)
    return 0.5*np.sum(ux*ux + vy*vy)*dx*dy

def enstrophy(omega, dx, dy):
    return np.sum(omega*omega)*dx*dy

def step(omega, nu, dt, Lx, Ly):
    ny, nx = omega.shape
    dx = Lx/nx; dy = Ly/ny
    psi = poisson_solve_periodic_rhs_minus_omega(omega, Lx, Ly)
    J = arakawa_J(psi, omega, dx, dy)
    rhs = -J + nu*laplacian(omega, dx, dy)
    omega1 = omega + dt*rhs
    psi1 = poisson_solve_periodic_rhs_minus_omega(omega1, Lx, Ly)
    J1 = arakawa_J(psi1, omega1, dx, dy)
    rhs1 = -J1 + nu*laplacian(omega1, dx, dy)
    omega_new = omega + 0.5*dt*(rhs + rhs1)
    return omega_new

def run_demo(N=64, nu=1e-2, steps=200, L=2*np.pi, dt=None):
    nx = ny = N
    Lx = Ly = L
    dx = Lx/nx; dy = Ly/ny
    x = np.linspace(0, Lx, nx, endpoint=False)
    y = np.linspace(0, Ly, ny, endpoint=False)
    X, Y = np.meshgrid(x, y)

    omega = 2.0*np.sin(X)*np.sin(Y)  # Taylor–Green vorticity
    psi = poisson_solve_periodic_rhs_minus_omega(omega, Lx, Ly)
    E0 = energy(psi, dx, dy)

    times = [0.0]; energies = [E0]; diss_rate = [nu*enstrophy(omega, dx, dy)]; cum_diss = [0.0]

    # time step: either given or diffusion-limited
    if dt is None:
        dt_diff = 0.25*min(dx*dx, dy*dy)/max(nu, 1e-12)
        dt = min(0.01, dt_diff)

    for n in range(1, steps+1):
        omega_new = step(omega, nu, dt, Lx, Ly)
        psi_new = poisson_solve_periodic_rhs_minus_omega(omega_new, Lx, Ly)
        E = energy(psi_new, dx, dy)
        D = nu*enstrophy(omega_new, dx, dy)

        cum = cum_diss[-1] + 0.5*(diss_rate[-1] + D)*dt
        t = times[-1] + dt

        omega = omega_new; psi = psi_new
        times.append(t); energies.append(E); diss_rate.append(D); cum_diss.append(cum)

    residual = np.array(energies) + np.array(cum_diss) - energies[0]

    with open('/mnt/data/ledger_timeseries.csv','w', newline='') as f:
        w = csv.writer(f); w.writerow(['t','E','cum_diss','ledger_residual'])
        for t,E,c,r in zip(times, energies, cum_diss, residual):
            w.writerow([t,E,c,r])

    return dt, energies[-1], cum_diss[-1], residual[-1]
