#!/usr/bin/env python
# coding: utf-8

# # 3.1 - Short Time Fourier Transformation

# <img style="float: right; margin:5px 0px 0px 10px" src="img/1-Titel.png" width="400">
# 
# Die Kurzzeit-Fourier-Transformation (Englisch: "short-time-fourier-tranform", kurz: STFT) ist eine Fourier-bezogene Transformation, mit der die Frequenzanteile und deren Phasenlage einzelner Zeitabschnitte eines Signals bestimmt werden. In der Praxis besteht das Verfahren zum Berechnen von STFTs darin, ein längeres Zeitsignal in kürzere Segmente gleicher Länge zu unterteilen und dann die Fourier-Transformation für jedes Segment separat zu berechnen. Die erzeugten Einzelspektren werden dann zur Analyse der spektralen Zusammensetzung über die Zeit in einem sog. __Spektrogramm__ aneinandergefügt.
# 
# Dieses Notebook soll Ihnen die Theorie hinter der STFT näher bringen und mit Anwendungsbeispielen zeigen, wann diese Analysetechnik genutzt werden kann. 
# 
# ---
# 
# Die Gliederung des Notebooks ist wie folgt aufgebaut:
# - In *Abschnitt 1* werden einige Limitationen einer normalen Fouriertransformation bei instationären Signalen gezeigt.
# - In *Abschnitt 2* wird die Fensterung und dadurch Segmentierung von instationären Signalen durchgeführt und dessen Frequenzänge berechnet.
# - In *Abschnitt 3* werden diese einzelnen Frequenzgänge grafisch zusammengefügt und somit das besagte Spektrogram erzeugt.
# - Im letzten *Abschnitt 4* wird die STFT auf verschiedene Audio-Beispiele angewendet.
# 
# 
# ## Inhalt  
# <table style="width:256px; border: 1px solid black; display: inline-block">
#     <tr>
#         <td  style="text-align:right" width=64px><img src="img/1-1.png" style="float:left"></td>
#         <td style="text-align:left" width=256px>
#             <a style="color:black; font-size:12px; font-weight:bold; text-decoration:none" href='#1'>
#                 1. Nichtstationäre Signale
#             </a>
#         </td>
#     </tr>  
#     <tr>
#         <td style="text-align:right"><img src="img/1-2_2.jpg" style="float:left"></td>
#         <td style="text-align:left" width=128px>
#             <a style="color:black; font-size:12px; font-weight:bold; text-decoration:none" href='#2'>
#                 2. Fensterung
#             </a>
#         </td>
#     </tr>
#     <tr>
#         <td style="text-align:right"><img src="img/1-3.jpg" style="float:left"></td>
#         <td style="text-align:left" width=128px>
#             <a style="color:black; font-size:12px; font-weight:bold; text-decoration:none" href='#3'>
#                 3. Kurzzeitspektrum
#             </a>
#         </td>
#     </tr>
#     <tr>
#         <td style="text-align:right"><img src="img/1-4.jpg" style="float:left"></td>
#         <td style="text-align:left" width=128px>
#             <a style="color:black; font-size:12px; font-weight:bold; text-decoration:none" href='#4'>
#                 4. Anwendungsbeispiele
#             </a>
#         </td>
#     </tr>
# </table>
# 
# ---

# <a id='1'></a>
# <div>
#     <img src="img/1-1.png" style="float:left">
#     <h2 style="position: relative; top: 6px; left: 6px">
#         1. Nichtstationäre Signale 
#     </h2>
# </div>
# <br>
# <br>
# Signale, die sich mit der Zeit ändern, werden als nichtstationäre Signale bezeichnet.
# 
# Die Fourier-Transformation ist v.a. für stationäre Signale geeignet ist, deren spektrale Zusammensetzung (Frequenz und Phasenlage) sich zeitlich nicht ändert. In der Praxis sind die Signale jedoch häufig nichtstationäre Signale, wodurch diese Bedingung nicht mehr erfüllt ist. Wenn das Spektrum über eine einzige Fourier-Transformation bestimmt wird, gehen nicht nur spektrale Charakteristika verloren, sondern u.U. auch ihre zeitliche Zuordnung (d.h. _wann_ die Frequenzkomponente im Zeitsignal auftritt). Daher müssen bei nicht stationären Signalen die lokalen Eigenschaften berücksichtigt werden. Das nichtperiodische Signal wird deswegen in zeitlich stationär angenommene Signalabschnitte unterteilt.
# 
# ---
# Als Beispiel sollen zunächst einige Zeitsignale erzeugt und deren Frequenzgänge analysiert werden. Importieren Sie dafür zunächst alle für dieses Notebook notwendigen Module und installieren Sie gegebenfalls fehlende Module via `pip install ...`

# In[ ]:


'''
Import externer Module
'''

import [..] # Installieren Sie numpy als np
import cmath

from   [..] # Importieren Sie fftpack und signal aus scipy in den globalen Namensraum
from   [..] # Importieren Sie wavfile aus scipy.io in den globalen Namensraum

import [..] # Importieren Sie matplotlib.pyplot als plt
from   [..] # Importieren Sie cm aus matplotlib in den globalen Namensraum

from mpl_toolkits.mplot3d import axes3d

import librosa
import librosa.display



import IPython.display as ipd
from ipywidgets import interact, FloatSlider


# Falls verhindert werden soll, dass große Cell-Outputs (Plots, Interaktive Grafiken etc.) mit einem Scrollbar versehen werden, kann diese Zeile ausgeführt werden:

# In[ ]:


