#!/usr/bin/env python
# coding: utf-8

# # 1.3 -  Anwendungsbeispiel

# <img style="float: right; margin:5px 0px 0px 10px" src="img/audio.jpg" width="400">
# 
# Diese Notebook baut auf die beiden Vorherigen auf, in denen der FIR und IIR Filterentwurf mit verschiedenen Methoden ausführlich behandelt wurde.
# 
# Im Folgenden soll ein Praxisbeispiel für einer Filterantwendung mit konkreten Randbedingungen bearbeitet werden. Auf ein Audiosignal (akustik.wav, zu finden im Ordner 'data') sollen zunächst Störsignale aufaddiert werden, die anschließend mit verschiedenen Filtern wieder entfernt werden, um das ursprüngliche Signal wiederherzustellen. Dabei sollen die Vor- und Nachteile der verschiedenen Filtertypen aufgezeigt werden.
# 
# Außerdem sollen einige grundlegende Python Module zur Verarbeitung speziell von Audiosignalen vorgestellt und angewendet werden.
# 
# 
# ## Inhalt  
# 
# <table style="width:256px; border: 1px solid black; display: inline-block">
#   <tr>
#     <td  style="text-align:right" width=64px><img src="img/IMG-Python.png" style="float:left"></td>
#       <td style="text-align:left" width=256px>
#           <a style="color:black; font-size:14px; font-weight:bold; text-decoration:none" href='#intro'>1. Audiosignale in Python</a>
#     </td>
#   </tr>  
#     <tr>
#     <td  style="text-align:right" width=64px><img src="img/IMG-fir.jpg" style="float:left"></td>
#       <td style="text-align:left" width=256px>
#           <a style="color:black; font-size:14px; font-weight:bold; text-decoration:none" href='#fir'>2. FIR-Filterung</a>
#     </td>
#   </tr>  
#     <tr>
#     <td  style="text-align:right" width=64px><img src="img/IMG-iir.jpg" style="float:left"></td>
#       <td style="text-align:left" width=256px>
#           <a style="color:black; font-size:14px; font-weight:bold; text-decoration:none" href='#iir'>3. IIR-Filterung</a>
#     </td>
#   </tr>
# </table>
# 
# ---

# <a id='intro'></a><div><img src="img/IMG-Python.png" style="float:left"><h2 style="position: relative; top: 6px; left: 6px">1. Audiosignale in Python</h2></div>
# 
# #### 1.1 Import von Audiodateien
# 
# Um ein Audiosignal zu bearbeiten, muss es zunächst geladen/importiert werden. Dafür werden drei verschiedene Methoden vorgestellt:
# 
# ```python
# path = 'data/akustik.wav'
# 
# # 1. wavfile:
# from scipy.io import wavfile
# sr, audio = wavfile.read(path)
# 
# # 2. wave:
# import wave
# wf = wave.open(path,'rb')
# audio = wf.readframes(1024)
# 
# # 3. librosa:
# import librosa
# audio, sr = librosa.load(path)
# ```
# 
# In diesem Notebook verwenden wir die erste Option [`wavfile()`](https://docs.scipy.org/doc/scipy/reference/io.html?highlight=wavfile#module-scipy.io.wavfile), da es schon in dem Modul `scipy` integriert und somit installiert ist. Schauen Sie sich nun die Audioaufnahme `data/akustik.wav` im Zeit- und Frequenzbereich an. Importieren Sie dafür zuerst die dafür notwendigen Module:
# 

# In[1]:


# Importieren Sie aus scipy die Teilbibliothek "fftpack" 
# Importieren Sie aus  scipy.io die Teilbibliothek "wavfile"
# Importieren Sie aus matplotlib die Teilbibliothek "pyplot" mit dem Alias "plt"
# Importieren Sie das numpy-Modul mit dem Alias "np"

[..]
[..]
[..]
[..]


# In[ ]:


'''
Beispiel: Audiodatei einlesen und visualisieren
'''

# Datei einlesen 
fs_Hz, audioSignal = [..]  # ToDo: Lesen Sie Sample-Rate und das Audiosignal in Arrayform ein 
audioSignal = audioSignal/np.max(np.abs(audioSignal))   # Normalisierung

