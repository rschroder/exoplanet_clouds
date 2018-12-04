# Condensate cloud formation in exoplanet atmospheres

To run this code, clone the repo, and then use the plot_pressure_curves functions [In a Jupyter notebook, for example] as in the examples below. Note: Current background on this model can be found here: https://github.com/rschroder/exoplanet_clouds/blob/master/c162_exoplanet_cloud_formation.pdf

```python
%matplotlib inline
from clausius import *
from molecular_species import *
from planet_atmospheres import *
from clausius_plot import *


plot_pressure_curves(venus, [SO4H2_liquid_1_venus, SO4H2_liquid_2_venus])
plot_pressure_curves(earth, [H20_liquid_1_earth, H20_solid_1_earth])
plot_pressure_curves(neptune, [CH4_solid_1_neptune, SH2_solid_1_neptune, NH3_solid_1_neptune,\
                             NH4SH_solid_1_neptune, H20_solid_1_neptune])

plot_pressure_curves(jupiter, [NH3_solid_1_jupiter, NH4SH_solid_1_jupiter, \
                               H20_solid_1_jupiter, H20_liquid_1_jupiter])
plot_pressure_curves(saturn, [NH3_solid_1_saturn, NH4SH_solid_1_saturn, H20_solid_1_saturn])
plot_pressure_curves(titan, [CH4_solid_1_titan, C2H6_solid_1_titan])
plot_pressure_curves(uranus, [CH4_solid_1_uranus, SH2_solid_1_uranus, NH3_solid_1_uranus,\
                             NH4SH_solid_1_uranus, H20_solid_1_uranus])


plot_pressure_curves_cba(hd209458b, 7.100,  -21723,  0.4536)
plot_pressure_curves_cba(WASP43b, 7.100,  -21723,  0.4536) 
plot_pressure_curves_cba(HD189733b, 7.100,  -21723,  0.4536)              


```