get_ipython().run_cell_magic('javascript', '', 'IPython.OutputArea.prototype._should_scroll = function(lines) {\n    return false;\n}\n')


# In diesem Notebook soll zudem das Konzept des [Dictionary](https://realpython.com/python-dicts/) zur übersichtlichen Speicherung von Daten eingeführt werden. Ein Dictionary wird (vergleichbar mit Listen und Tupeln) mit geschweiften Klammern `{ ... }` erzeugt. Ein Dictionary speichert alle möglichen Datentypen, die man mit einem Schlüsselwort wieder aus diesem aufrufen kann. Die Syntax ist dabei wie folgt: <br>
# { Key_1: Value_1,<br>
#   Key_2: Value_2,<br>
#   ... }<br><br>
# Der Schlüssel muss dabei ein String (also `".."` oder `'..'`) sein.
#  
# 
# Als Beispiel sollen alle Informationen einer Audiodatei gespeichert werden. Diese kann beinhalten:
# - Strings: Speicherort, Titel, Autor*in
# - Zahlen (float, int,..): Dauer, Abtastfrequenz
# - Listen bzw. Arrays... (auch Numpy-Array): Audiospur(en)
# - ...
# 
# Speichern Sie im Folgenden nun Ihr (vorgegebenes) Lieblingslied in ein Dictionary:
# 

# In[ ]:


'''
Erzeugen und Speichern von Dictionaries
'''

author = "Wolfgang Petry"              # Speichern Sie 'author' unter dem Schlüssel 'Autor_in' in dict_hit_no1
title = 'Wahnsinn'                     # Speichern Sie 'title' unter dem Schlüssel 'Titel' in dict_hit_no1
duration_s = 319.25                    # Speichern Sie 'duration_s' unter dem Schlüssel 'Spieldauer' in dict_hit_no1
fs_Hz = 44100                          # Speichern Sie 'fs_Hz' unter dem Schlüssel 'Abtastfreq links' in dict_hit_no1
track_left = [1, 0.458,0.23,-1]        # Speichern Sie 'track_left' unter dem Schlüssel 'Spur links' in dict_hit_no1
track_right = [1,0.5,0.02,1] # Speichern Sie 'track_right' unter dem Schlüssel 'Spur rechts' in dict_hit_no1

dict_hit_no1 = { ... } # ToDo: erstellen sie das Dictionary


# In[ ]:


print("Einträge im Dictionary: {}".format(len(dict_hit_no1)))


# Um wieder an die in dem Dictionary gespeicherten Daten zu kommen, kann man diese auf zwei Weisen mit dem Schlüssel-bzw. Key-String aufrufen: <br>
# `dict_hit_no1['key_string']` oder `dict_hit_no1.get('key_string')`
# 
# Testen Sie beide Verfahren nun aus:

# In[ ]:


'''
Laden von Daten aus Dictionaries
'''

[..]


# Um nun das angefangene Dictionary zu erweitern, kann dies mit dem Befehl `dict_XY.update(...)` erfolgen. Dabei kann man auch ein anderes Dictionary mit einfügen. Wenn sie einen Schlüssel nutzen, den es schon im Dictionary gab, werden die Daten überschrieben (nutzen Sie dies zur Aktualisierung der Daten).
# 
# Aktualisieren Sie nun das Dictionary Ihres Lieblingsliedes mit einem Genre und einer besseren Audiospur:

# In[ ]:


'''
Erweiterung und Aktualisierung von Dictionaries
'''

genre = "1a Kuschelrock"                       # Speichern Sie 'genre' unter dem Schlüssel 'Genre' in dict_hit_no1
track_left_np = np.array([1, 0.458,0.23,-1])   # Überschreiben Sie 'Spur links' in dict_hit_no1
track_right_np = np.array([1,0.5,0.02,1])      # Überschreiben Sie 'Spur rechts' in dict_hit_no1
dict_better_version = {'Spur links': track_left_np, 'Spur rechts': track_right_np}

# ToDo: Speichern Sie 'Genre' ins Dictionary
[..]

# ToDo: Updaten Sie das Unterdictionary 'dict_better_version' in 'dict_hit_no1'
[..]


# In[ ]:


print("Einträge im Dictionary: {}".format(len(dict_hit_no1)))


# Dictionaries können genutzt werden, um den Code übersichtlicher zu gestalten. Im Folgenden sollen jetzt mehrere instationäre Testsignale erzeugt werden, welche aus verschiedenen Sinusschwingungen zusammengesetzt sind. 

# In[ ]:


'''
Erzeugen von nichtstationären Signalen
'''


# Initialisierung der Variablen
fs_Hz = 200        # Abtastfrequenz
T_s = 6            # Zeitdauer
L_periods = 10     # Länge des Signals in Perioden

# Vier Sinus-Signale
f1_Hz = 9;
f2_Hz = 10;
f3_Hz = 15;
f4_Hz = 20;

# Vier Zeit-Segmente
t1_s = np.arange(0, 1/f1_Hz*L_periods, 1/fs_Hz);
t2_s = np.arange([..]);
t3_s = np.arange([..]);
t4_s = np.arange([..]);

# Vier Sinus-Segmente
seg1 = 2*np.sin([..]) 
seg2 = 5*np.sin([..]) 
seg3 = 7*np.sin([..]) 
seg4 = 4*np.sin([..]) 


# Drei verschiedene Signale mit unterschiedlichen Segmentzusammensetzungen
s1 = np.array([seg1, seg2, seg3, seg4]).flatten()
s2 = np.array([seg3, seg4, seg2, seg1]).flatten()
s3 = np.array([seg2, seg1, seg4, seg3]).flatten()
t_s = [..]  # ToDo: Erzeugen Sie ein Array mit den zugehörigen Zeitschritten 


