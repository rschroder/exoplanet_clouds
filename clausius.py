import numpy as np
from astropy.constants import R

from astropy import constants as const

def P(Po, T, To, g, gamma_ad, R, mu):
    print 'Po ', Po
    print 'To ', To
    print 'g ', g
    print 'gamma_ad ', gamma_ad
    print 'R ', R
    print 'mu ', mu
    pressure = Po * (T / To)**(g/(gamma_ad*R/mu)) # from sanchez-lavega 2003, (eqn. 7)
    print 'R* ', R/mu
    return pressure
                                               # (eqn. 19)

def saturation_vapor_pressure(ln_c, T, Lo, beta, alpha, Rv, Xc):
    #print 'ln_c ', ln_c
    #print 'Lo ', Lo
    #print 'beta ', beta
    #print 'alpha ', alpha
    #print 'Rv ', Rv
    #print 'Xc ', Xc
    beta_term = (beta)/Rv
    alpha_term = (alpha)/Rv
    Lo_term = Lo/Rv
    svp =  1./Xc * np.e**(ln_c +(-Lo_term/T + \
        alpha_term*np.log(T)  + T*beta_term))
    #print 'svp ', svp
    return svp
