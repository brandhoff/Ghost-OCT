#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:09:21 2021

@author: Jonas Brandhoff
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
from scipy.signal import blackman, hamming
import nfft
import scipy.interpolate as interp

ref_wav, ref_int = [1,2,3,4,5],[1,2,3,4,5]
current_wave, current_int = [1,2,3,4.3,5],[1,2.2783,3,4,5]
lowerBounds = 0
upperBounds = 1000

FFTlower = -10000
FFTupper = 10000

windowFunction = "Hamming"

substract = False
doFFT = True
doWriteAlways = False

writeContinu = False

writeAllAv = False

filePrefix = ""




integrationTime = 10000
averageTotal = 1
averageCount = 1
doAverage = False


doOffset = False
linOffset = 0

doFFTRemoveAv = False
doZeroPad = False


averageSum = []

current_fft_X = [] #um direkt die FFT speicher zu koennen
current_fft_Y= []



#No unopened devices
spec = sm.from_first_available()

liveFig, (axSpec, axFFT) = plt.subplots(2,1)




   





def animate(i): #hauptfunktion mit i als refresh rate bzw. current frame, wird mit jedem refresh neu gecallt
    global spec,integrationTime, current_wave, current_int,ref_wav, ref_int, substract,doFFT
    global liveFig, axSpec, axFFT,doZeroPad
    global averageSum, averageTotal, averageCount,writeContinu,linOffset,doOffset,doFFTRemoveAv, current_fft_X, current_fft_Y
    
    
    
    spec.integration_time_micros(integrationTime) #setzt die integrations time. bis jetzt ist der default sinnvoll
    current_wave = spec.wavelengths() #auslesen der spec werte
    current_int = spec.intensities()
    
    if doOffset:
        current_int = current_int - linOffset#wenn ein offset gemacht werden soll wird der hier gesetzt
    
    
    if substract:
        if len(current_int) == len(ref_int):
            current_int = np.divide(current_int, ref_int, out=np.zeros_like(current_int), where=ref_int!=0) 
            #der befehl umgeht das true divide problem, indem er nur elemente beruecksichtigt, die in der ref nicht 0 sind. 
            #momentan wird anstatt inf einfach 0 gegeben. alternativ waere Nan
    
    wavelengths_cut = [] #bereitet gecuttete arrays vor 
    intensity_cut = []
    #WICHTIG!#
    #Das cuttet tatsaechliche werte, damit wird spaeter die fft nur mit den gecutteten werten durchgefuerht dadurch
    #werden oberschwingungen um die null verhindert. 
    for idx, wv in enumerate(current_wave):
        if wv > lowerBounds and wv < upperBounds:
            wavelengths_cut.append(current_wave[idx])
            intensity_cut.append(current_int[idx])
            
    wav = np.asarray(wavelengths_cut)
    its = np.asarray(intensity_cut)

    if doAverage: #wenn ein average gebildet werden soll werden alle aufaddiert und dann durch die zahl geteilt
        if len(averageSum) != len(its): # wenn die laengen nicht stimmen ist das das erste element mit falscher laenge
            averageSum = its
            averageCount = averageCount+1
        else:
          averageSum = averageSum + its #einfach aufsummieren
          averageCount = averageCount+1
          
        if averageCount == averageTotal: #der average wurde erreicht
             its = averageSum/averageTotal #neue avrg its ist also nun summer / anzahl
             averageSum = []
             averageCount=0 #von vorne beginnen
             #Falls filewriting an ist sollen diese auch geschrieben werden
             if writeContinu:
                    df = pd.DataFrame()
                    df.insert(0,"wavelength",wav)
                    df.insert(0,"intensity",its)
                    if filePrefix != "":
                        df.to_csv(str(filePrefix)+"_average.speck")
                    else:
                        df.to_csv("average_spectrum_"+str(datetime.now())+".speck")

        else:
             return
    axSpec.cla()
    axSpec.plot(wav,its) #plottet das spektrum egal um nun averg oder normal

    axFFT.cla()
    if doFFT: #fft beginnt hier
        k = 2*np.pi/wav #nicht aqd achse von Ks 
        start = wav[-1]
        ende = wav[0]
        k2_helper = np.linspace(2*np.pi/start, 2*np.pi/ende, len(wav)) #raender beibehalten aber nun aqd gespaced
        k2 = k2_helper
      
           
           
           
        if windowFunction == "Hamming":
            w=hamming(len(k2))
        else:
            w=blackman(len(k2))
        
        if doFFTRemoveAv:
            its = its-np.mean(its)
        
        
        #k2 entspricht der neuen aqd Achse, nun muessen die wave werte zu der neuen achse interpoliert werden:
            
        f = interp.interp1d(k, its) #interpoliert die bereiche zwischen den Ks und der Intensity
        
        its_aq = f(k2) #mapped die interpolierten werte auf aqud. K2
        fenster_int = w*its_aq
          
           
        if doZeroPad:
           distant_k = k2_helper[1]-k2_helper[0]
           k2 = np.linspace(k2_helper[0] - len(k2_helper)*distant_k, k2_helper[-1] + len(k2_helper)*distant_k, 3*len(wav)) 
       
           fenster_int= np.pad(fenster_int, (len(fenster_int),  len(fenster_int)), 'constant')

        
        transformed = ff.fft(fenster_int) #fuehrt die FFT durch jetzt mit aqud. intensities und gefaltet mit dem fenster
        x = ff.fftfreq(len(k2),k2[1]-k2[0]) #transformiert k2 zu real raum werten
        x *= np.pi
      
        axFFT.plot(x,np.abs(transformed)) #plotten, hier mit x/2, da der optische weg sich verdoppelt, wenn ein spiegel verfahren wird
        #ich haette das lieber im postprocessing aber paul wollte das zum debuggen
        axFFT.set_xlim(FFTlower, FFTupper) #setzt die vom userfestgelget range 
        current_fft_X = x
        current_fft_Y = np.abs(transformed)
