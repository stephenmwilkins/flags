

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import cmasher as cmr

from flags.pz import eazy

import flare.plt as fplt



template_set = 'tweak_fsps_QSF_12_v3.spectra.param'

templates = eazy.get_templates(template_set)

print(templates)


left  = 0.15
bottom = 0.15
width = 0.8
height = 0.8

lam_range = [3, 4]


fig = plt.figure(figsize = (3.5, 5))
ax = fig.add_axes((left, bottom, width, height))

for t in templates.values():

    s = (t.log10lam>lam_range[0])&(t.log10lam<lam_range[1])

    ax.plot(t.log10lam[s], np.log10(t.fnu[s]), lw=1)


template_set_id = template_set.split('.')[0]

fig.savefig(f'figs/{template_set_id}.pdf')
