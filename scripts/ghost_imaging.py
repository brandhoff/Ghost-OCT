'''
we want to retrieve a spectrum via ghost imaging
this can be done either via traditional ghost imaging, differential ghost imaging and normalized ghost imaging
the iterative retrieval via traditional ghost imaging is rather simple:
	we take a reference spectrum to get the illumination pattern of the laser and then muliply it with the object
	intensity, which we get from the camera. this is gives us an approximation of the spectrum, that gets
	iteratively better with each iteration. the reference spectrum is then varied in a chosen way, e.g. randomly,
	and the approximate spectrum from step n-1 is avg with the spectrum obtained in step n. therefore we have to
	take a "cumulative average"
differential and normalized ghost imaging have higher SNRs, but a more complicated spectrum retrieval algorithm
therefore, in a first step we will implement only traditional ghost imaging
'''


import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt


def illumination_pattern(type="random",numer_of_peaks=8):
	#function that returns the input wavelengths for the laser
	wavelengths = np.zeros(number_of_peaks)#hier sollten wir eventuell = [] nehmen und jeden peak mit intensity appenden
	#dann hat der array die form [[peak1Wav,peak1Int], [peak2Wav,peak2Int], ...] damit laufen wir auch nicht gefahr am ende 
	#eine "tote" wellenlaenge zu haben, die div 0 verursacht
	#choose everyone of the input wavelengths randomly in the desired interval
	return wavelengths


#initialisiere spektrometer
#initialisiere kamera
#initialisiere laser-steuerung
#wähle muster der beleuchtung, auswahl zwischen: random und ???
#wähle art der Ghost auswertung: traditional ghost imaging, differential ghost imaging, normalized ghost imaging


#wähle nummer der "ghost-schritte"
step_number = 1000
#großer loop über die einzelnen schritte
for i in range(step_number):

	#get input wavelengths patter
	wavelengths = illumination_pattern()
	#set laser to input wavelengths
	set_wavelengths(wavelengths)
	#lread reference spectrum out, to control if input wavelengths = output wavelengths of laser
	reference_spectrum = read_out_spectrometer()
	#lese objekt-intensität mit kamera aus
	object_intensity = read_out_camera()
	#multipliziere referenz-spektrum mit objekt-intensität

	#taking the cumulative avg
	if i == 0:
		#in the zeroth iteration, no avg has to be taken
		spectrum = reference_spectrum*object_intensity
	else:
		spectrum *= i/(i+1)
		spectrum += reference_spectrum*object_intensity*1/i
	#for differential and normalized ghost imaging, the spectrum will have to be reconstructed differently from
	#the reference spectrum and object intensity

#after number_of_steps the spectrum should be reconstructed and can be handed to the FFT etc.