# Initialisierung und füllen des Dictionaries:
dict_s = [..]  # Speichern Sie die Signale 's1', 's2' und 's3' mit Ihren Namen als Schlüssel in das 'dict_s'


# Vorbereitung der Fouriertransformation
signalLength = len(s1);
print("Länge des Signals: {}".format(signalLength))
Nfft = int(2**(np.floor(np.log(signalLength)/np.log(2))+1)) # Länge der Fft
print("Länge der FFT: {}".format(Nfft))
f_Hz = np.arange(0,fs_Hz,fs_Hz/Nfft)   # Frequenzachse


dictIndex = 0;
for s in (s1,s2,s3):
    dictIndex += 1
    
    # Transformation in den Frequenzbereich:
    S = [..]      # ToDo: führen Sie eine FFT der Länge N mit dem Signal S durch. Nutzen Sie zB: fftpack.fft()
    dict_s.update({'S{}'.format(dictIndex) : S})
    
    # Graphische Darstellung
    plt.subplot(131)
    plt.title('Signal %d' %dictIndex)
    plt.xlabel('Zeit [s]') 
    plt.ylabel('s(t)') 
    plt.plot(t_s, s)
    plt.subplot(132)
    plt.title('Frequenzgang des Signals %d' %dictIndex)
    plt.xlabel('Frequenz [Hz]') 
    plt.xlim(0, 40)
    plt.ylabel('|S(f)|') 
    Sabs = np.abs(S)
    plt.plot(f_Hz, Sabs)
    line1, = plt.plot([f1_Hz,f1_Hz],[0,max(Sabs)],'-r',label='f=' + str(f1_Hz) + 'Hz')
    line2, = plt.plot([f2_Hz,f2_Hz],[0,max(Sabs)],'-g',label='f=' + str(f2_Hz) + 'Hz')
    line3, = plt.plot([f3_Hz,f3_Hz],[0,max(Sabs)],'-b',label='f=' + str(f3_Hz) + 'Hz')
    line4, = plt.plot([f4_Hz,f4_Hz],[0,max(Sabs)],'-m',label='f=' + str(f4_Hz) + 'Hz')
    plt.gcf().set_size_inches(20, 5)
    plt.legend(handles=[line1,line2,line3,line4])
    plt.subplot(133)
    plt.title('Phasengang des Signals %d' %dictIndex)
    plt.xlabel('Frequenz [Hz]') 
    plt.xlim(0, fs_Hz/5)
    plt.ylabel('$\phi$(f) [rad]') 
    SPhase = np.angle(S)
    plt.plot(f_Hz, SPhase)
    plt.show()


# Die absoluten Frequenzgänge $|S(f)|$ sind nahezu identisch und enthalten keine erkennbare Information mehr darüber, in welchem Segment welche harmonische Schwingung lag, während man die jeweiligen Amplitudenhöhen immer ungenauer werden, je kleiner die Signalabschnitte werden (durch die Wahl von $L_{periods}$).
# 
# Um alle Ergebnisse besser zu inspizieren, werden nun alle Ergebnisse über die `interact`- Funktion interaktiv dargestellt:

# In[ ]:


'''
Interaktive Grafik
'''
@interact( domain =[('1. Zeitsignal', 's{}'), ('2. Frequenzsignal', 'S{}')], \
          signal1 = True, signal2 = True, signal3 = True, type= [('Realteil', 1), ('Imaginärteil',2), ('Betrag',3), ('Phase',4)], \
          lower_bound =FloatSlider(min=0,max=Nfft, step=1, continuous_update=False), \
          upper_bound = FloatSlider(min=1,max=Nfft, step=1, continuous_update=False) )
def interactive_signals(domain = 'Zeitsignal', signal1 =True, signal2 = True, signal3 = True, \
                             type = 'abs', lower_bound = 0, upper_bound = Nfft):
    s = []
    col = []
    legend_label = []

    if signal1:
        s.append(dict_s.get(domain.format(1)))
        col.append('y')
        legend_label.append('Segment 1')
    if signal2:
        s.append(dict_s.get(domain.format(2)))
        col.append('g')
        legend_label.append('Segment 2')
    if signal3:
        s.append(dict_s.get(domain.format(3))) 
        col.append('r')
        legend_label.append('Segment 3')
    
    m = []
    for n in s:
        
        if type == 1:
            m.append(n.real)
        elif type == 2:
            m.append(n.imag)
        elif type == 3:
            m.append(abs(n))
        elif type == 4:
            m.append(np.angle(n))   
        s = m
    

    # Grafische Darstellung
    i = 0
    for n in s:
        
        plt.plot(n, color = col[i], label=legend_label[i])
        plt.xlim(lower_bound, upper_bound)
        i+=1
    plt.legend()
    plt.gcf().set_size_inches(20, 5)
    plt.show()
    


