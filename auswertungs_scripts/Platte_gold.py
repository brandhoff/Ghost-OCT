# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:41:16 2021

@author: Jonas
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
from lmfit import Model, Parameters
from lmfit.models import VoigtModel
from lmfit.models import GaussianModel
from scipy import stats
from matplotlib.lines import Line2D
from random import randint
import matplotlib.pylab as pl
from matplotlib.colors import ListedColormap
import matplotlib as mpl
from collections import OrderedDict


colors = ['cadetblue','yellowgreen'
,
'darkgoldenrod',

'coral']


annot_colors = ['red',
'cornflowerblue',
'mediumvioletred']

datas = []

filePRefix = r"/Users/jonas/OCT/scripts/gold_plaettchen/"

maxima = []

for i in range(1,7):
    data = pd.read_csv(filePRefix+"20nmgold_plaettchen_pos"+ str(i)+"_FFT.speck", sep=',')
    data['x'] = data['x'] / 1000
    datas.append(data)



fig, axes = plt.subplots(1,3,sharey=True,sharex=True, gridspec_kw={'wspace': 0,'hspace': 0}, facecolor='w',figsize=(11,8))




drops = []

for j, Xs in enumerate(datas[0]['x']):
    if(Xs < 0):
     drops.append(j)
cuts = []
for i,data in enumerate(datas):
    cuts.append(data.drop(data.index[drops]))


#Drei asugewaehlte plots um zu unbeschichtet besser zu vergleichen
#eventuell beide uebereinander?
cuts[1].plot.scatter(ax = axes[0], s=5, x='x', y= 'intensity',c = colors[0])
cuts[2].plot.scatter(ax = axes[1], s=5, x='x', y= 'intensity',c = colors[1])
cuts[3].plot.scatter(ax = axes[2], s=5, x='x', y= 'intensity',c = colors[2])


fig.tight_layout()






fig.tight_layout()


axes[1].tick_params(
    axis='y',          
    which='both',      
    left=False,      
    right=False,        
    labelleft=False)
axes[2].tick_params(
    axis='y',          
    which='both',      
    left=False,      
    right=False,        
    labelleft=False)

axes[0].spines['right'].set_visible(False)

axes[1].spines['left'].set_visible(False)
axes[1].spines['right'].set_visible(False)

axes[2].spines['left'].set_visible(False)

axes[0].tick_params(axis="y",direction="in", pad=-22)

axes[0].tick_params(axis="x",direction="in")
axes[1].tick_params(axis="x",direction="in")
axes[2].tick_params(axis="x",direction="in")




yUpperBound = 70



axes[0].set_ylim(0,yUpperBound)
axes[1].set_ylim(0,yUpperBound)
axes[2].set_ylim(0,yUpperBound)


axes[0].set_xlim(0,170)
axes[1].set_xlim(0,170)
axes[2].set_xlim(0,170)



linewidths = 14


axes[0].axvline(101, linewidth=linewidths, color=colors[0], alpha=0.1)
axes[1].axvline(110, linewidth=linewidths, color=colors[1], alpha=0.1)
axes[2].axvline(119.5, linewidth=linewidths, color=colors[2], alpha=0.1)

axes[0].set_ylabel('Intensity in a.u.',fontsize=12)

axes[0].tick_params(labelleft=False)
axes[0].set_xlabel('')
axes[1].set_xlabel('X relative to equal mirror distances in $\mu m$',fontsize=12)

axes[-1].set_xlabel('')


legend_ax0 = [Line2D([0], [0], color='none', lw=2, label='Mirror at '),
                   Line2D([0], [0], color=colors[0], lw=2, label='$x= 101\mu m$')]

legend_ax1 = [Line2D([0], [0], color='none', lw=2, label='Mirror at '),
                   Line2D([0], [0], color=colors[1], lw=2, label='$x= 110\mu m$')]

legend_ax2 = [Line2D([0], [0], color='none', lw=2, label='Mirror at '),
                   Line2D([0], [0], color=colors[2], lw=2, label='$x= 120\mu m$')]



axes[0].legend(handles=legend_ax0,fontsize = 12,loc=(0.25,0.9)) 
axes[1].legend(handles=legend_ax1,fontsize = 12,loc=(0.25,0.9)) 
axes[2].legend(handles=legend_ax2,fontsize = 12,loc=(0.25,0.9)) 


axes[0].axvline(163, linewidth=linewidths, color=annot_colors[0], alpha=0.1)
axes[1].axvline(163, linewidth=linewidths, color=annot_colors[0], alpha=0.1)
axes[2].axvline(163, linewidth=linewidths, color=annot_colors[0], alpha=0.1)


axes[0].axvline(12, linewidth=linewidths, color=annot_colors[1], alpha=0.1)
axes[1].axvline(12, linewidth=linewidths, color=annot_colors[1], alpha=0.1)
axes[2].axvline(12, linewidth=linewidths, color=annot_colors[1], alpha=0.1)

axes[1].axvline(42, linewidth=linewidths, color=annot_colors[2], alpha=0.1)
axes[2].axvline(42, linewidth=linewidths, color=annot_colors[2], alpha=0.1)
plt.savefig("goldPlot.pdf");