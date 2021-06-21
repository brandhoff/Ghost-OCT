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

cmap = pl.cm.viridis

# Get the colormap colors
my_cmap = cmap(np.arange(cmap.N))

# Set alpha
my_cmap[:,-1] = np.linspace(0, 1, cmap.N)

# Create new colormap
my_cmap = ListedColormap(my_cmap)
colors = cmap(np.linspace(0,1,4))

datas = []


filePRefix = r"D:\uni\PPraktikum\OCT\scripts\messwerte\platte_unbeschichtet//"
maxima = []

for i in range(1,4):
    data = pd.read_csv(filePRefix+"plaettchen_unbeschichtet_"+ str(i)+"_FFT.speck", sep=',')
    data['x'] = data['x'] / 1000
    datas.append(data)

data_switch = datas[-1]
datas[-1] = datas[1]
datas[1] = data_switch

print(datas)
fig, axes = plt.subplots(1,3,sharey=True, facecolor='w',figsize=(11,8))
for i,data in enumerate(datas):
    data.plot.scatter(ax = axes[i], s=5, x='x', y= 'intensity',c = colors[i])
fig.tight_layout()

legend_elements = [Line2D([0], [0], color='none', lw=2, label='Mirror at '),
                   Line2D([0], [0], color=colors[0], lw=2, label='$x= 21.5\mu m$'),
                   Line2D([0], [0], color=colors[1], lw=2, label='$x= 106.5\mu m$'),
                   Line2D([0], [0], color=colors[2], lw=2, label='$x= 127.5\mu m$'),
                   Line2D([0], [0], color='red', lw=2, label='Constant Peak at: '),
                   Line2D([0], [0], color='none', lw=2, label='$x= 152.0\mu m$')]

axes[2].legend(handles=legend_elements,fontsize = 12,loc=(0.33,0.775)) 

yUpperBound = 200
axes[0].set_ylim(0,yUpperBound)
axes[1].set_ylim(0,yUpperBound)
axes[2].set_ylim(0,yUpperBound)

bbox_props = dict(boxstyle="circle",pad=0.1,fc=(0.8,0.9,0.9,0),  ec="red", lw=1)
#axes[0].annotate("   ",(15,27),fontsize=18, color = "red", xycoords="axes points", bbox=bbox_props)
#axes[1].annotate("   ",(15,27),fontsize=18, color = "red", xycoords="axes points", bbox=bbox_props)
#axes[2].annotate("   ",(15,27),fontsize=18, color = "red", xycoords="axes points", bbox=bbox_props)

axes[0].axvline(-21.5, linewidth=2, color=colors[0])
#axes[0].text(2.2,25000,'HOMO', color = 'black', rotation=90, fontsize=17)

axes[1].axvline(-106.5, linewidth=2, color=colors[1])
axes[1].axvline(-45.1, linewidth=2, color='cornflowerblue')


axes[2].axvline(-127.8, linewidth=2, color=colors[2])
axes[2].axvline(-25.1, linewidth=2, color='cornflowerblue')


axes[0].axvline(-152, linewidth=2, color='red')
axes[1].axvline(-152, linewidth=2, color='red')
axes[2].axvline(-152, linewidth=2, color='red')

axes[1].text(-43.1,120,'Peak at', color = 'cornflowerblue', fontsize=12)
axes[1].text(-43.1,115,'$x= 45.0\mu m$', color = 'cornflowerblue', fontsize=12)

axes[2].text(-23.1,120,'Peak at', color = 'cornflowerblue', fontsize=12)
axes[2].text(-23.1,115,'$x= 25.0\mu m$', color = 'cornflowerblue', fontsize=12)


axes[0].set_xlabel('')
axes[1].set_xlabel('X relative to equal mirror distances in $\mu m$',fontsize=12)

axes[-1].set_xlabel('')

axes[0].set_ylabel('Intensity in a.u.',fontsize=12)

axes[0].tick_params(labelleft=False)

plt.savefig("unbeschichetPlot.pdf");