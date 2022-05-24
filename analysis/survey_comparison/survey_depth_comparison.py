

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import cmasher as cmr

from flags.surveys import jwst


import flare.plt as fplt


surveys = ['FAKE', 'GLASS','CEERS','PEARLS','COSMOS-Web','PRIMER','NGDEEP']


fig, ax = fplt.simple()


import flare.filters

filters = ['Hubble.ACS.f814w']+[f'Webb.NIRCAM.{f}' for f in ['F070W','F090W','F115W','F150W','F200W','F277W','F356W','F410M','F444W']]
F = flare.filters.add_filters(filters) # --- NOTE: need to give it the redshifted

# --- pre compute pivot wavelength
pivwv = {filter: F[filter].pivwv() for filter in filters}


f = 'Webb.NIRCAM.F150W'




for survey_name, c in zip(surveys, cmr.take_cmap_colors('cmr.bubblegum', len(surveys), cmap_range = (0.0,1.0))):

    survey = jwst.survey[survey_name]

    for field, ls in zip(survey.fields_, ['-','--','-.',':']):

        if survey_name == 'FAKE':
            lw = 2
        else:
            lw = 1

        depths_mag = field['depths_mag']
        print(depths_mag)

        x = np.array([pivwv[filter] for filter in field['filters']])/1E4
        y = np.array([depths_mag[filter] for filter in field['filters']])

        idx = np.argsort(x)

        ax.scatter(x[idx],y[idx], s=5, alpha = 1.0, c=c)
        ax.plot(x[idx],y[idx], ls=ls, lw=lw, alpha = 1.0, c=c)







area_lims = np.array([0, 1.5])

ax.legend(fontsize = 7)

# ax.set_xlim([26.2, 31.])
# ax.set_ylim(area_lims)

ax.set_ylabel(rf"$\rm {f.split('.')[-1]}\ {{\bf depth}}\ (5\sigma\ point\ source)$")
ax.set_xlabel(r"$\rm \lambda/\mu m$")

fig.savefig(f"figs/survey_depth_comparison.pdf")