# ---
# 
# <a id='2'></a>
# <div>
#     <img src="img/1-2_2.jpg" style="float:left">
#     <h2 style="position: relative; top: 6px; left: 6px">
#         2. Fensterung  
#     </h2>
# </div>
# <br>
# <br>
# Im folgenden Abschnitt soll die Fensterung näher betrachtet werden, mit der das nichtstationäre Signal in quasi-stationäre Signalabschnitte segmentiert wird.
# 
# Ein bloßes Ausschneiden des Signals würde nicht nur potentiell Sprünge im periodisch forgesetzten Zeitsignal erzeugen, was bereits in Notebook 2.2 thematisiert wurde, sondern ist auch gleichbedeutend mit einer Rechteckfensterung. Anders formuliert ist das einfache Ausschneiden eines Signalabschnittes gleichbedeutend mit der Multiplikation mit einem Rechteckfenster im Zeitbereich, welches einer Faltung mit einer Spaltfunktion im Frequenzbereich und dadurch ein Verwischen der Spektrallinien zur Folge hat. Deshalb ist es wichtig, eine geeignetere Fensterfunktion $h(t)$ zu wählen (z.B. ein von-Hann-Fenster). Die Fensterlänge $T$ wird entsprechend der Länge des quasi-periodischen Signalsegments gewählt.
# Ein weiterer Parameter ist der Grad der Überlappung aufeinanderfolgender Signalabschnitte (siehe Vorlesung Thema4, Folie 15 ff.).
# 
# ---
# Nutzen Sie die vorgegebene Funktion ``live_plot()``, um sich einen Durchlauf der Segmentierung, Fensterung und Fouriertransformation auf das Signal `s1` anschauen zu können. Durch den Aufruf von `ipd.clear_output()` wird der vorherige Plot gelöscht, auf dessen Stelle ein neuer Plot eingefügt wird.
# (Anmerkung: für richtige Animationen von Plots bietet sich auch die [animation](https://matplotlib.org/api/animation_api.html) API von Matplotlib an. Da dies aber nicht der Inhalt dieses Notebooks ist, soll die Animation simpel gehalten werden). 
# Die Funktionsargumente sind
# - die Zeitachse `t_s` 
# - das Audiosignal `audioSignal`
# - die Zeitachse eines gefensterten Signalausschnittes `tSegment_s`
# - der gefensterte Signalausschnitt `winAudioSignalSegment`
# - die Frequenzachse des Spektrums `fSegment_Hz` 
# - das Spektrum selbst `SSegment`
# - der Schritt, an dem sich das Spektrogramm gerade befindet `stepIndex`
# - Limits für die Achsen `xLim_max`& `yLim_max`
# 

# In[ ]:


'''
Funktion definieren: Dynamische Darstellung
'''

def live_plot(t_s, audioSignal, tSegment_s, winAudioSignalSegment, fSegment_Hz, SSegment,\
              stepIndex, xLim_max= 50, yLim_max= 80):

    plt.ion()
    ipd.clear_output(wait=True)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    
    ax1.set_title('Fensterung des Signals')
    ax1.set_xlabel('Zeit [s]') 
    ax1.set_ylabel('s(t)') 
    ax1.plot(t_s, audioSignal)
    ax1.plot(tSegment_s, winAudioSignalSegment)

    ax2.set_title('Frequenzgang des gefensterten Signalsegments %d' %stepIndex)
    ax2.set_xlabel('Frequenz [Hz]') 
    ax2.set_ylabel('|S(f)|') 
    ax2.plot(fSegment_Hz, SSegment)
    plt.xlim(0, xLim_max)
    plt.ylim(0, yLim_max)    
    
    fig.set_size_inches(20, 5)  
    plt.show()


# 1. Normalisieren Sie zunächst das Signal `s1`, dass dessen Maximalwert den Wert 1 beträgt.
# 2. Erzeugen Sie ein [Tukey-Fenster](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html) mit einem alpha-Parameter von 0.7, dessen Fensterlänge `T_samples` $2^x$ Samples beträgt (z.B. $x=7$ für 128 samples). Dies soll auch die Länge der FFT sein.
# 3. Stellen Sie eine Überlappung des Zeitfensters `overlap_samples` auf die Hälfte oder zwei Drittel der Fensterlänge `Twin_samples` ein. Die Überlappung und der Vorschub zweier Fenster sind voneiander abhängig: Anzahl an Segmenten = (Fensterlänge - Overlap)/Vorschub (Vorschub ist hier als `slide_samples` bezeichnet).
# 4. Erzeugen Sie eine for-Schleife, in welcher jedes Segment gefenstert und Fourier-transformiert wird. Achten Sie dabei darauf, dass die Schleife bei Erreichen des Signalendes korrekt beendet wird und nicht auf Indices außerhalb des Arrays zugegriffen wird. Berechnen Sie daher vorher die Anzahl an möglichen Segmenten (`numSegments`).
# 5. Fügen Sie zum Schluss die Funktion `live_plot` in die for-Schleife ein und übergeben Sie diesem die benötigten Parameter und Werte.

# In[ ]:


'''
Dynamische Fensterung des Signals 's1'
'''

get_ipython().run_line_magic('matplotlib', 'inline')

# Signal s1 normalisieren
s = [..]         # ToDo: Signal 's1' aus dict_s normalisieren
T_samples = [..] # ToDo: Anzahl an Abtastpunkten
T_s = [..]       # ToDo: Zeitdauer des Gesamtsignals
t_s = np.arange(0, T_s, 1/fs_Hz)


# Erzeugung des Fensters
Nfft = 2**7;                       # FFT Länge
Twin_samples = Nfft                # Fensterlänge in samples
overlap_samples = Twin_samples//4  # Überlappung zwischen zwei Segmenten
slide_sample = [..]                # ToDo: Legen Sie den Vorschub des Fensters (abhängig von "Twin Samples" und "overlap_samples") fest
window = [..]                      # ToDo: Erzeugen Sie das Tukey-Fenster mit 'signal.get_window()'
f_Hz = np.arange(0, fs_Hz, fs_Hz/Nfft)


# Erzeugung des Segments, Fouriertransformation dessen und graphische Anzeige
numSegments = (T_samples - overlap_samples)//slide_sample

