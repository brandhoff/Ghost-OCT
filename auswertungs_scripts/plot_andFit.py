
"""
Created on Sat Jun  5 14:27:52 2021

@author: Jonas
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress
from lmfit import Model, Parameters
from lmfit.models import VoigtModel
from scipy import stats
from matplotlib.lines import Line2D
from random import randint
import matplotlib.pylab as pl
from matplotlib.colors import ListedColormap
datas = []



for i in range(0,180):
    num = i
    filePRefix = r"D:\uni\PPraktikum\OCT\scripts\messwerte\spiegel_fahrt_percise//" + str(num) + "_FFT.speck"
    data = pd.read_csv(filePRefix, sep=',')
    data['x'] = data['x']
    datas.append(data)

maxima_intensity = [] 
maxima_Xs = [] 


fig, ax = plt.subplots(1,1,sharey=True, facecolor='w',figsize=(11,8))
for i,data in enumerate(datas):
    data.plot(ax = ax, x = 'x', y = 'intensity', legend=False) #plotten der datenreihen

plt.title('Mirror positions', fontsize=21)
plt.xlabel('Distance X in nm', fontsize=18)
plt.ylabel('Intensity in a.u.', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='y', which='major', labelsize=0)
plt.savefig('mirrors_fine.pdf')

drops = []

for data in datas:
    ints = data[data['intensity']==data['intensity'].max()]['intensity'].values
    Xs = data[data['intensity']==data['intensity'].max()]['x'].values
    maxima_intensity.append(ints[0])
    maxima_intensity.append(ints[1])

    maxima_Xs.append(Xs[0])
    maxima_Xs.append(Xs[1])


#distanzen abspeichern
df = pd.DataFrame()
df.insert(0,"x",maxima_Xs)
df.insert(0,"int",maxima_intensity)

df.to_csv("maximaData.speck", sep='&')
