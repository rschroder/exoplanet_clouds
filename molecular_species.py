
H20_liquid_1_e = {
    'name'     : "$H_{2}O \ Liquid$",
    'ln_c'     : 25.096,           # From table II,sanchez-lavega 2003
    'Lo'       : 3148.2,           # From table II,sanchez-lavega 2003
    'alpha'    : 0.,               # From table II,sanchez-lavega 2003
    'beta'     : -8.7*10**(-3),    # From table II,sanchez-lavega 2003
    'Xc'       : 0.015,            # from table III, sanchez-lavega 2003
    'Rv'       : 8.3144598/18.02,  # Remember to plug in mu_cl for cloud vapor
}                                  # From table II,sanchez-lavega 2003

H20_solid_1_e = {
    'name'     : "$H_{2}O \ Solid$",
    'ln_c'     : 25.096,           # From table II,sanchez-lavega 2003
    'Lo'       : 3148.2,           # From table II,sanchez-lavega 2003
    'alpha'    : 0.,               # From table II,sanchez-lavega 2003
    'beta'     : -8.7*10**(-3),    # From table II,sanchez-lavega 2003
    'Xc'       : 2.5*10**(-4),     # from table III, sanchez-lavega 2003
    'Rv'       : 8.3144598/18.02,  # Remember to plug in mu_cl for cloud vapor
}                                  # From table II,sanchez-lavega 2003

SO4H2_liquid_1_v = {
    'name'     : "$SO_{4}H_{2} \ Solid \ 1$",
    'ln_c'     : 16.256,           # From table II,sanchez-lavega 2003
    'Lo'       : 865.8,           # From table II,sanchez-lavega 2003
    'alpha'    : 0.,               # From table II,sanchez-lavega 2003
    'beta'     : 0,                # From table II,sanchez-lavega 2003
    'Xc'       : 2.0*10**(-6),     # from table III, sanchez-lavega 2003
    'Rv'       : 8.3144598/98.08,  # Remember to plug in mu_cl for cloud vapor
}                                  # From table II,sanchez-lavega 2003

SO4H2_liquid_2_v = {
    'name'     : "$SO_{4}H_{2} \ Solid \ 2$",
    'ln_c'     : 16.256,           # From table II,sanchez-lavega 2003
    'Lo'       : 865.8,           # From table II,sanchez-lavega 2003
    'alpha'    : 0.,               # From table II,sanchez-lavega 2003
    'beta'     : 0,                # From table II,sanchez-lavega 2003
    'Xc'       : 2.0*10**(-3),     # from table III, sanchez-lavega 2003
    'Rv'       : 8.3144598/98.08,  # Remember to plug in mu_cl for cloud vapor
}                                  # From table II,sanchez-lavega 2003

CO2_solid_1_m = {
    'name'     : "$CO_{2} \ Solid$",
    'ln_c'     : 26.100,           # From table II,sanchez-lavega 2003
    'Lo'       : 639.6,           # From table II,sanchez-lavega 2003
    'alpha'    : 0.,               # From table II,sanchez-lavega 2003
    'beta'     : -1.7*10**(-3),    # From table II,sanchez-lavega 2003
    'Xc'       : 0.95,            # from table III, sanchez-lavega 2003
    'Rv'       : 8.3144598/44.01,  # Remember to plug in mu_cl for cloud vapor
}                                  # From table II,sanchez-lavega 2003

H20_solid_1_m = {
    'name'     : "$H_{2}O \ Solid$",
    'ln_c'     : 25.096,           # From table II,sanchez-lavega 2003
    'Lo'       : 3148.2,           # From table II,sanchez-lavega 2003
    'alpha'    : 0.,               # From table II,sanchez-lavega 2003
    'beta'     : -8.7*10**(-3),    # From table II,sanchez-lavega 2003
    'Xc'       : 3.0*10**(-4),     # from table III, sanchez-lavega 2003
    'Rv'       : 8.3144598/18.02,  # Remember to plug in mu_cl for cloud vapor
}                                  # From table II,sanchez-lavega 2003
NH3_solid_1_saturn = {
    'name'     : "$NH_{3} \ Solid$",
    'ln_c'     : 27.863,           # From table II,sanchez-lavega 2003
    'Lo'       : 2016.,           # From table II,sanchez-lavega 2003
    'alpha'    : -0.888,               # From table II,sanchez-lavega 2003
    'beta'     : 0,    # From table II,sanchez-lavega 2003
    'Xc'       : 2.0*10**(-4),     # from table III, sanchez-lavega 2003
    'Rv'       : 8.3144598/17.00,  # Remember to plug in mu_cl for cloud vapor
}

FE_solid_1_HD209458b = {
    'name'     : "$Fe \ Solid$",
#    'ln_c'     : 15.71,           # From marley
    'ln_c'     : 1.894,           # From table II,sanchez-lavega 2003
#    'Lo'       : 6250.,           # From table II,sanchez-lavega 2003
    'Lo'       : 7097.,           # From table II,sanchez-lavega 2003
    'alpha'    : 0.,               # From table II,sanchez-lavega 2003
    'beta'     : 0,    # From table II,sanchez-lavega 2003
    'Xc'       : 6.77*10**(-5),     # from table III, sanchez-lavega 2003
    'Rv'       : 8.3144598/55.84,  # Remember to plug in mu_cl for cloud vapor
}

MGSIO3_solid_1_HD209458b = {
    'name'     : "$MgSiO_{3} \ Solid$",
#    'ln_c'     : 25.37,           # From marley
    'ln_c'     : 11.554,           # From table II,sanchez-lavega 2003
#    'Lo'       : 4500.5,           # From table II,sanchez-lavega 2003
    'Lo'       : 4877.5,           # From table II,sanchez-lavega 2003
    'alpha'    : 0.,               # From table II,sanchez-lavega 2003
    'beta'     : 0,    # From table II,sanchez-lavega 2003
    'Xc'       : 7.52*10**(-5),     # from table III, sanchez-lavega 2003
    'Rv'       : 8.3144598/100.4,  # Remember to plug in mu_cl for cloud vapor
}
