import numpy as np
from astropy.constants import R

from astropy import constants as const

def P(Po, T, To, g, gamma_ad, R, mu):
    #print 'Po ', Po
    #print 'To ', To
    #print 'g ', g
    #print 'gamma_ad ', gamma_ad
    #print 'R ', R
    #print 'mu ', mu
    pressure = Po * (T / To)**(g/(gamma_ad*R/mu)) # from sanchez-lavega 2003, (eqn. 7)
    #print 'r/mu ', R/mu
    return pressure

#def P_v(T):
#    svp =  1./0.015 * np.e**(25.096 - (6823.15 / T) - 0.019 * T) # from sanchez-lavega 2003,
#    return svp                                                   # (eqn. 19)

def saturation_vapor_pressure(ln_c, T, Lo, beta, alpha, Rv, Xc):
    #print 'ln_c ', ln_c
    #print 'Lo ', Lo
    #print 'beta ', beta
    #print 'alpha ', alpha
    #print 'Rv ', Rv
    #print 'Xc ', Xc
    beta_term = (beta)/Rv
    #print 'beta_term ', beta_term
    alpha_term = (alpha)/Rv
    #print 'alpha_term ', alpha_term
    Lo_term = Lo/Rv
    #print 'Lo_term ', Lo_term
    svp =  1./Xc * np.e**(ln_c +(-Lo_term/T + \
        alpha_term*np.log(T)  + T*beta_term))
    #print 'svp ', svp
    return svp