# Überprüfung der Parameter:
print("Länge des Signals: {} samples".format(T_samples))
print("Fenster/FFT Länge: {} samples".format(Twin_samples))
print("Vorschub: {} samples".format(overlap_samples))
print("Anzahl an Segmenten: {}".format(numSegments))


for seqIndex in range(numSegments):
    tSegment_s = t_s[seqIndex*slide_sample: seqIndex*slide_sample + Twin_samples]
    sSegment = s[seqIndex*slide_sample: seqIndex*slide_sample + Twin_samples]
    winsSegment = sSegment * window
    winS = np.abs(fftpack.fft(winsSegment, Nfft))       
    
    # Graphische Darstellung
    [..]      # ToDo: Fügen Sie die Funktion 'live_plot()' ein (xLim_max=50, yLim_max=90)


# Die Wahl der Fensterfunktion $h(t)$ und der Zeitfensterlänge `Twin_samples` muss problemspezifisch erfolgen. Im Allgemeinen kann ein kurzes Zeitfenster eine höhere Auflösung des zeitlichen Zustands und ein langes Fenster eine höhere Auflösung im Frequenzbereich bieten. Zwischen beidem muss der beste Kompromiss gesucht werden.
# 
# ---

# <a id='3'></a>
# <div>
#     <img src="img/1-3.jpg" style="float:left">
#     <h2 style="position: relative; top: 6px; left: 6px">
#         3. Kurzzeitspektrum  
#     </h2>
# </div>
# 
# <br>
# <br>
# Setzt man den Signalabschnitt als zu transformierende Funktion in das Fourier-Integral ein, erhält man die Hintransformationsgleichung der STFT wie folgt:
# \begin{equation}
# X(\omega, t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)e^{-j\omega \tau}d\tau 
# \end{equation} 
# Das dabei entstehende Spektrum hat außer der Kreisfrequenz $\omega$ nun auch noch den Analysezeitpunkt $t$ als Variable. Da gewöhnlich voraussetzt wird, dass die Zeitfensterlänge $T$ endlich ist, können die Integrationsgrenzen entsprechend eingeengt werden.  
# 
# Zur Berechnung der STFT können direkt Funktionen aus installierten Bibliotheken genutzt werden. Hier sollen die Funktionen [signal.stft()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.stft.html) und [librosa.stft()](https://librosa.org/doc/0.8.0/generated/librosa.stft.html) genutzt werden.

# In[ ]:


'''
Spektrogramm mit scipy.signal.stft()
'''
for i in range(1,4):
    f, t, Zxx = signal.stft(dict_s.get('s{}'.format(i)), fs=fs_Hz, window=('tukey', 0.7),nperseg=200)  # Frequenzgänge
    dict_s.update({'s{}_scipy_stft'.format(i): (f, t, Zxx)})
    
    # Grafische Darstellung:
    plt.subplot(1,3,i)
    plt.pcolormesh(t, f, np.abs(Zxx), shading = 'auto')
    plt.title('STFT Magnitude des Signals %d' %i)
    plt.xlabel('Zeit [s]') 
    plt.ylabel('Frequenz [Hz]')   
    plt.ylim(0, 50)
    plt.colorbar()


plt.gcf().set_size_inches(20, 5)
plt.show()


# Durch die Darstellung der Signale im Spektrogramm wird nun aus dem Amplitudenfrequenzgang deutlich klarer, welche Frequenzelemente sich in welchen Zeitabschnitten befinden. Über die Fensterlänge `nperseq` lässt sich die Frequenzauflösung auf Kosten der Zeitauflösung verbessern. Wird `nperseq` klein genug gewählt (z.B. = 50), wird sogar sogar die Periodizität des Zeitsignals sichtbar. Die Frequenzauflösung ist in diesem Falle dann aber sehr grob.
# 
# Alternativ kann das Spektrogramm mit den Funktionen [signal.spectrogram()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.spectrogram.html) oder [librosa.display.specshow()](https://librosa.org/doc/main/generated/librosa.display.specshow.html) berechnet werden. Beide Funktionen sollten identische Ergebnisse liefern, lediglich standard colormap ist unterschiedlich.

# In[ ]:


'''
Spektrogramm mit librosa.stft()
'''

windowLength = 200;
for i in range(1,4):
    S = np.abs(librosa.stft(dict_s.get("s{}".format(i)), n_fft=windowLength, \
                            win_length=windowLength, window=('tukey', 0.7))) 

    # (Optional) in dB konvertieren:
    # S_dB = librosa.amplitude_to_db(S)     
    
    # Graphische Darstellung
    plt.subplot(1,3,i)
    librosa.display.specshow(S, sr=fs_Hz, x_axis='s', y_axis='hz')
    plt.title('Spektrogramm des Signals %d' %i)
    plt.xlabel('Zeit [s]') 
    plt.ylabel('Frequenz [Hz]')  
    plt.ylim(0, 50)
    plt.colorbar()
    
plt.gcf().set_size_inches(20, 5)
plt.show()


# Das Spektrogramm kann auch dreidimensional geplottet werden:

# In[ ]:


# 3D-Visualisierung

fig = plt.figure()

for plotIndex in range(1,4):
    f_Hz, t_s, magnitude = dict_s.get('s{}_scipy_stft'.format(plotIndex)) # STFT 
    fLimits_Hz = (f>0) & (f<50) # Frequenzgrenze
    f_Hz = f[fLimits_Hz]        # Frequenzbereich
    magnitude = magnitude[fLimit]
    
    # Graphische Darstellung
    ax = fig.add_subplot(1,3,plotIndex, projection='3d')
    ax.set_title('3D-Visualisierung des Signals %d' %plotIndex)
    ax.set_xlabel('Zeit [s]') 
    ax.set_ylabel('Frequenz [Hz]')  
    ax.set_zlabel('Amplitude')  
    ax.plot_surface(t[None, :], f_Hz[:, None], abs(magnitude), cmap=cm.cool)
    
