import numpy as np
import math

def f(x, ke, tmax):
    return math.log(x) - ke*(x - 1)*tmax

def solve_for_ka(ke=0.13, tmax=4.0, x_lower=1.01, x_upper=20.0, tol=1e-7):
    fl = f(x_lower, ke, tmax)
    fu = f(x_upper, ke, tmax)
    if fl*fu > 0:
        raise ValueError("Sin cambio de signo en intervalo.")
    while (x_upper - x_lower) > tol:
        x_mid = 0.5*(x_lower + x_upper)
        fm = f(x_mid, ke, tmax)
        if fm == 0:
            return x_mid * ke
        if fl*fm < 0:
            x_upper = x_mid
            fu = fm
        else:
            x_lower = x_mid
            fl = fm
    x_final = 0.5*(x_lower + x_upper)
    return x_final * ke

def solve_2C_micro(ka, k10, k12, k21, Vc, times, dt=0.02):
    Xg, Xc, Xp = 1.0, 0.0, 0.0
    t_current = 0.0
    results, idx_times = [], 0
    max_time = times[-1]

    while t_current <= max_time + 1e-9:
        while idx_times < len(times) and t_current >= times[idx_times]-1e-9:
            Cp = Xc / Vc
            results.append(Cp)
            idx_times += 1
            if idx_times >= len(times):
                break

        dXg = -ka * Xg
        dXc = ka * Xg - k10 * Xc - k12 * Xc + k21 * Xp
        dXp = k12 * Xc - k21 * Xp

        Xg += dXg * dt
        Xc += dXc * dt
        Xp += dXp * dt
        t_current += dt

    return np.array(results)

def SSR_2C_micro(params, t_obs, cp_obs):
    ka, k10, k12, k21, Vc = params
    if any(p <= 0 for p in params):
        return 1e12

    cp_pred = solve_2C_micro(ka, k10, k12, k21, Vc, t_obs)
    if np.any(cp_pred < 0) or len(cp_pred) != len(cp_obs):
        return 1e12

    ssr = np.sum((cp_obs - cp_pred)**2)
    return ssr
