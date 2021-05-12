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

def refspectrum():
    spec = sm.from_first_available()
    spec.integration_time_micros(10000)
    wavelengths = spec.wavelengths()
    intensity = spec.intensities()
   
    spec.close()
    return (wavelengths, intensity)


ref_wav, ref_int = [1,2,3,4,5],[1,2,3,4,5]
current_wave, current_int = [1,2,3,4,5],[1,2,3,4,5]
lowerBounds = 0
upperBounds = 1000
substract = True
doFFT = True
doWriteAlways = False

def debug(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    


"""
Hier sind debug sachen da ich kein sts spectrometer habe
"""
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)
ani = matanimation.FuncAnimation(plt.gcf(), debug, interval=10)


def animate(i):
    plt.cla()

    spec = sm.from_first_available()
    spec.integration_time_micros(10000)
    wavelengths = spec.wavelengths()
    intensity = spec.intensities() - ref_int
    wavelengths_cut = []
    intensity_cut = []
    for idx, wv in enumerate(wavelengths):
        if wv > lowerBounds and wv < upperBounds:
            wavelengths_cut.append(wavelengths[idx])
            intensity_cut.append(intensity[idx])
            
    wav = np.asarray(wavelengths_cut)
    its = np.asarray(intensity_cut)

    k = 2*np.pi/wav
    w=blackman(len(k))
    transformed = ff.fft(w*its)
    x = ff.fftfreq(len(k),k[1]-k[0])
    #plt.plot(ref_wav,ref_int)
    #plt.plot(k,its)
    plt.plot(x,np.abs(transformed))
    spec.close()




class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

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

       
    def loadReference(self):
        file = QFileDialog.getOpenFileName()
    

    def startSampling(self):
        
        #ani = matanimation.FuncAnimation(plt.gcf(), debug, interval=10)
       
        ani.event_source.start()
        plt.show()

    def stopSampling(self):
        ani.event_source.stop()
        
    def showRef(self):
        fig, ax = plt.subplots()
        fig.suptitle('Reference Spectra', fontsize=16)
        ax.plot(ref_wav,ref_wav, label="Reference Spectra")
        ax.set_xlabel("Wavelength")
        ax.set_ylabel("Intensity")
        fig.show()

    def saveSpec(self):
        df = pd.DataFrame()
        df.insert(0,"wavelength",current_wave)
        df.insert(0,"intensity",current_int)
        df.to_csv("spectrum_"+str(datetime.now())+".csv")


    def updateParams(self):
        doFFT = self.checkFFT.isChecked()
        doAlwaysWrite = self.checkWrite.isChecked()
        substract = self.checkSub.isChecked()
        
        lowerBounds = self.spinLower.value()
        upperBounds = self.spinUpper.value()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())