# Initiale Daten
signalLength = len(audioSignal)                 # Länge des Audiosignals
T_s = signalLength/fs_Hz - 1/fs_Hz              # Zeit
t_s = np.linspace(0, T_s, signalLength)         # Zeitbereich
f_Hz = np.linspace(0, fs_Hz/2, signalLength//2) # Frequenzbereich

# Spectrale
audioSignal_fft = [..]   # ToDo: Führen Sie eine FFT des Audiosignals durch


# Graphische Darstellung
plt.subplot(121)
plt.title('Audiosignal im Zeitbereich')
plt.xlabel('Zeit [s]') 
plt.ylabel('Signalamplitude') 
plt.plot(t_s, audioSignal)

plt.subplot(122)
plt.title('%d Punkte FFT des Audiosignals' %signalLength)
plt.xlabel('Frequenz [Hz]') 
plt.ylabel('|X(f)|') 
plt.ylim(0, 200)
plt.plot(f_Hz, np.abs(audioSignal_fft[:int(signalLength/2)]))

plt.gcf().set_size_inches(15, 5)
plt.show()


# #### 1.2 Abspielen von Audiodateien
# 
# Die Ausgabe von Audiosignalen kann in Python auch mit unterschiedlichen externen Modulen realisiert werden. Falls Sie das Modul nicht installiert haben, können Sie dies via `pip install "module"` durchführen. Hier werden Ihnen drei mögliche Module mit Ihren individuellen Vorzügen vorgestellt:  
# 
# - [`playsound`](https://pypi.org/project/playsound/)   
# Das PlaySound-Modul ist ein plattformübergreifendes Modul, das Audiodateien abspielen kann.

# In[ ]:


from playsound import playsound


# In[ ]:


playsound('data/akustik.wav')


# - [`IPython.display`](https://ipython.org/ipython-doc/dev/api/generated/IPython.display.html)  
# Mit diesem Modul wird die Audiodatei mit einem Audioplayer geöffnet, der anschließend per Klick gestartet werden kann:

# In[ ]:


import IPython.display as ipd


# In[ ]:


ipd.Audio('data/akustik.wav')


# - [`simpleaudio`](https://simpleaudio.readthedocs.io/en/latest/)  
# Das Modul ermöglicht es, sowohl wav-Dateien als auch NumPy-Arrays abgespielt zu können. Diese Eigenschaft ist für dieses Notebook sehr nützlich, weshalb im Weiteren auf `simpleaudio` zurückgegriffen wird.

# In[ ]:


import simpleaudio as sa


# In[ ]:


# Beispiel: wav-Dateien abspielen

# Datei einlesen
wave_obj = sa.WaveObject.from_wave_file('data/akustik.wav')

# abspielen
play_obj = wave_obj.play()
play_obj.wait_done()


# In[ ]:


# Beispiel: NumPy-Arrays (Audiosignal) abspielen

# Datei ablesen 
fs_Hz, audioSignal = wavfile.read('data/akustik.wav')

# abspielen
play_obj = sa.play_buffer(audioSignal, 1, 2, fs_Hz)
play_obj.wait_done()


# In[ ]:


# Beispiel: NumPy-Arrays (Sinussignal) abspielen

# Sinussignal erzeugen
t_s = np.linspace(0, 3, 8000)
sine = np.sin(440 * np.pi * t_s)

# Werte im 16-Bit-Bereich konvertieren
sound = sine * (2**15 - 1) / np.max(sine)
sound = sound.astype(np.int16)

# abspielen
play_obj = sa.play_buffer(sound, 1, 2, 8000)
play_obj.wait_done()


# #### 1.3 Signale bearbeiten / Störsignal erstellen
# 
# Wenn das Audiosignal als numpy-Array vorliegt, kann das Signal sehr leicht bearbeitet werden. Zuerst soll dafür auf die Audiodatei `akustik.wav` ein Sinus mit der Frequenz von 440 Hz addiert werden. Dadurch erhält die Audiodatei ein Störsignal, welches Sie danach wieder davon zu entfernen versuchen. Da gleich das Signal zudem gefenstert werden soll, wird noch das Modul `signal` importiert, um daraus [get_window()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html) zu verwenden.

# In[ ]:


# Importieren Sie aus scipy die Teilbibliotheken "signal" und "fft"
[..]


# In[ ]:


'''
Beispiel: Signal addieren, visualisieren und abspielen
'''

# Datei einlesen (originales Audiosignal)
fs_Hz, audioSignal = [..]   # ToDo: lesen sie die Audiodatei "akustik.wav" mit dem Objekt wavfile.read() ein
audioSignal = [..]          # ToDo: Normalisieren Sie das numpy-Array

# Initialisierung der Variablen
fsin_Hz = [..]              # ToDo: Bestimmen Sie die Sinusfrequenz
signalLength = [..]         # ToDo: Bestimmen Sie die Länge des Audio-Arrays
T_s = [..]                  # ToDo: Bestimmen Sie die Zeitdauer der Aufnahme
t_s = [..]                  # ToDo: Erzeugen Sie das zeitliche Array (nutzen Sie dafür np.linspace())
f_Hz = [..]                 # ToDo: Erzeugen Sie das Array für den Frequenzbereich (nutzen Sie dafür np.linspace())

# Sinussignale erstellen
sine = [..]                 # ToDo: Erzeugen Sie das Sinussignal mit einer Frequenz von 440 Hz im Zeitbereich
sine_fft = [..]             # ToDo: Berechnen Sie mittels FFT den Frequenzbereich des Signals

# Graphische Darstellung
plt.subplot(211)
plt.title('Störsignal im Zeitbereich')
plt.xlabel('Zeit [s]') 
plt.xlim(0, 0.1)
plt.ylabel('Amplitude') 
plt.ylim(-1, 1)
plt.plot(t_s, sine)

plt.subplot(222)
plt.title('Störsignal im Frequenzbereich')
plt.xlabel('Frequenz [rad]') 
plt.ylabel('Amplitude') 
plt.ylim(0, 500)
plt.plot(f_Hz, np.abs(sine_fft[:int(signalLength/2)]))

plt.gcf().set_size_inches(15, 5)
plt.show()


# In[ ]:


# Abspielen des Sinussignals
sound = [..]    # ToDo: Konvertieren sie das Audio-Array "sine" in 16-Bit-Format (INT16) 
play_obj = [..] # ToDo: Abspielen von sound
play_obj.wait_done()


# In[ ]:


# Erzeugung eines mit Sinus gestörten Audiosignals
corruptedAudioSignal = [..]         # ToDo: Addieren Sie das Audiosignal mit dem Sinussignal (im Zeitbereich)
corruptedAudioSignal_fft = [..]     # ToDo: Berechnen Sie mittels FFT den Frequenzbereich des Signals mit Störung


plt.subplot(211)
plt.title('Audiosignal mit Störung im Zeitbereich')
plt.xlabel('Zeit [s]') 
plt.ylabel('Amplitude') 
plt.plot(t, s)

plt.subplot(222)
plt.title('Audiosignal mit Störung im Frequenzbereich')
plt.xlabel('Frequenz [rad]') 
plt.ylabel('Amplitude') 
plt.ylim(0, 500)
plt.plot(f_Hz, np.abs(corruptedAudioSignal_fft[:int(signalLength/2)]))

plt.gcf().set_size_inches(15, 5)
plt.show()


# In[ ]:


# Abspielen des gestörten Signals
sound = [..]    # ToDo: Konvertieren sie das Audio-Array "corruptedAudioSignal" in 16-Bit-Format (INT16) 
play_obj = [..] # ToDo: Abspielen von sound
play_obj.wait_done()


# In[ ]:


# Fensterung (optional)
window = [..]      # ToDo: Erzeugen Sie ein Hanning-Fenster der Länge "signalLength" mit signal.get_window()
corruptedAudioSignal_windowed = [..]  # ToDo: Wenden Sie das Fenster auf das Signal "s" an.
corruptedAudioSignal_windowed_fft = [..]  # ToDo: Berechnen Sie mittels FFT den Frequenzbereich von s_windowed

plt.subplot(211)
plt.title('gefenstertes Audiosignal mit Störung im Zeitbereich')
plt.xlabel('Zeit [s]') 
plt.ylabel('Amplitude') 
plt.plot(t_s, corruptedAudioSignal_windowed)

plt.subplot(222)
plt.title('gefenstertes Audiosignal mit Störung im Frequenzbereich')
plt.xlabel('Frequenz [rad]') 
plt.ylabel('Amplitude') 
plt.ylim(0, 500)
plt.plot(f_Hz, np.abs(corruptedAudioSignal_windowed_fft[:signalLength//2]))

plt.gcf().set_size_inches(15, 5)
plt.show()


# In[ ]:


# Abspielen des gefensterten Störsignals
sound = [..]    # ToDo: Konvertieren sie das Audio-Array "s_windowed" in 16-Bit-Format (INT16) 
play_obj = [..] # ToDo: Abspielen von sound
play_obj.wait_done()


# Mit `corruptedAudioSignal` beziehungsweise `corruptedAudioSignal_windowed` wurde jetzt ein mit einem Sinuston gestörtes Audiosignal erzeugt. Im Folgenden wird nun versucht, mittels der in Notebook 1.1 und 1.2 kennengelernten Filter diese Störung zu filtern und wieder ein dem Original ähnliches Audiosignal zu rekonstruieren.
# 
# ---

# <a id='fir'></a><div><img src="img/IMG-fir.jpg" style="float:left"><h2 style="position: relative; top: 6px; left: 6px">2. FIR-Filterung </h2></div>
# 
# #### 2.1 FIR-Filter mittels IDFT
# 
# Wie in Kapitel 1.1 wird zuerst ein Bandsperrfilter mittels IDFT verwendet und entworfen, um das Sinussignal aus dem Audiosignal zu entfernen. Der Filter soll dabei eine Bandbreite von 60 Hz haben.

# In[ ]:


'''
Beispiel: Entfernen von Signalen mittels selbst definierten FIR-Bandsperrfilter
'''

# Filter
bw_Hz = [..]   # ToDo: definieren Sie die Bandbreite
fcLower_Hz = [..] # ToDo: berechnen Sie die untere Grenzfrequenz der Bandsperre
fcUpper_Hz = [..] # ToDo: berechnen Sie die obere Grenzfrequenz der Bandsperre
fftLength = 2048

# Definition des idealen Frequenzganges der Bandsperre:
f_Hz = np.linspace(0, fs_Hz, fftLength)
H = [..]         # ToDo: Erzeugen Sie mit np.where einen idealen Bandsperrfilter mit Bandbreite 60 Hz

h = [..]         # ToDo: Berechnen Sie die Impulsantwort mittels ifft (ifft-shift nicht vergessen!)


# Filterkern aus der Impulsantwort ausschneiden und Fenstern:
filterLength = 1500;
window = signal.get_window('hanning', filterLength+1)
filterKernel = np.real(h[(fftLength - filterLength)//2:(fftLength + filterLength)//2 + 1])*window
k = np.arange(0, filterKernel.size)

# Frequenzgang des ist-Filters:
H_ist = [..] # ToDo: Berechnen Sie den Frequenzgang von filterKernel mittels FFT


# Plot
plt.subplot(131)
plt.title('Idealer Amplitudenfrequenzgang \n des Bandpasses')
plt.xlabel('Frequenz [Hz]') 
plt.ylabel('$H(e^{j\Omega})$')
plt.xlim([0,1200])
plt.plot(f_Hz, H)

plt.subplot(132)
plt.title('Maskierte und gefensterte \n Impulsantwort des Bandsperrfilters')
plt.xlabel('Sample Index k') 
plt.stem(k, filterKernel, use_line_collection=True)

plt.subplot(133)
plt.title('Tatsächlicher Amplitudenfrequenzgang \n des Bandsperrfilters')
plt.xlabel('Frequenz [Hz]') 
plt.ylabel('$|H(e^{j\Omega})|$') 
plt.plot(f_Hz, H_ist)
plt.xlim([0,1200])

plt.subplots_adjust(left=0.1, right=2, top=0.9)


# In[ ]:


# Filterung
corruptedAudioSignal_filtered = [..] # ToDo: Falten Sie das gestörte Signal "corruptedAudioSignal" mit dem Filter "filterKernel" 
corruptedAudioSignal_filtered_fft = [..] # ToDo: Berechnen Sie den Frequenzgang von corruptedAudioSignal_filtered mittels FFT

# Plot
fPlot_Hz = np.linspace(0, fs_Hz, signalLength)
plt.subplot(121)
plt.title('Audiosignal nach Bandsperrfilterung')
plt.xlabel('Zeit [s]') 
plt.ylabel('Signalamplitude') 
plt.plot(t_s, corruptedAudioSignal_filtered)

plt.subplot(122)
plt.title('Frequenzgang nach Filterung')
plt.xlabel('Frequenz [Hz]') 
plt.ylabel('Amplitude') 
plt.ylim(0, 200)
plt.plot(fPlot_Hz[:signalLength//2], np.abs(corruptedAudioSignal_filtered_fft[:signalLength//2]))

plt.gcf().set_size_inches(15, 10)
plt.show()


# In[ ]:


# Abspielen des mit FIR-gefilterten Signals
sound = [..]    # ToDo: Konvertieren sie das Audiosignal in 16-Bit-Format (INT16) 
play_obj = [..] # ToDo: Abspielen von sound
play_obj.wait_done()


# #### 2.2 FIR-Filter mittels __firwin()__  
# Für solche Anwendungen können wir aber auch die vorhandenen Filter wie [`signal.firwin()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html) in __[`scipy.signal`](https://docs.scipy.org/doc/scipy/reference/signal.html)__ direkt benutzen. Ändern Sie dabei die Ordnung (sie können dafür auch eine for-Schleife mit logarithmisch ansteigender Ordnungszahl implementieren), bis das Ergebnis dem der IDFT ähnelt. <br> _Hinweis_: die Ordnungszahl $n$ kann gerne größer 1000 sein.

# In[ ]:


'''
Aufgabe: Entfernen von Frequenzen mittels signal.firwin() 
'''

# zu verwendende Parameter für firwin()
bw_Hz = 60                                        # Bandbreite
filterOrder = 5001                                # Ordnung
wPass_Hz = [(fsin_Hz-bw_Hz/2), (fsin_Hz+bw_Hz/2)] # Grenzfrequenzen

# Erzeugen des Bandsperrfilters
h_fir = [..]       # ToDo: Erzeugen Sie mit signal.firwin() einen Bandsperrfilter.
H_fir = [..]       # ToDo: Berechnen Sie mittels FFT den Frequenzbereich des Bandpassfilters

# Filterung mit Fenster
corruptedAudioSignal_filtered = [..]  # ToDo: Falten Sie das gestörte Signal "corruptedAudioSignal" mit dem Filter "h_fir" 
corruptedAudioSignal_filtered_fft = [..]  # ToDo: Berechnen Sie mittels FFT den Frequenzbereich des gefilterten Signals

# Graphische Darstellung
fPlot_Hz
plt.subplot(221)
plt.title('Impulsantwort des Filters')
plt.xlabel('Sample Nummer') 
plt.ylabel('Amplitude') 
plt.plot(h_fir)

plt.subplot(222)
plt.title('Spektral des Filters')
plt.xlabel('Frequenz [rad]') 
plt.ylabel('Amplitude') 
plt.plot(fPlot_Hz[:signalLength//2], np.abs(H_fir[:signalLength//2]))

plt.subplot(223)
plt.title('Audiosignal nach Bandsperrfilterung')
plt.xlabel('Zeit [s]') 
plt.ylabel('Amplitude') 
plt.plot(t_s, corruptedAudioSignal_filtered)

plt.subplot(224)
plt.title('Frequenzgang nach Filterung')
plt.xlabel('Frequenz [rad]') 
plt.ylabel('Amplitude') 
plt.ylim(0, 200)
plt.plot(fPlot_Hz[:signalLength//2], np.abs(corruptedAudioSignal_filtered_fft[:signalLength//2]))

plt.gcf().set_size_inches(15, 10)
plt.show()


# In[ ]:


# Abspielen des mit firwin() gefilterten Signals
sound = [..]    # ToDo: Konvertieren sie das Audiosignal in 16-Bit-Format (INT16) 
play_obj = [..] # ToDo: Abspielen von sound
play_obj.wait_done()


# Um einen Bandsperrfilter mit hohem Knick und engem Frequenzbereich zu erzeugen, um nur das Sinussignal zu entfernen, benötigt der FIR-Filter eine große Ordnungszahl. Das bedeutet, dass man für die Umsetzung des Filters viel Speicherplatz benötigt und einen goßen Rechenaufwand hat, was für eine niedrige Effizienz spricht.  
# 
# Um zu analysieren, ob IIR-Filter eine bessere Alternative darstellen, wenn es um effizientes Filterdesign geht, soll nun im nächsten Kapitel dasselbe Signal `corruptedAudioSignal` bzw. `corruptedAudioSignal_windowed` mittels der in Notebook 1.2 kennengelernten Filter und Filterdesign bereinigt werden.
# 
# ---

# <a id='iir'></a><div><img src="img/IMG-iir.jpg" style="float:left"><h2 style="position: relative; top: 6px; left: 6px">3. IIR-Filterung </h2></div>
# 
# #### 3.1 Butterworth Filter
# 
# Zunächst soll ein Butterworth-Filter mit 10. Ordnung und einer Bandbreite $bw = 60$ Hz entworfen werden. Dazu wird, wie in Kapitel 1.2, das Objekt [`signal.butter()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html) zur Erzeugung der Filterkoeffizienten verwendet. Geben Sie sich nun aber mittels `output=sos` die "second-order sections" aus, da mit diesen diekt über das Objekt [`signal.sosfilt()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.sosfilt.html) eine Filterung des Signals durchgeführt werden kann.
# 
# 

# In[ ]:


'''
Beispiel: Entfernen von Signalen mittels IIR-Bandsperrfilters (Butterworth)
'''
# Parameterinitialisierung
bw_Hz = [..]         # ToDo: Angabe der Bandbreite
filterOrder = [..]   # ToDo: Ordnung des IIR-Filters
wPass_Hz = [..]      # ToDo: Frequenzbereich des Sperrbands

# Erzeugen des Bandsperrfilters 
sos =  [..]                              # ToDo: Berechnung der "second-order sections" mittels signal.butter()
w, H_butt = [..]                         # ToDo: Berechnung des Frequenzgangs mittels signal.sosfreqz()

# Filterung 
corruptedAudioSignal_filtered = [..]     # ToDo: IIR-Filterung von "corruptedAudioSignal" mittels signal.sosfilt()
corruptedAudioSignal_filtered_fft = [..] # ToDo: Berechnen Sie mittels FFT den Frequenzbereich des gefilterten Signals

# Graphische Darstellung
plt.subplot(311)
plt.title('Frequenzgang des Butterworth Filters mit Ordnung=%d' %filterOrder)
plt.xlabel('Frequenz [rad]') 
plt.ylabel('Amplitude') 
plt.plot(fPlot_Hz[:signalLength//2], np.abs(H_butt[:int(signalLength/2)]))

plt.subplot(312)
plt.title('Audiosignal nach Filterung')
plt.xlabel('Zeit [s]') 
plt.ylabel('Amplitude') 
plt.plot(t_s, corruptedAudioSignal_filtered)

plt.subplot(313)
plt.title('Frequenzgang nach Filterung')
plt.xlabel('Frequenz [rad]') 
plt.ylabel('Amplitude') 
plt.ylim(0, 200)
plt.plot(fPlot_Hz[:signalLength//2], np.abs(corruptedAudioSignal_filtered_fft[:signalLength//2]))

plt.gcf().set_size_inches(8, 16)
plt.show()


# In[ ]:


# Abspielen des Butterworth-gefilterten Signals (10. Ordnung)
sound = [..]    # ToDo: Konvertieren sie das Audiosignal in 16-Bit-Format (INT16) 
play_obj = [..] # ToDo: Abspielen von sound
play_obj.wait_done()


# Um nun den Butterworth-Filter mit Spezifikationen zu erzeugen, soll nun der Filterentwurf mit Ordnungsselektion durchgeführt werden. Dazu wird das Objekt [signal.buttord()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.buttord.html) verwendet. Dessen Dämpfung soll im Sperrbereich von $fsin\_Hz-bw$ bis $fsin\_Hz+bw$ Hz mindestens 60 dB betragen, während die Dämpfung im Durchlassbereich (außerhalb von [$fsin\_Hz-bw-10, fsin\_Hz+bw+10$] Hz) innerhalb von -10 dB liegen soll.<br>
# Die Bandbreite soll dabei wieder 30 Hz betragen.

# In[ ]:


'''
Aufgabe: Entfernen von Signalen mittels IIR-Bandsperrfilters (Butterworth)
'''
# Ordnungsselektion
bw_Hz = [..]  # ToDo: Angabe der Bandbreite
optOrder, wPass_rad = [..] # ToDo: Berechnung der Ordnungszahl und der Grenzfrequenzen mit signal.buttord() 

# Filterung 
sos = [..]                               # ToDo: Berechnung der "second-order sections" mittels signal.butter()
w, H_butt = [..]                         # ToDo: Berechnung des Frequenzgangs mittels signal.sosfreqz()
corruptedAudioSignal_filtered = [..]     # ToDo: IIR-Filterung von "corruptedAudioSignal" mittels signal.sosfilt()
corruptedAudioSignal_filtered_fft = [..] # ToDo: Berechnung des Frequenzgangs mittels FFT


# Graphische Darstellung
plt.subplot(311)
plt.title('Frequenzgang des Butterworth Filters mit Ordnung=%d' %optOrder)
plt.xlabel('Frequenz [rad]') 
plt.ylabel('Amplitude') 
plt.plot(fPlot_Hz[:signalLength//2], np.abs(H_butt[:int(signalLength/2)]))

plt.subplot(312)
plt.title('Audiosignal nach Filterung')
plt.xlabel('Zeit [s]') 
plt.ylabel('Amplitude') 
plt.plot(t_s, corruptedAudioSignal_filtered)

plt.subplot(313)
plt.title('Frequenzgang nach Filterung')
plt.xlabel('Frequenz [rad]') 
plt.ylabel('Amplitude') 
plt.ylim(0, 200)
plt.plot(fPlot_Hz[:signalLength//2], np.abs(corruptedAudioSignal_filtered_fft[:signalLength//2]))

plt.gcf().set_size_inches(8, 16)
plt.show()


# In[ ]:


# Abspielen des Butterworth-gefilterten Signals (Ordnungsselektion)
sound = [..]    # ToDo: Konvertieren sie das Audiosignal in 16-Bit-Format (INT16) 
play_obj = [..] # ToDo: Abspielen von sound
play_obj.wait_done()


# Im Titel der ersten Graphik wird die Ordnungszahl ausgegeben. Diese ist um mindestens 2 Zehnerpotenzen geringer als die des FIR-Filters. Das bedeutet, dass man für die Umsetzung des IIR-Filters viel weniger Speicherplatz und Rechenleistung benötigt, was die Anwendung des IIR-Filters in diesem Fall viel effizienter macht. 
# 
# ---
# 
# ### 3.2 Chebyshev Filter
# 
# Entwerfen Sie zum Schluss noch einen Chebyshev-Filter vom Typ 2 zur Bereinigung des Audiosignals. Auch hier soll die Ordnungsselektion angewendet werden, wofür das Objekt [`signal.cheb2ord()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cheb2ord.html) zur Verfügung steht.<br>
# Die Bedingungen an den Filter sind wie in 3.1: Die Dämpfung soll im Sperrbereich von $fsin\_Hz-bw$ bis $fsin\_Hz+bw$ Hz mindestens 60 dB betragen, während die Dämpfung im Durchlassbereich (außerhalb von [$fsin\_Hz-bw-10, fsin\_Hz+bw+10$] Hz) innerhalb von -10 dB liegen soll.<br>
# Die Bandbreite soll dabei wieder $bw = 60$ Hz betragen.
# 
# Für die Berechnung des Filters soll nun aber das Objekt [`signal.cheby2()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.cheby2.html) verwendet werden.

# In[ ]:


'''
Aufgabe: Entfernen von Signalen mittels IIR-Bandsperrfilters (Chebyshev II mit Ordnungselektion)
'''



# Ordnungsselektion
bw_Hz = [..]               # ToDo: Angabe der Bandbreite
optOrder, wPass_rad = [..] # ToDo: Berechnung der Ordnungszahl und der Grenzfrequenzen mit signal.cheb2ord() 

# Erzeugen des Bandsperrfilters 
sos = [..]        # ToDo: Berechnung der "second-order sections" mittels signal.cheby2()
w, H_butt = [..]  # ToDo: Berechnung des Frequenzgangs mittels signal.sosfreqz()

# Filterung 
corruptedAudioSignal_filtered =     [..] # ToDo: IIR-Filterung von "s_windowed" mittels signal.sosfilt()
corruptedAudioSignal_filtered_fft = [..] # ToDo: Berechnung des Frequenzgangs mittels FFT


# Graphische Darstellung
plt.subplot(311)
plt.title('Frequenzgang des Chebyshev-II Filters mit Ordnung=%d' %optOrder)
plt.xlabel('Frequenz [rad]') 
plt.ylabel('Amplitude') 
plt.plot(fPlot_Hz[:signalLength//2], np.abs(H_butt[:int(signalLength/2)]))

plt.subplot(312)
plt.title('Audiosignal nach Filterung')
plt.xlabel('Zeit [s]') 
plt.ylabel('Amplitude') 
plt.plot(t_s, corruptedAudioSignal_filtered)

plt.subplot(313)
plt.title('Frequenzgang nach Filterung')
plt.xlabel('Frequenz [rad]') 
plt.ylabel('Amplitude') 
plt.ylim(0, 200)
plt.plot(fPlot_Hz[:signalLength//2], np.abs(corruptedAudioSignal_filtered_fft[:signalLength//2]))
plt.gcf().set_size_inches(8, 16)
plt.show()


# In[ ]:


# Abspielen des Chebyshev-gefilterten Signals (Ordnungsselektion)
sound = [..]    # ToDo: Konvertieren sie das Audiosignal in 16-Bit-Format (INT16) 
play_obj = [..] # ToDo: Abspielen von sound
play_obj.wait_done()


# ---
# 
# Zum Schluss soll nun das bearbeitete Audiosignal gespeichert werden. Dazu kann das Objekt [`wavfile.write()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.write.html) verwendet werden.

# In[ ]:


'''
Beispiel: Daten in eine wav-Datei schreiben
'''
# Pfad einer neuen wav-Datei bestimmen
file_path = 'data/akustik_filtered.wav'

# Audiodaten in 16-Bit-Format konvertieren
data = [..]  # ToDo: Konvertieren sie das Audiosignal in 16-Bit-Format (INT16) 

# Audiodaten schreiben
[..]         # ToDo: Speichern Sie das Audiosignal data in data_path mit fs_Hz-Frequenz ab.

# Testen, ob die Daten erfolgreich gespeichert wurde
[..]         # ToDo: Spielen Sie die gespeicherte Datei mit z.B. playsound() ab.


# ---
# 
# ### References
# 
# 1. Titelbild von [Encarni Mármol](https://lda-audiotech.com/en/2018/10/30/how-to-digitize-analog-audio/)  
# 2. [Play sound in Python](https://pythonbasics.org/python-play-sound/)
# ---
# <div>Notebook erstellt von Arne-Lukas Fietkau, Yifei Li  und <a href="mailto:christoph.wagner@tu-dresden.de?Subject=Frage%20zu%20Jupyter%20Notebook%201.3%20Anwendungsbeispiel" target="_top">Christoph Wagner</a></div>
