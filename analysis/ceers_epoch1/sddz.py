


import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.lines import Line2D
import cmasher as cmr

import flare

from flare.photom import m_to_flux

import flare.plt as fplt

from flare_lf.utilities import m_to_fnu

import flare_lf.lf as lf
import flare_lf.plots as plots
import flare_lf.completeness as completeness

import flags_data.distribution_functions as fd


from flags.surveys import jwst

cosmo = flare.default_cosmo()

size = 3.5
fig = plt.figure(figsize = (size, size))
left  = 0.15
height = 0.8
bottom = 0.15
width = 0.8
ax = fig.add_axes((left, bottom, width, height))

m_limit = 28.6
flux_limit = m_to_fnu(m_limit)
area = 1.


models = ['/'.join(x.split('/')[1:]) for x in fd.list_datasets('LUV/models')]
print(models)

models = ['models/schechter/bluetides', 'models/schechter/tng-a', 'models/schechter/mason2015', 'models/schechter/fire-2', 'models/binned/croc', 'models/binned/flares', 'models/binned/scsam', 'models/binned/coda', 'models/binned/universe_machine', 'models/binned/dragons']

reverse_model = lambda x: '/'.join(x.split('/')[::-1])


models = list(map(reverse_model, sorted(list(map(reverse_model, models)))))
print(models)


#  # has variable binning

# models = ['models/binned/flares','models/binned/scsam','models/schechter/bluetides','models/schechter/mason2015']



dz = 0.1
y_limits = np.array([-1.99, 3.5])
colors = cmr.take_cmap_colors('cmr.guppy', len(models))

for model, ls, color in zip(models, ['-','-.','--',':']*5, colors):

    print(model)
    ty = model.split('/')[1]
    m = lf.read(model)

    redshift_limits_ = [m.redshifts[0], m.redshifts[-1]]

    bin_edges, bin_centres, N_tot = m.N(redshift_limits = redshift_limits_, log10L_limits = [27., 30.], dz = dz, dlog10L = 0.1, cosmo = cosmo)

    # --- simple completeness
    C = completeness.completeness_cut(bin_centres, flux_limit, cosmo = flare.default_cosmo())

    # --- get expected number of galaxies
    N = np.multiply(N_tot, C) * area
    n = np.sum(N, axis=0)[::-1]
    ndz = n/dz

    l = m.name.replace(" ",r"\ ")

    ax.plot(bin_centres['z'][::-1], np.log10(ndz), c=color, alpha = 0.7, lw=1, ls = ls, label = rf'$\rm {l}\ [{ty}]$')

# ax.text(0.95, 0.85, rf'$\rm\bf S/N({filter.split(".")[-1]})>{detection_snr:.0f}$', ha='right', fontsize = 9, color = 'k', transform=ax.transAxes)


ax.legend(loc = 'upper right', fontsize = 8, title = rf'$\rm m<{m_limit}$', labelspacing = 0.1)


# ax.set_ylimits([-10, 2])
ax.set_xlim([5, 15])
ax.set_ylim(y_limits)
ax.set_xlabel(r'$\rm z$')
ax.set_ylabel(rf'$\rm log_{{10}}[N\ dz/arcmin^2]$')

fig.savefig(f'figs/sddz.pdf')
