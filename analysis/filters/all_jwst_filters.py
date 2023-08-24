"""
A demonstration of filter and filter collections creation and usage.
"""
import numpy as np
import numpy as np
import cmasher as cmr
import matplotlib as mpl
import matplotlib.patheffects as pe
import matplotlib.cm as cm
import matplotlib.pyplot as plt

from synthesizer.filters import Filter, FilterCollection

plt.style.use('http://stephenwilkins.co.uk/matplotlibrc.txt')

filters = []
filters += [f"JWST/NIRCam.{f}" for f in ['F070W', 'F090W', 'F115W', 'F150W', 'F200W', 'F277W', 'F356W', 'F444W']]
filters += [f"JWST/NIRCam.{f}" for f in ['F140M','F162M','F182M','F210M','F250M','F300M','F335M','F360M','F410M','F430M','F460M','F480M']]
filters += [f"JWST/MIRI.{f}" for f in ['F560W','F770W','F1000W','F1130W','F1280W','F1500W','F1800W','F2100W','F2550W']]

cmap = cm.Spectral_r

norm = mpl.colors.Normalize(vmin=np.log10(0.5), vmax=np.log10(26.))

fc = FilterCollection(filter_codes=filters)

fig = plt.figure(figsize=(12,2))

left = 0.025
height = 0.7
bottom = 0.25
width = 0.95

ax = fig.add_axes((left, bottom, width, height))

for i,filter in enumerate(fc):
    wv = np.log10(filter.pivwv()/1E4)
    c = cmap(norm(wv))
    ax.fill_between(filter.lam/1E4, 0.0*filter.lam/1E4, filter.t, color=c, alpha=0.5)
    ax.plot(filter.lam/1E4, filter.t, color=c)

    offset = 0.025-0.15*(i // 2 - i/2)
    print(offset)
    # ax.text(filter.pivwv()/1E4, np.max(filter.t)+offset, filter.filter_code.split('.')[-1],fontsize = 5,ha='center', color=c, path_effects=[pe.withStroke(linewidth=2, foreground="k")])
    

ax.set_xlim([0.6, 30.]) # um
ax.set_ylim([0.0, 0.7]) # um
ax.set_xscale('log')
ax.set_yticks([])
ax.set_xticks([1, 2, 3,4, 5, 6,7,8,9,10, 20, 30])
ax.get_xaxis().set_major_formatter(mpl.ticker.ScalarFormatter())

ax.set_xlabel(r'$\rm \lambda/\mu m$')

fig.savefig('all_jwst_filters.pdf')