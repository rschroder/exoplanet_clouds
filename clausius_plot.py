import csv
import numpy as np
from molecular_species import *
from planet_atmospheres import *
from clausius import *
import matplotlib.pyplot as plt
from labellines import labelLine, labelLines
from scipy.optimize import fsolve
from astropy.io import ascii

def read_venus_pt_profile():
    data_path = 'earth-pt.csv'
    data = ascii.read(data_path, data_start=1)
    return data


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

    plt.figure(figsize=(5,5))
    pressure = P(P_o, T, T_o, g, gamma_ad, R.si.value, mu)
    plt.semilogy(T,pressure, \
        label='Atmosphere P-T Profile', \
        color = 'lightsalmon', \
        linewidth=3)

    #data[:, 1], data[:, 0]
    #actual_pt_profile = read_venus_pt_profile()
    #plt.semilogy(actual_pt_profile['col1'],actual_pt_profile['col2'] * 1.e-5, \
    #    label='NASA P-T Profile', \
    #    color = 'g', \
    #    linewidth=3, \
    #    linestyle = '-.', \
    #    alpha = 0.5)

    constraint_range = [2.0*10**(-6), 2.0*10**(-3)]
    i = 0
    for condensate in condensates:
        species_name = condensate['name']
        ln_c = condensate['ln_c']
        Lo = condensate['Lo']
        alpha = condensate['alpha']
        beta = condensate['beta']
        Xc = condensate['Xc']
        Rv = condensate['Rv']

        i = i + 1
        c0 = plt.cm.Blues(float(i)/len(condensates))
        c1 = plt.cm.Reds(float(i)/len(condensates))
        svp = saturation_vapor_pressure(ln_c, T, Lo, beta, alpha, Rv, Xc)
        plt.semilogy(T,svp, label=species_name, linestyle = '-', \
            linewidth=3, \
            color = c0)

        idx = np.argwhere(np.diff(np.sign(pressure - svp))).flatten()
        cloud_base = cloud_base_location(T_o, g, pressure[idx], P_o, mu)
        plt.plot(T[idx], pressure[idx], 'p', color = c1)
        print str(cloud_base) + ' km'
        print str(T[idx]) + ' K'
        print str(pressure[idx]) + ' bar'
        print ' '

    plt.ylim(P_max, P_min)
    plt.xlabel('T(K)')
    plt.ylabel('Pv (bar)')
    plt.title(name)
    plt.legend(loc=1)
    plt.grid(True)
    plt.show()

    return

def plot_pressure_curves_cba(planet, A, B, C):
    A = A
    B = B
    C = C

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

    plt.figure(figsize=(5,5))
    pressure = P(P_o, T, T_o, g, gamma_ad, R.si.value, mu)
    plt.semilogy(T,pressure, label='Atmosphere P-T Profile', color = 'lightsalmon', \
        linewidth=3)
    #labelLines(plt.gca().get_lines(),align=False,fontsize=10)
    constraint_range = [6.77*10**(-5)]
    i = 0
    for Xc in constraint_range:
        i = i + 1
        c0 = plt.cm.Blues(float(i)/len(constraint_range))
        c1 = plt.cm.Reds(float(i)/len(constraint_range))
        svp = svp_cba(A, B, C, T, Xc)
        plt.semilogy(T,svp, label='Fe - mole fraction ' + str(Xc), linestyle = '-', \
            color = c0, linewidth=3)

        idx = np.argwhere(np.diff(np.sign(pressure - svp))).flatten()
        cloud_base = cloud_base_location(T_o, g, pressure[idx], P_o, mu)
        plt.plot(T[idx], pressure[idx], 'p', color = c1, \
            label = str(cloud_base) + ' km')

    plt.ylim(P_max, P_min)
    plt.xlabel('T(K)')
    plt.ylabel('Pv (bar)')
    plt.title(name)
    plt.legend(loc=0)
    plt.grid(True)
    plt.show()

    return

def plot_pressure_curves_exo(planet, condensate):
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
    Xc = condensate['Xc']
    T = np.arange(T_min, T_max, T_step)

    plt.figure(figsize=(5,5))
    pressure = P(P_o, T, T_o, g, gamma_ad, R.si.value, mu)
    plt.semilogy(T,pressure, \
        label='Atmosphere P-T Profile', \
        color = 'lightsalmon', \
        linewidth=3)

    print Xc

    i = 0
    for Xc_i in Xc:
        species_name = condensate['name']
        ln_c = condensate['ln_c']
        Lo = condensate['Lo']
        alpha = condensate['alpha']
        beta = condensate['beta']
        #Xc = condensate['Xc']
        Rv = condensate['Rv']

        i = i + 1
        c0 = plt.cm.Purples(float(i)/len(Xc))
        c1 = plt.cm.Reds(float(i)/len(Xc))
        svp = saturation_vapor_pressure(ln_c, T, Lo, beta, alpha, Rv, Xc_i)
        plt.semilogy(T,svp, label=species_name, linestyle = '-', \
        linewidth=3, \
        color = c0)

        idx = np.argwhere(np.diff(np.sign(pressure - svp))).flatten()
        cloud_base = cloud_base_location(T_o, g, pressure[idx], P_o, mu)
        plt.plot(T[idx], pressure[idx], 'p', color = c1, \
            label = str(cloud_base) + ' km')

    plt.ylim(P_max, P_min)
    plt.xlabel('T(K)')
    plt.ylabel('Pv (bar)')
    plt.title(name)
    plt.legend(loc=0)
    plt.grid(True)
    plt.show()

    return

#plot_pressure_curves(neptune, [CH4_solid_1_neptune, SH2_solid_1_neptune, NH3_solid_1_neptune,\
#                             NH4SH_solid_1_neptune, H20_solid_1_neptune])
