

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import cmasher as cmr

from flags.surveys import jwst


import flare.plt as fplt


deg = True
deg = False

fig, ax = fplt.simple()


survey_name = 'FLAGS-DR1'

filter = 'Webb.NIRCAM.F356W'

survey = jwst.survey[survey_name]


for field, c in zip(survey.fields_, cmr.take_cmap_colors('cmr.bubblegum', len(survey.fields_), cmap_range = (0.1,0.9))):

    depth = field['depths_mag'][filter]
    area = field['area']
    if deg: area /= 3600.

    print(field['name'], depth, area)

    ax.plot([0, depth, depth], [area, area, 0], ls='-', lw=1, alpha = 0.7, label = rf"$\rm {field['name']}$", c=c)



# --- plot full area

x,y = survey.get_cumulative_area(filter)

if not deg:
    y = 3600.*np.array(y)



ax.plot(x,y, ls='-', lw=2, alpha = 0.5, label = rf'$\rm {survey.name}$', c='k')






area_lims = np.array([0, np.max(y)*1.4])

ax.legend(fontsize = 7)

ax.set_xlim([26.2, 31.])
ax.set_ylim(area_lims)

ax.set_xlabel(rf"$\rm {filter.split('.')[-1]}\ {{\bf depth}}\ (5\sigma\ point\ source)$")
if deg:
    ax.set_ylabel(r"$\rm {\bf cumulative\ area}/deg^2$")
else:
    ax.set_ylabel(r"$\rm {\bf cumulative\ area}/arcmin^2$")


fig.savefig(f"figs/fields_{survey_name}.pdf")