ani = matanimation.FuncAnimation(liveFig, animate, interval=10) #aufrufen der hauptfunktion



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
       self.btnTakeRef.clicked.connect(self.takeRef)
       
       self.checkSub.clicked.connect(self.updateParams)
       self.checkFFT.clicked.connect(self.updateParams)
       self.checkWrite.clicked.connect(self.updateParams)
       self.spinLower.valueChanged.connect(self.updateParams)
       self.spinUpper.valueChanged.connect(self.updateParams)
       
       self.spinAverage.valueChanged.connect(self.updateParams)
       self.spinInt.valueChanged.connect(self.updateParams)
       self.checkAverage.clicked.connect(self.updateParams)
       
       
       self.spinFFTlower.valueChanged.connect(self.updateParams)
       self.spinFFTupper.valueChanged.connect(self.updateParams)
       self.comboWindow.currentTextChanged.connect(self.updateParams)
       self.lineEdit.textChanged.connect(self.updateParams)
       self.checkWriteAllAve.clicked.connect(self.updateParams)

       self.spinOffset.valueChanged.connect(self.updateParams)
       self.checkOffset.clicked.connect(self.updateParams)
       self.checkZeroPad.clicked.connect(self.updateParams)

       self.checkFFTAv.clicked.connect(self.updateParams)
       self.btnSaveFFT.clicked.connect(self.takeFFT)
       self.btnExit.clicked.connect(self.close)
    
       
    
    def close(self):
        spec.close()
        exit()

    def takeFFT(self):
        global current_fft_X, current_fft_Y
        if current_fft_X != [] and current_fft_Y != []:
            df = pd.DataFrame()
            df.insert(0,"x",current_fft_X)
            df.insert(0,"intensity",current_fft_Y)
            if filePrefix != "":
                df.to_csv(str(filePrefix)+"_FFT.speck")
            else:
                df.to_csv("FFT_"+str(datetime.now())+".speck") #Diese endung beibehalten, ist eig nur eine csv aber muss
                                                                #ja keiner wissen 
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
        if filePrefix != "":
            df.to_csv(str(filePrefix)+".speck")
        else:
            df.to_csv("spectrum_"+str(datetime.now())+".speck") #Diese endung beibehalten, ist eig nur eine csv aber muss
                                                            #ja keiner wissen 


    def takeRef(self):
        global spec,integrationTime,ref_wav, ref_int, substract,doFFT
        global liveFig, axSpec, axFFT
        
        spec.integration_time_micros(integrationTime)
        ref_wav = spec.wavelengths()
        ref_int = spec.intensities()
        if doOffset:
            ref_int = ref_int - linOffset
        df = pd.DataFrame()
        df.insert(0,"wavelength",ref_wav)
        df.insert(0,"intensity",ref_int)
        if filePrefix != "":
            df.to_csv(str(filePrefix)+".speck")
        else:
            df.to_csv("reference_"+str(datetime.now())+".speck")
        
        
    def exitOut(self):
        global spec
        spec.close()
        exit()
        
    
    
    
    """
    Falls an den parameteren geschraubt wird soll das aktualisiert werden
    """
    def updateParams(self):
        
        
        global doFFT, doAlwaysWrite, substract, lowerBounds, upperBounds, doAverage, averageTotal, integrationTime
        global averageSum,averageCount,writeContinu
        global filePrefix, FFTlower, FFTupper, writeAllAv, windowFunction, doOffset, linOffset, doFFTRemoveAv
        global doZeroPad
        
        averageSum = []
        averageCount=0
        doFFT = self.checkFFT.isChecked()
        doAlwaysWrite = self.checkWrite.isChecked()
        substract = self.checkSub.isChecked()
        
        lowerBounds = self.spinLower.value()
        upperBounds = self.spinUpper.value()
        
        doAverage = self.checkAverage.isChecked()
        averageTotal = self.spinAverage.value()
        #averageTotal = averageTotal * integrationTime / 1000 #streng genommen sind integration und view update nicht
                                                             #im sync weshalb eigentlich das noch verrechnet werden muss
        integrationTime = self.spinInt.value()

        writeContinu = self.checkWrite.isChecked()
        writeAllAv = self.checkWriteAllAve.isChecked()
        filePrefix = self.lineEdit.text()
        
        FFTlower = self.spinFFTlower.value()
        FFTupper = self.spinFFTupper.value()
        
        doOffset = self.checkOffset.isChecked()
        linOffset = self.spinOffset.value()
        doZeroPad = self.checkZeroPad.isChecked()

        doFFTRemoveAv = self.checkFFTAv.isChecked()
        windowFunction = str(self.comboWindow.currentText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())