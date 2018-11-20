import numpy as np
from astropy.constants import R

from astropy import constants as const

def P(P_o, T, T_o, g, gamma_ad, R, mu):
    pressure = P_o * (T / T_o)**(g/(gamma_ad*R/mu)) # from sanchez-lavega 2003, (eqn. 7)
    return pressure

#def P_v(T):
#    svp =  1./0.015 * np.e**(25.096 - (6823.15 / T) - 0.019 * T) # from sanchez-lavega 2003,
#    return svp                                                   # (eqn. 19)

def saturation_vapor_pressure(ln_c, T, Lo, beta, alpha, Rv, Xc):
    beta_term = (beta)/Rv
    alpha_term = (alpha)/Rv
    Lo_term = Lo/Rv
    svp =  1./Xc * np.e**(ln_c +(-Lo_term/T + alpha_term*np.log(T)  + T*beta_term))
    return svp
