H20_liquid = {
    'name'     : "$H_{2}O \ Liquid$",
    'ln_c'     : 25.096,           # From table II,sanchez-lavega 2003
    'Lo'       : 3148.2,           # From table II,sanchez-lavega 2003
    'alpha'    : 0.,               # From table II,sanchez-lavega 2003
    'beta'     : -8.7*10**(-3),    # From table II,sanchez-lavega 2003
    'Xc'       : 0.015,            # from table III, sanchez-lavega 2003
    'Rv'       : 8.3144598/18.02,  # Remember to plug in mu_cl for cloud vapor
}                                  # From table II,sanchez-lavega 2003

H20_solid = {
    'name'     : "$H_{2}O \ Solid$",
    'ln_c'     : 25.096,           # From table II,sanchez-lavega 2003
    'Lo'       : 3148.2,           # From table II,sanchez-lavega 2003
    'alpha'    : 0.,               # From table II,sanchez-lavega 2003
    'beta'     : -8.7*10**(-3),    # From table II,sanchez-lavega 2003
    'Xc'       : 2.5*10**(-4),     # from table III, sanchez-lavega 2003
    'Rv'       : 8.3144598/18.02,  # Remember to plug in mu_cl for cloud vapor
}                                  # From table II,sanchez-lavega 2003
