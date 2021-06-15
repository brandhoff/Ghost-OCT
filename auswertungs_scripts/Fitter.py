# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:35:04 2021

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


data = pd.read_csv("maximaData.speck", sep='&')
print(data)
data = data.sort_values(by='x')
print(data)


data['int'] = data['int']-48

scaleInt = data['int'].max()
scaleX = data['x'].max()

data['int'] = data['int']/scaleInt
data['x'] = data['x']/scaleX
def plot_Peak(data, label, titel, color, save, savetitle):
    x = data['x'].values;
    y = data['int'].values;
    fit_model = GaussianModel(prefix='peak_')
    params = Parameters()
    params.add_many(
        ('peak_amplitude', 0.2, True, 0.0, np.inf),
        ('peak_center', 0, True, -200, 200),
        ('peak_sigma', 0.7, True, 0.0, 1.0))
    result = fit_model.fit(y, params, x=x)
    
    
    
    peak_amplitude=  0.90450295
    peak_sigma=     0.38874020
    
    peak_amplitude *=scaleInt
    peak_sigma *=scaleX
    
    
    peak_amplitude = np.round(peak_amplitude, decimals=2)
    peak_sigma = np.round(peak_sigma, decimals=2)

    fig, ax = plt.subplots(figsize=(8,5))   
    
    data['int'] = data['int']*scaleInt
    data['x'] = data['x']*scaleX

    data.plot.scatter(ax = ax, s=5, x='x', y= 'int', c ='blue', label = label)
    
    ax.plot(data['x'], result.best_fit*scaleInt, color='red')
    
    legend_elements = [Line2D([0], [0], color='blue', lw=4, label='Maxima der Spiegelstellungen'), Line2D([0], [0], color='red', lw=4, label='Gaussian-Fit'),
                       Line2D([0], [0], color='none', lw=4, label='Amplitude: '+ str(peak_amplitude)), Line2D([0], [0], color='none', lw=4, label='Sigma: '+ str(peak_sigma))]

    ax.legend(handles=legend_elements,fontsize = 18,loc=(0.1,0.8)) 
    
    plt.title(titel)
    plt.xlabel('Distanz in nm')
    plt.ylabel('Intensity')
    plt.gca().invert_xaxis()
    if(save):
        plt.savefig(savetitle+".pdf");
    plt.show()
plot_Peak(data, '', '', 'red', False, 'plots_fit')


peak_amplitude=  0.90450295
peak_sigma=     0.38874020

peak_amplitude *=scaleInt
peak_sigma *=scaleX

print(peak_amplitude)
print(peak_sigma)

"""
   peak_amplitude:  0.90450295 (init = 0.2)
    peak_center:    -8.9528e-12 (init = 0)
    peak_sigma:      0.38874020
    """