plt.gcf().set_size_inches(15, 5)
plt.show()


# ---
# <a id='4'></a>
# <div>
#     <img src="img/1-4.jpg" style="float:left">
#     <h2 style="position: relative; top: 6px; left: 6px">
#         4. Anwendungsbeispiele  
#     </h2>
# </div>
# <br><br>
# Für die STFT gibt es viele Anwendungsmöglichkeiten, wie zum Beispiel für die Analyse von Sprache. In diesem Abschnitt soll die STFT zur Analyse von Musiksignalen verwenden. Dazu soll zunächst eine Funktion definiert werden, mit der Informationen aus einer .wav-Datei importiert und als Dictionary abgespeichert werden können.
# 
# Ergänzen Sie die Leerstellen [..] :

# In[ ]:


'''
Funktion definieren: wav-Datei laden
'''

def wav_data(name, file):
    
    fs_Hz, s = wavfile.read( [..] )                 # Abtrastfrequenz, Signal
    if len(np.shape(s))>1:
        s = s[:,0]                                  # Linken Kanal speichern 
    s = s/np.max(np.abs(s))                         # Signal normalisieren 
    L = [..]                                        # Signal-Länge
    N = int(2**(np.floor(np.log2(L))+1))            # FFT-Länge
    T_s = [..]                                      # Zeitdauer
    t_s = np.linspace( [..] )                       # Zeitbereich
    f_Hz = [..]                                     # Frequenzbereich
    
    # alle benötige Daten in Dictionary speichern
    data = {'name': [..] , 'signal': [..] , 'fs_Hz': [..] , 'signalLength': [..] , 'fftLength': [..] , 't_s': [..] , 'f_Hz': [..] }
                                                    
    return [..]


# - __Beispiel 1: missing fundamental / Die fehlende Grundfrequenz__
# 
#     Unsere Wahrnehmung von Akustik wird nicht nur von den einzelnen Frequenzkoponenten innerhalb eines Tons bestimmt, sondern u.a. auch von den Abständen der Obertöne/Harmonischen zueinandner. Dies führt zu einem interessanten Phänomen des sog. "Residualtons" (im Englischen etwas treffender "missing fundamental"), bei dem zwei Töne, von denen einer keine (oder nur eine sehr gering ausgeprägte) Grundfrequenz aufweist, trotzdem sehr ähnlich klingend wahrgenommen werden.
#     
#     Laden sie dazu die beiden Audiodateien ``toneF.wav`` und ``toneF_noFund.wav`` ein, anhand dieser Effekt demonstriert werden soll.

# In[ ]:


'''
toneF.wav laden und abspielen
'''

file = 'data/toneF.wav'
# Laden von toneF mit dem Namen 'Ton F'
toneF = [..] # ToDo: Nutzen Sie die Funktion 'wav_data', um die .wav in das Projekt zu laden 
# Akustische Ausgabe
ipd.Audio(file)                   


# In[ ]:


'''
toneF_noFund.wav laden und abspielen
'''

file = 'data/toneF_noFund.wav'
# Laden von toneF_noFund mit dem Namen 'Ton F ohne Fundament'
toneF_noFund =  # ToDo: Nutzen Sie die Funktion 'wav_data', um die .wav in das Projekt zu laden
# Akustische Ausgabe
[..] # ToDo


# Beide Töne sollten relativ ähnlich klingen, vor allem von der wahrgenommenen Tonhöhe. Ein Blick auf das Spektrogramm verrät aber, dass im zweiten Falle die Grundfrequenz fehlt. Erstellen Sie dazu das Spektrogramm beider Audiosignale mit librosa. Skalieren Sie die Frequenzachse logarithmisch ([librosa.amplitude_to_db()](http://man.hubwiz.com/docset/LibROSA.docset/Contents/Resources/Documents/generated/librosa.core.amplitude_to_db.html)) Um die Frequenzkomponenten klarer darzustellen.

# In[ ]:


'''
toneF und toneF_NoFund über Spektrogramm darstellen
'''

i = 0
for tone in (toneF, toneF_noFund):

    S = [..]    # ToDo: Wenden Sie die Funktion 'librosa.stft()' auf das Signal 'tone['signal']' an
    S_dB = librosa.amplitude_to_db(S)     # in dB konvertieren
    
    # Graphische Darstellung
    i += 1
    plt.subplot(1, 2, i)
    librosa.display.specshow(S_dB, sr=tone['fs_Hz'], x_axis='s', y_axis='hz', cmap=cm.gist_heat)
    plt.title('Spektrogramm von %s' %tone['name'])
    plt.xlabel('Zeit [s]') 
    plt.xlim(0, 0.5)
    plt.ylabel('Frequenz [Hz]')  
    plt.ylim(0, 1500)
    plt.colorbar()

plt.gcf().set_size_inches(20, 5)
plt.show()


# - __Beispiel 2: Melodie aus verschiedenen Instrumenten__
# 
#     Als ein weiteres Beispiel für die Nützlichkeit von Spektrogrammen sollen die beiden Audiodateien `melodie_klavier.wav`, `melodie_geige.wav` sowie `melodie_stimme.wav` untersucht werden. Laden Sie diese ein. Die Signale stellen dieselbe Melodie dar, aber mit unterschiedlichen Instrumenten bzw. gesungen (Vocoder).

