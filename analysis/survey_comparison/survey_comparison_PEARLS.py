

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import cmasher as cmr

from flags.surveys import jwst


import flare.plt as fplt



for log in [False, True]:

    fig, ax = fplt.simple()


    f = 'Webb.NIRCAM.F150W'


    x,y = jwst.survey['Cycle 1'].get_cumulative_area(f)
    if log: y = np.log10(y)
    ax.plot(x,y, ls='-', lw=2, alpha = 0.5, label = rf'$\rm Cycle 1$', c='k')

    x,y = jwst.survey['Public Cycle 1'].get_cumulative_area(f)
    if log: y = np.log10(y)
    ax.plot(x,y, ls='-', lw=2, alpha = 1.0, label = rf'$\rm Public\ Cycle 1$', c='k')

    for survey, c, ls in zip(jwst.surveys['Cycle 1'][::-1], cmr.take_cmap_colors('cmr.bubblegum', len(jwst.surveys['Cycle 1']), cmap_range = (0.0,1.0)), ['-','--','-.',':']*4):
        x,y = survey.get_cumulative_area(f)
        if log: y = np.log10(y)

        lw = 1
        if survey.name == 'PEARLS':
            ls = '-'
            lw = 2
            c = 'g'


        ax.plot(x,y,lw=lw, ls=ls, alpha = 1.0, label = rf'$\rm {survey.name}$', c=c)





    ax.legend(fontsize = 7, loc = 'upper right', labelspacing = 0.1)

    ax.set_xlim([26.2, 31.])
    if log:
        ax.set_ylim([-2.9, 0.49])
    else:
        ax.set_ylim([0.001, 1.5])

    ax.set_xlabel(rf"$\rm {f.split('.')[-1]}\ {{\bf depth}}\ (5\sigma\ point\ source)$")


    if log:
        ax.set_ylabel(r"$\rm log_{10}({\bf cumulative\ area}/deg^2)$")
        fig.savefig(f"figs/surveys_log10.pdf")
    else:
        ax.set_ylabel(r"$\rm {\bf cumulative\ area}/deg^2$")
        fig.savefig(f"figs/surveys.pdf")
