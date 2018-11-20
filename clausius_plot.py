import numpy as np
from clausius import *
import matplotlib.pyplot as plt


def plot_pressure_curves(planet, condensates):
    name        = planet['name']
    P_o         = planet['P_o']
    T_o         = planet['T_o']
    g           = planet['g']
    gamma_ad    = planet['gamma_ad']
    mu          = planet['mu']
    T_min       = planet['T_min']
    T_max       = planet['T_max']
    T_step      = planet['T_step']
    P_min       = planet['P_min']
    P_max       = planet['P_max']
    T = np.arange(T_min, T_max, T_step)

    pressure = P(P_o, T, T_o, g, gamma_ad, R.si.value, mu)
    plt.semilogy(T,pressure, label='Theoretical P/T Profile')

    for condensate in condensates:
        species_name = condensate['name']
        ln_c = condensate['ln_c']
        Lo = condensate['Lo']
        alpha = condensate['alpha']
        beta = condensate['beta']
        Xc = condensate['Xc']
        Rv = condensate['Rv']

        svp = saturation_vapor_pressure(ln_c, T, Lo, beta, alpha, Rv, Xc)
        plt.semilogy(T,svp, label=species_name, linestyle = '-.')

    plt.ylim(P_max, P_min)
    plt.xlabel('T(K)')
    plt.ylabel('Pv (bar)')
    plt.title(name)
    plt.legend(loc=0)
    plt.grid(True)
    plt.show()

    return