# In[ ]:


'''
melodie_klavier.wav laden und abspielen
'''

file = 'data/melodie_klavier.wav'
melodyPiano = wav_data('Klaviermelodie', file)
ipd.Audio(file)                       


# In[ ]:


'''
melodie_geige.wav laden und abspielen
'''

file = 'data/melodie_geige.wav'
melodyViolin = wav_data('Geigemelodie', file)
ipd.Audio(file)                       


# In[ ]:


'''
melodie_stimme.wav laden und abspielen
'''

file = 'data/melodie_stimme.wav'
melodyVoice = wav_data('Stimme', file)
ipd.Audio(file)                       


# Stellen Sie nur das Spektrogramm zur Analyse der drei Signale dar. Varrieren Sie FFT Länge, Fenstertyp und Überlappung (Achtung, der Grad der Überlappung wird in Anzahl an Abtastwerten abgegeben, nach welchen sich die Fensterung wiederholt, nicht relativ zur FFT Länge).

# In[ ]:


'''
Kurzzeitspektrum
'''
numSamplesPerSegment = 512
numSamplesOverlap = numSamplesPerSegment/4

plotIndex = 0
for melody in (melodyPiano, melodyViolin, melodyVoice):
    
    plotIndex += 1 
    f, t, magnitude = [..]  # ToDo: Wenden Sie die Funktion 'signal.stft()' auf das Signal 'melody' an
    
    # Graphische Darstellung
    plt.subplot(3, 1, plotIndex)
    plt.pcolormesh(t_s, f_Hz, np.abs(magnitude), shading = 'auto')
    plt.title('STFT Magnitude der %s' %melody['name'])
    plt.xlabel('Zeit [s]') 
    plt.xlim(0, 8)
    plt.ylabel('Frequenz [Hz]')   
    plt.ylim(0, 3000)
    plt.colorbar()


plt.gcf().set_size_inches(20, 20)
plt.show()


# In[ ]:


'''
Kurzzeitspektrum
'''
numSamplesPerSegment = 512
numSamplesOverlap = numSamplesPerSegment/4

#Lösung
plotIndex = 0
for melody in (melodyPiano, melodyViolin, melodyVoice):
    
    plotIndex += 1 
    f_Hz, t_s, magnitude = signal.stft(melody['signal'], melody['fs_Hz'], window='hann', \
                            nperseg=numSamplesPerSegment, noverlap=numSamplesOverlap) 
    
    # Graphische Darstellung
    plt.subplot(3, 1, plotIndex)
    plt.pcolormesh(t_s, f_Hz, np.abs(magnitude), shading = 'auto')
    plt.title('STFT Magnitude der %s' %melody['name'])
    plt.xlabel('Zeit [s]') 
    plt.xlim(0, 8)
    plt.ylabel('Frequenz [Hz]')   
    plt.ylim(0, 3000)
    plt.colorbar()

plt.gcf().set_size_inches(20, 20)
plt.show()


# Wie im Spektrogramm gut zu sehen ist, sind die Töne der einzelnen Instrumente aus einer Grundfrequenz und mehreren Harmonischen aufgebaut, die immer Vielfache der Grundfrequenz sind. Die höherfrequenten Beiträge dieser "Obertöne" lassen verschiedene Musikinstrumente unterschiedlich klingen.
# 
# - __Beispiel 3: Spektrogramm vs. Musiknoten__
# 
#  Nun analysieren Sie bitte anhand der nun kennengelernten Verfahren das Audiosignal von ``musik.wav``[9]:

# In[ ]:


'''
musik.wav laden und abspielen
'''

file = 'data/musik.wav'
# Laden von musik.wav mit dem Namen 'Musiksignal'
music = # ToDo: Nutzen Sie die Funktion 'wav_data', um die .wav mit dem Namen 'Musikdatei' in das Projekt zu laden. 
# Akustische Ausgabe
[..]                       


# Führen Sie zunächst eine dynamische Fensterung (wie in Abschnitt 2) mit folgenden Eigenschaften durch,
# - Zeitfenstertyp: Blackman,
# - Zeitfensterlänge: $2^{14}$ Samples,
# - Vorschub: 50 \% der Fensterlänge,
# 
# um noch eimal den Prozess der Erstellung des Spektrogramms zu visualisieren (die Fensterlänge von $2^{14} = 16384$ Samples ist relativ groß und wird nur für diese Visualisierung gewählt, damit das Plotten nicht zu lange dauert). Gehen sie dabei wie in Abschnitt 2 vor. Ggf. können Sie die Routine zur Berechnung der Zeitversetzung, Fensterung und Fouriertransformation der Signalabschnitte auch als eigene Funktion kapseln.

# In[ ]:


'''
Aufgabe: Dynamische Fensterung darstellen
'''
get_ipython().run_line_magic('matplotlib', 'inline')

# Signal importieren und normalisieren
audioSignal = [..] # Audiosignal normieren
fs_Hz = [..]
T_samples = [..]
T_s = [..]
t_s = [..]


# Erzeugung des Zeitfensters
Nfft = 2**14;                         # FFT Länge
Twin_samples = Nfft                   # Fensterlänge in samples
overlap_samples = Twin_samples//4     # Überlappung zwischen zwei Segmenten                         
slide_samples = [..]                  # Vorschub eines Abschnittes pro Segment
window = [..]                         # Blackman-Fenster
f_Hz = np.arange(0, fs_Hz, fs_Hz/Nfft)

# Erzeugung des Segments, Fouriertransformation dessen und grafische Anzeige:
numSegments = (T_samples - overlap_samples)//slide_samples

