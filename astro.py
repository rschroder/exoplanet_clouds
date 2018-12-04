import numpy as np
from astropy.constants import G
from astropy.constants import M_jup
from astropy.constants import R_jup
from astropy.constants import M_earth
from astropy.constants import R_earth

G = G.si.value
m_j = M_jup.si.value
r_j = R_jup.si.value
m_e = M_earth.si.value
r_e = R_earth.si.value

def g_j(jupiter_masses, jupiter_radii):
    g = (G * m_j * jupiter_masses) / (r_j * jupiter_radii)**2.
    return g

def g_e(earth_masses, earth_radii):
    g = (G * m_e * earth_masses) / (r_e * earth_radii)**2.
    return g
