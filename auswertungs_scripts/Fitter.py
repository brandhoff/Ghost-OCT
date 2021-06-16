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
import scipy.constants as consts

data = pd.read_csv("maximaData.speck", sep='&')
data = data.sort_values(by='x')


data['int'] = data['int']

for i,j in enumerate(data['x']):
    if j < 1000 and j > -1000:
        data = data.drop(i)
        print(str(i)+' **** '+str(j))

scaleInt = data['int'].max()
scaleX = data['x'].max()

#data['int'] = data['int']/scaleInt
#data['x'] = data['x']/scaleX
def plot_Peak(data, label, titel, color, save, savetitle):
    x = data['x'].values;
    y = data['int'].values;
    fit_model = VoigtModel(prefix='peak_')
    params = Parameters()
    params.add_many(
        ('peak_amplitude', 150, True, 0.0, np.inf),
        ('peak_center', 0, False, 0, 0.1),
        ('peak_sigma', 0.2, True, 0.0, np.inf),
        ('peak_gamma', 0.333, True, 0.0, np.inf))
    result = fit_model.fit(y, params, x=x)
    
    print(result.fit_report())
    
    

    
    
    

    fig, ax = plt.subplots(figsize=(8,5))   
    
   # data['int'] = data['int']*scaleInt
   # data['x'] = data['x']*scaleX

    data.plot.scatter(ax = ax, s=5, x='x', y= 'int', c ='blue', label = label)
    
    ax.plot(data['x'], result.best_fit, color='red')
    
    
    peak_amplitude=  1.1256e8
    peak_sigma=     53189.4513
    peak_gamma=     32100.0093
    
   
    
    
    #peak_amplitude *=scaleInt
    #peak_sigma *=scaleX
    
    print(str(peak_amplitude) + '+/-' +str(peak_amplitude*0.0062))
    print(str(peak_sigma) + '+/-' +str(peak_sigma*0.0186))
    print(str(peak_gamma) + '+/-' +str(peak_gamma*0.0438))
        
    fehler_amp = peak_amplitude*0.0062
    fehler_sigma = peak_sigma*0.0186
    fehler_gamma = peak_gamma*0.0438
    
    
    fehler_amp = np.round(fehler_amp, decimals=2)
    peak_sigma = np.round(peak_sigma, decimals=2)
    peak_gamma = np.round(peak_gamma, decimals=2)
     
    peak_amplitude = np.round(peak_amplitude, decimals=2)
    fehler_sigma = np.round(fehler_sigma, decimals=2)
    fehler_gamma = np.round(fehler_gamma, decimals=2) 
    
    legend_elements = [Line2D([0], [0], color='blue', lw=4, label='Maxima der Spiegelstellungen'), Line2D([0], [0], color='red', lw=4, label='Voigt-Fit'),
                       Line2D([0], [0], color='none', lw=4, label='Amplitude: '+ str(peak_amplitude) + '+/-' +str(fehler_amp)), Line2D([0], [0], color='none', lw=4, label='Sigma: '+ str(peak_sigma) + '+/-' +str(fehler_sigma))
                       ,Line2D([0], [0], color='none', lw=4, label='Gamma: '+ str(peak_gamma) + '+/-' +str(fehler_gamma))]

    ax.legend(handles=legend_elements,fontsize = 12,loc=(-0.2,0.8)) 
    
    
    fwhm_gauss = peak_sigma*2*np.sqrt(np.log(2)*2)
    fwhm_lorentz = 2* peak_gamma
    
    fwhm_total = 0.5346*fwhm_lorentz+np.sqrt(0.2166*fwhm_lorentz**2 + fwhm_gauss**2)
    
    print('Tiefen-Auflösung:')
    print(fwhm_total)
    #print(np.sqrt(8*np.log(2))*fwhm_total)
    print('Delta E:')
    deltaE = consts.hbar*consts.c*(4*np.log(2)/(np.pi * fwhm_total*1e-9))
    print(deltaE/consts.elementary_charge)
    deltaLambda = (deltaE*(1000e-9)**2)/(consts.h*consts.c)
    
    print('deltaLambda')
    print(deltaLambda)
    
    print()
    
    
    plt.title(titel)
    plt.xlabel('Distanz in nm')
    plt.ylabel('Intensity')
    plt.gca().invert_xaxis()
    if(save):
        plt.savefig(savetitle+".pdf");
    plt.show()
plot_Peak(data, '', '', 'red', False, 'plots_fit')





"""
   peak_amplitude:  0.90450295 (init = 0.2)
    peak_center:    -8.9528e-12 (init = 0)
    peak_sigma:      0.38874020
    """