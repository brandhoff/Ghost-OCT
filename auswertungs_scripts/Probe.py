# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 14:53:16 2021

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

"""
---Maincolors---
cadetblue
coral
darkgoldenrod
yellowgreen
---annotations---
red
cornflowerblue
mediumvioletred
"""



colors = ['cadetblue','yellowgreen'
,
'darkgoldenrod',

'coral']


annot_colors = ['red',
'cornflowerblue',
'mediumvioletred']

datas = []

file2 = '/Users/jonas/OCT/scripts/gold_plaettchen/20nmgold_plaettchen_pos2_10ym.speck'
filePRefix = r"/Users/jonas/OCT/scripts/platte_unbeschichtet/"
maxima = []
data_spek = filePRefix+ r'plaettchen_unbeschichtet_1.speck'

#
dataImp = pd.read_csv(data_spek, sep=',')
dataImp.plot( x='wavelength', y= 'intensity',c = 'red')
dataImp = pd.read_csv(file2, sep=',')
dataImp.plot( x='wavelength', y= 'intensity',c = 'red')
for i in range(1,4):
    data = pd.read_csv(filePRefix+"plaettchen_unbeschichtet_"+ str(i)+"_FFT.speck", sep=',')
    data['x'] = data['x'] / 1000
    datas.append(data)

data_switch = datas[-1]
datas[-1] = datas[1]
datas[1] = data_switch

fig, axes = plt.subplots(1,3,sharey=True, gridspec_kw={'wspace': 0}, facecolor='w',figsize=(11,8))

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


legend_elements = [
                   
                   Line2D([0], [0], color='red', lw=2, label='Constant Peak at: '),
                   Line2D([0], [0], color='none', lw=2, label='$x= 152.0\mu m$')]



legend_ax0 = [Line2D([0], [0], color='none', lw=2, label='Mirror at '),
                   Line2D([0], [0], color=colors[0], lw=2, label='$x= 21.5\mu m$')]

legend_ax1 = [Line2D([0], [0], color='none', lw=2, label='Mirror at '),
                   Line2D([0], [0], color=colors[1], lw=2, label='$x= 106.5\mu m$')]

legend_ax2 = [Line2D([0], [0], color='none', lw=2, label='Mirror at '),
                   Line2D([0], [0], color=colors[2], lw=2, label='$x= 127.5\mu m$')]



axes[0].legend(handles=legend_ax0,fontsize = 12,loc=(0.25,0.9)) 
axes[1].legend(handles=legend_ax1,fontsize = 12,loc=(0.25,0.9)) 
axes[2].legend(handles=legend_ax2,fontsize = 12,loc=(0.25,0.9)) 


#axes[2].legend(handles=legend_elements,fontsize = 12,loc=(0.33,0.775)) 

yUpperBound = 200
axes[0].set_ylim(0,yUpperBound)
axes[1].set_ylim(0,yUpperBound)
axes[2].set_ylim(0,yUpperBound)


axes[0].set_xlim(0,170)
axes[1].set_xlim(0,170)
axes[2].set_xlim(0,170)

bbox_props = dict(boxstyle="circle",pad=0.1,fc=(0.8,0.9,0.9,0),  ec="red", lw=1)
#axes[0].annotate("   ",(15,27),fontsize=18, color = "red", xycoords="axes points", bbox=bbox_props)
#axes[1].annotate("   ",(15,27),fontsize=18, color = "red", xycoords="axes points", bbox=bbox_props)
#axes[2].annotate("   ",(15,27),fontsize=18, color = "red", xycoords="axes points", bbox=bbox_props)



linewidths = 14

axes[0].axvline(21.5, linewidth=linewidths, color=colors[0], alpha=0.1)

axes[1].axvline(106.5, linewidth=linewidths, color=colors[1], alpha=0.1)
axes[1].axvline(45.1, linewidth=linewidths, color=annot_colors[1], alpha=0.1)


axes[2].axvline(127.8, linewidth=linewidths, color=colors[2], alpha=0.1)
axes[2].axvline(25.1, linewidth=linewidths, color=annot_colors[1], alpha=0.1)


axes[0].axvline(152, linewidth=linewidths, color=annot_colors[0], alpha=0.1)
axes[1].axvline(152, linewidth=linewidths, color=annot_colors[0], alpha=0.1)
axes[2].axvline(152, linewidth=linewidths, color=annot_colors[0], alpha=0.1)


axes[1].text(43.1,120,'Peak at', color = annot_colors[1], fontsize=12)
axes[1].text(43.1,115,'$x= 45.0\mu m$', color = annot_colors[1], fontsize=12)

axes[2].text(23.1,120,'Peak at', color = annot_colors[1], fontsize=12)
axes[2].text(23.1,115,'$x= 25.0\mu m$', color = annot_colors[1], fontsize=12)







drops = []

for j, Xs in enumerate(datas[0]['x']):
    if(Xs < 0):
     drops.append(j)
cuts = []
for i,data in enumerate(datas):
    cuts.append(data.drop(data.index[drops]))

for i,data in enumerate(cuts):
    
    data.plot.scatter(ax = axes[i], s=5, x='x', y= 'intensity',c = colors[i])


axes[0].set_ylabel('Intensity in a.u.',fontsize=12)

axes[0].tick_params(labelleft=False)
axes[0].set_xlabel('')
axes[1].set_xlabel('X relative to equal mirror distances in $\mu m$',fontsize=12)

axes[-1].set_xlabel('')
plt.savefig("unbeschichetPlot.pdf");