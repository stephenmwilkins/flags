

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import cmasher as cmr

from flags.surveys import jwst


import flare.plt as fplt


fig, ax = fplt.simple()


f = 'Webb.NIRCAM.F150W'

for survey, c in zip(jwst.surveys['Cycle 1'], cmr.take_cmap_colors('cmr.bubblegum', len(jwst.surveys['Cycle 1']), cmap_range = (0.0,1.0))):

    x,y = survey.get_cumulative_area(f)

    ax.plot(x,y, ls='-', lw=1, alpha = 1.0, label = rf'$\rm {survey.name}$', c=c)


x,y = jwst.survey['Public Cycle 1'].get_cumulative_area(f)
ax.plot(x,y, ls='-', lw=2, alpha = 1.0, label = rf'$\rm Public\ Cycle 1$', c='k')

x,y = jwst.survey['Cycle 1'].get_cumulative_area(f)
ax.plot(x,y, ls='-', lw=2, alpha = 0.5, label = rf'$\rm Cycle 1$', c='k')


# x = Area['With WAFLS']['x']
#
#
# interp_func = interpolate.interp1d(Area['Without WAFLS']['x'][::-1], Area['Without WAFLS']['y'][::-1], kind='nearest')
#
# ax.fill_between(x, Area['With WAFLS']['y'], interp_func(x), color=WAFLS.c, alpha=0.1, label = r'$\rm WAFLS\ gain$')


area_lims = np.array([0, 1.5])

ax.legend(fontsize = 7)

ax.set_xlim([26.2, 31.])
ax.set_ylim(area_lims)

ax.set_xlabel(rf"$\rm {f.split('.')[-1]}\ {{\bf depth}}\ (5\sigma\ point\ source)$")
ax.set_ylabel(r"$\rm {\bf cumulative\ area}/deg^2$")

fig.savefig(f"figs/surveys.pdf")