for seqIndex in range(numSegments):
    print("Segment {}".format(seqIndex))
    tSegment_s = [..]
    sSegment = [..]
    # Fenstern
    winsSegment = [..]
    # Fouriertransformation
    winS = [..]

    # Grafische Darstellung:
    [..]      # ToDo: Fügen Sie die Funktion 'live_plot()' ein (xLim_max=fs_Hz/10, yLim_max=0.1)


# Auch hier lohnt die Darstellung des kurzen Musikabschnittes als Spektrogramm. Variieren Sie die Parameter wie Fenstertyp, Überlappung, Fensterlänge usw.

# In[ ]:


'''
Aufgabe: Spektrogramm darstellen
'''

S = [..] # ToDo: Führen Sie eine STFT des Signal music['signal'] mit librosa.stft() durch
S_dB = librosa.amplitude_to_db(S)     
T_samples = np.size(S_dB)

# Einige interessante Frequenzen:
f1_Hz = 700
f2_Hz = 950
f3_Hz = 1050

# Grafische Darstellung:
librosa.display.specshow(S_dB, sr=music['fs_Hz'], x_axis='s', y_axis='hz', cmap=cm.bwr)
freqLine1, = plt.plot([0, T_samples],[f1_Hz, f1_Hz],'-k',label='f1_Hz=' + str(f1_Hz) + 'Hz')
freqLine2, = plt.plot([0, T_samples],[f2_Hz, f2_Hz],'-k',label='f2_Hz=' + str(f2_Hz) + 'Hz')
freqLine3, = plt.plot([0, T_samples],[f3_Hz, f3_Hz],'-k',label='f3_Hz=' + str(f3_Hz) + 'Hz')
plt.title('Spektrogramm des Musiksignals')
plt.xlabel('Zeit [s]') 
plt.ylabel('Frequenz [Hz]')  
plt.ylim(0, 1500)
plt.legend(handles=[freqLine1, freqLine2, freqLine3])
plt.colorbar()

plt.gcf().set_size_inches(20, 5)
plt.show()


# In[ ]:


'''
Aufgabe: Spektrogramm darstellen
'''

# Lösung
S = abs(librosa.stft(music['signal'], win_length = 1024))
S_dB = librosa.amplitude_to_db(S)     
T_samples = np.size(S_dB)
# Einige interessante Frequenzen:
f1_Hz = 700
f2_Hz = 950
f3_Hz = 1050

# Grafische Darstellung:
librosa.display.specshow(S_dB, sr=music['fs_Hz'], x_axis='s', y_axis='hz', cmap=cm.bwr)
freqLine1, = plt.plot([0, T_samples],[f1_Hz, f1_Hz],'-k',label='f1_Hz=' + str(f1_Hz) + 'Hz')
freqLine2, = plt.plot([0, T_samples],[f2_Hz, f2_Hz],'-k',label='f2_Hz=' + str(f2_Hz) + 'Hz')
freqLine3, = plt.plot([0, T_samples],[f3_Hz, f3_Hz],'-k',label='f3_Hz=' + str(f3_Hz) + 'Hz')
plt.title('Spektrogramm des Musiksignals')
plt.xlabel('Zeit [s]') 
plt.ylabel('Frequenz [Hz]')  
plt.ylim(0, 1500)
plt.legend(handles=[freqLine1, freqLine2, freqLine3])
plt.colorbar()

plt.gcf().set_size_inches(20, 5)
plt.show()


# Im Spektrogramm sind z.B. die Frequenzanteile um $700$ Hz, $950$ Hz, $1050$ Hz deutlich zu sehen, die zu den exakten Tonhöhen $ F_{5} = 698.46$ Hz, $ B^b_{5} = 932.33$ Hz und $ C_{6}=1046.50$ Hz korrespondieren. Weitere Beziehungen zwischen Tonhöhen und Frequenzen sind in der Tabelle unter Referenz \[7\] zu finden.
# 
# <img style="float:center; margin:5px 0px 0px 10px" src="img/1-note.png" width="900">
# 
# ---
# 
# <br>
# 
# ### References
# 
# 1. Titelbild von [Ethan Weil](https://de.wikipedia.org/wiki/Kurzzeit-Fourier-Transformation#/media/Datei:Short_time_fourier_transform.PNG)  
# 2. [Short-time Fourier transform](https://en.wikipedia.org/wiki/Short-time_Fourier_transform)  
# 3. Lehrbuch: [Intelligente Signalverarbeitung 1 - Signalanalyse](https://katalog.slub-dresden.de/id/0-1654371521/#detail)  
# 4. Vedio: [The Short Time Fourier Transform | Digital Signal Processing](https://www.youtube.com/watch?v=g1_wcbGUcDY)  
# 5. [The Missing Fundamental](https://pages.mtu.edu/~suits/MissingFund.html)  
# 6. [Music Feature Extraction in Python](https://towardsdatascience.com/extract-features-of-music-75a3f9bc265d)   
# 7. [Frequencies for equal-tempered scale](https://pages.mtu.edu/~suits/notefreqs.html)   
# 8. Referenz von Colormap: [matplotlib.cm](https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html)
# 9. [Wiz Khalifa - See You Again ft. Charlie Puth](https://www.youtube.com/watch?v=RgKAFK5djSk)
# 
# ---
# <div>Notebook erstellt von Arne-Lukas Fietkau, Yifei Li  und <a href="mailto:christoph.wagner@tu-dresden.de?Subject=Frage%20zu%20Jupyter%20Notebook%203.1%20STFT" target="_top">Christoph Wagner</a></div>
# 
