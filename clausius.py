import numpy as np
from astropy.constants import R

from astropy import constants as const

def cloud_base_location(To, g, P, Po, mu):
    z = (((-8.3144598/mu) * To) / g) * np.log(P/Po)
    return z

def P(Po, T, To, g, gamma_ad, R, mu):
    pressure = Po * (T / To)**(g/(gamma_ad*R/mu)) # from sanchez-lavega 2003, (eqn. 7)
    return pressure
                                               # (eqn. 19)

def saturation_vapor_pressure(ln_c, T, Lo, beta, alpha, Rv, Xc):
    beta_term = (beta)/Rv
    alpha_term = (alpha)/Rv
    Lo_term = Lo/Rv
    svp =  1./Xc * np.e**(ln_c +(-Lo_term/T + \
        alpha_term*np.log(T)  + T*beta_term))
    return svp

def svp_cba(A, B, C, T, Xc):
    Rv = 8.3144598/55.84
    svp =  (1/Xc)*np.e**(A/Rv + B/(T*Rv) + (C*np.log(T))/Rv)
    return svp
