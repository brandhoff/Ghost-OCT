#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:09:21 2021

@author: jonas
"""
import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QFileDialog

from MainWindow import Ui_MainWindow
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from seabreeze.spectrometers import Spectrometer as sm
import matplotlib.animation as matanimation
from itertools import count
import scipy.fftpack as ff
from scipy.signal import blackman



ref_wav, ref_int = [1,2,3,4,5],[1,2,3,4,5]
current_wave, current_int = [1,2,3,4.3,5],[1,2.2783,3,4,5]
lowerBounds = 0
upperBounds = 1000
substract = True
doFFT = True
doWriteAlways = False

integrationTime = 10000
averageTotal = 1
averageCount = 1
doAverage = False

#No unopened devices
spec = ""#sm.from_first_available()

liveFig, (axSpec, axFFT) = plt.subplots(2,1)



"""
Hier sind debug sachen da ich kein sts spectrometer habe
"""

def debug(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    axFFT.cla()
    if doFFT:
        
        k = x
        w=blackman(len(k))
        transformed = ff.fft(w*y)
        x = ff.fftfreq(len(k),k[1]-k[0])
        axFFT.plot(x,np.abs(transformed))
        axFFT.set_xlim(0,4)



line, = axSpec.plot([], [], lw=2)
axSpec.set_xlim(0,2)
axSpec.set_ylim(-2,2)
ani = matanimation.FuncAnimation(liveFig, debug, interval=10)


def animate(i):
    global spec,integrationTime, current_wave, current_int,ref_wav, ref_int, substract,doFFT
    global liveFig, axSpec, axFFT
    
    plt.cla()
    spec.integration_time_micros(integrationTime)
    current_wave = spec.wavelengths()
    current_int = spec.intensities()
    
    if substract:
        current_int = current_int - ref_int
    
    wavelengths_cut = []
    intensity_cut = []
    for idx, wv in enumerate(current_wave):
        if wv > lowerBounds and wv < upperBounds:
            wavelengths_cut.append(current_wave[idx])
            intensity_cut.append(current_int[idx])
            
    wav = np.asarray(wavelengths_cut)
    its = np.asarray(intensity_cut)

    axSpec.plot(wav,its)


    if doFFT:
        k = 2*np.pi/wav
        w=blackman(len(k))
        transformed = ff.fft(w*its)
        x = ff.fftfreq(len(k),k[1]-k[0])
        axFFT.plot(x,np.abs(transformed))





class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()


    """
    HIER WERDEN DIE EINZELNEN SIGNALS MIT DEN SLOTS VERBUNDEN
    siehe QT5 Doc
    """
    def connectSignalsSlots(self):
       self.btnLoadRef.clicked.connect(self.loadReference)
       self.btnStart.clicked.connect(self.startSampling)
       self.btnStop.clicked.connect(self.stopSampling)
       self.btnShowRef.clicked.connect(self.showRef)
       self.btnSaveSpec.clicked.connect(self.saveSpec)
       
       self.checkSub.clicked.connect(self.updateParams)
       self.checkFFT.clicked.connect(self.updateParams)
       self.checkWrite.clicked.connect(self.updateParams)
       self.spinLower.valueChanged.connect(self.updateParams)
       self.spinUpper.valueChanged.connect(self.updateParams)
       
       self.spinAverage.valueChanged.connect(self.updateParams)
       self.spinInt.valueChanged.connect(self.updateParams)
       self.checkAverage.clicked.connect(self.updateParams)

       
    """
    oeffnet einen file dialog und schaut ob eine datei ausgewaelt wurde,
    dann wird das spektrum als ref geoeffnet
    """
    def loadReference(self):
        global ref_int
        global ref_wav
        file = QFileDialog.getOpenFileName()
        if file[0] != '':
            data = pd.read_csv(file[0], sep=',', decimal='.')
            ref_wav = data["wavelength"].values
            ref_int = data["intensity"].values
        
       


    def startSampling(self):
        
     
       
        ani.event_source.start()
        plt.show()

    def stopSampling(self):
        ani.event_source.stop()
        
    def showRef(self):
        fig, ax = plt.subplots()
        fig.suptitle('Reference Spectra', fontsize=16)
        ax.plot(ref_wav,ref_int, label="Reference Spectra")
        ax.set_xlabel("Wavelength")
        ax.set_ylabel("Intensity")
        fig.show()


    """
    Speichert das momentane Spektrum ab
    """
    def saveSpec(self):
        df = pd.DataFrame()
        df.insert(0,"wavelength",current_wave)
        df.insert(0,"intensity",current_int)
        df.to_csv("spectrum_"+str(datetime.now())+".speck") #Diese endung beibehalten, ist eig nur eine csv aber muss
                                                            #ja keiner wissen 


    def takeRef(self):
        global spec,integrationTime,ref_wav, ref_int, substract,doFFT
        global liveFig, axSpec, axFFT
        
        spec.integration_time_micros(integrationTime)
        ref_wav = spec.wavelengths()
        ref_int = spec.intensities()
        
        df = pd.DataFrame()
        df.insert(0,"wavelength",ref_wav)
        df.insert(0,"intensity",ref_int)
        df.to_csv("reference"+str(datetime.now())+".speck")
        
        
        
    """
    Falls an den parameteren geschraubt wird soll das aktualisiert werden
    """
    def updateParams(self):
        
        
        global doFFT, doAlwaysWrite, substract, lowerBounds, upperBounds, doAverage, averageTotal, integrationTime
        
        
        doFFT = self.checkFFT.isChecked()
        doAlwaysWrite = self.checkWrite.isChecked()
        substract = self.checkSub.isChecked()
        
        lowerBounds = self.spinLower.value()
        upperBounds = self.spinUpper.value()
        
        doAverage = self.checkAverage.isChecked()
        averageTotal = self.spinAverage.value()
        
        integrationTime = self.spinInt.value()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())