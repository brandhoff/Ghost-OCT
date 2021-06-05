# -*- coding: utf-8 -*-
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





"""
Vorbetrachtung:
wir haben eine FFT mit insgeamt 570 gesampelten werten. Insgesamt haben wir 64 solcher FFTs.
der Abstand zweier benachtbarter Punkte betraegt gerundet 191, was damit erstmal unsere aufloesung bestimmt.
Wenn wir von einem Fehler von ca. 1 pixel (also hier einer distanz im Four-Raum) annehmen erwarten wir einen eine schwankung von ca. 382 um einen wert.

Um die distanzen zu bestimmen machen wir jetzt folgendes: von allen der 64 datein die maxima bestimmen (sind jeweils 2, negativ und positiv) hierzu auch direkt die x werte nehmen
(mittels pandas geht das recht simpel) anschließend (x(i+1) - x(i)) rechnen um die distanz zu bekommen. da der 0 abstand zu sich selber ambiguous ist, wird dieser ignoriert und wir
haben am ende 64/2 -1  (31)distanzen raus.

"""







"""
Hier ist Colormap zeug, falls das mal benoetigt werden sollte
"""
cmap = pl.cm.viridis

# Get the colormap colors
my_cmap = cmap(np.arange(cmap.N))

# Set alpha
my_cmap[:,-1] = np.linspace(0, 1, cmap.N)

# Create new colormap
my_cmap = ListedColormap(my_cmap)
colors = cmap(np.linspace(0,1,32))

for i in range(0,32):
    num = 827 - (5*i)
    filePRefix = r"D:\uni\PPraktikum\OCT\scripts\messwerte\spiegel_stellung\fahrt_19_"+str(num)+"_FFT.speck"
    data = pd.read_csv(filePRefix, sep=',')
    data['x'] = data['x'] * np.pi #eigentlich *2Pi aber da ja der optische weg gesucht ist *pi
    datas.append(data)

maxima = [] 
distances = []


fig, ax = plt.subplots(1,1,sharey=True, facecolor='w',figsize=(11,8))
for i,data in enumerate(datas):
    data.plot(ax = ax, x = 'x', y = 'intensity', legend=False) #plotten der datenreihen





plt.title('Mirror positions', fontsize=21)
plt.xlabel('Distance X in nm', fontsize=18)
plt.ylabel('Intensity in a.u.', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='y', which='major', labelsize=0)
plt.savefig('mirrors.pdf')
   #anschauen des maximums (auch schreiben), abstaende werden so berechtet: immer benachtbarte maxima der einzelenen datenreihen
    #anschauen und distanz bilden, dann in distances schreiben und anschließend mittelwert bilden
    #das beruht auf der annahme, dass verbreiterungseffekte erstmal keine rolle spielen (idealer delta peak)
    
    #erstmal nur eine seite der FFT betrachten (positiv):
drops = []





for j, Xs in enumerate(datas[0]['x']):
    if(Xs < 0):
     drops.append(j)
cuts = []
for i,data in enumerate(datas):
    #da alle geleiche positionen haben muss nur einmal alle zu droppenden indices aufgeschrieben werden und nicht fuer alle datas gecylet werden 


    cuts.append(data.drop(data.index[drops]))
for cut in cuts:
   maxima.append(cut[cut['intensity']==cut['intensity'].max()])

for i,maxi in enumerate(maxima):
    if(i != 0 and i+1 != len(maxima)): #peak um 0 ignorieren, da die distanz ja immer 0 zu 0 ist, und da wir abstaende haben darf nicht der abstand zu einem nicht existenten punkt
                                        #gebildet werden
        distances.append(maxima[i+1]['x'].values[0] - maxi['x'].values[0] )
print(np.sum(distances)/len(distances))


#distanzen abspeichern
df = pd.DataFrame()
df.insert(0,"distanze",distances)
df.to_csv("distances.speck", sep='&')
