#!/usr/bin/env python
# coding: utf-8

# # 0.2 - Einführung

# <img style="float: right; margin:5px 0px 0px 10px" src="img/Titel.png" width="400">
# Begleitend zur Übung des Fachs Signalverarbeitung wird Ihnen eine Reihe an Jupyter-Notebooks zur Verfügung gestellt. Diese soll Ihnen sowohl zum besseren Verständnis der in der Vorlesung und Übung behandelten Themen helfen, als auch die Fähigkeit zur selbstständigen Lösung eigener Problemstellungen geben.
# 
# Die Bearbeitung der Notebooks ist dabei komplett freiwillig. Falls Sie aber Probleme und Fragen haben, posten Sie Ihre Fragen gerne ins Opal-Forum. 
# 
# 
# Dieses Notebook soll Ihnen beim Einstieg in die Programmiersprache Python helfen. Weitere Notebooks werden zeitnah zur jeweiligen Übung online gestellt.
# 
# 
# ## Inhalt  
# <table style="width:300px; border: 1px solid black; display: inline-block">
#     <tr>
#     <td style="text-align:right"><img src='./img/IMG-graph.png' style="float:left"></td>
#     <td style="text-align:left" width=128px><a style="color:black; font-size:14px; font-weight:bold; text-decoration:none" href='#signalrep'>1. Signalrepräsentation</a>
#         </td>
#     </tr>
#     <tr>
#     <td style="text-align:right"><img src="img/IMG-signal.png" style="float:left"></td>
#     <td style="text-align:left" width= 256px><a style="color:black; font-size:14px; font-weight:bold; text-decoration:none" href='#signalop'>2. Signaloperation</a>
#         </td>
#   </tr>
#     <tr>
#     <td style="text-align:right"><img src="img/IMG-Fourier.png" style="float:left"></td>
#     <td style="text-align:left" width=128px><a style="color:black; font-size:14px; font-weight:bold; text-decoration:none" href='#fourier'>3. Diskrete Fourier-Transformation</a>
#         </td>
#   </tr>
# </table>

# <a id='signalrep'></a><div><img src="img/IMG-graph.png" style="float:left"><h2 style="position: relative; top: 6px; left: 6px"> 1. Signalrepräsentation</h2>

# Zunächst schauen wir uns an, wie man mit Python typische Eingangssignale erzeugt und sich diese graphisch darstellen lassen kann.
# Dafür benötigen wir aus dem Modul `numpy` Funktionen zur Erzeugung von Arrays. Zur Visualisierung verwenden wir aus dem Modul `matplotlib` das Objekt [`pyplot`](https://matplotlib.org/api/pyplot_api.html).
# 
# Die Module und Objekte lassen sich wie folgt importieren:
# 
# ```python
# import numpy as np
# import matplotlib.pyplot as plt
# 
# ```
# 
# Probieren Sie es in der nächsten Zelle gleich mal aus, indem sie die mit [..] gekennzeichneten Zeilen ersetzen!

# In[1]:


# Hier können Sie Python-Code hineinschreiben und mit Shift+Enter ausführen!
# Module importieren (numpy und matplotlib.pyplot)
[..]
[..]


# Erzeugung eines linearen Arrays als Zeitbereich
t = np.linspace(-5, 5, 1001)


# Das Objekt [`np.linspace(a,z,res)`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) erzeugt ein äquidistantes Zahlenarray zwischen der unteren Schranke ```a``` und der oberen Schranke ```z``` mit der Auflösung von ```res```. Den Inhalt von Variablen lässt sich anzeigen, indem man das ```print()```-Kommando verwendet oder die Variable alleine ans Ende der Zelle in eine Zeile schreibt.
# 
# Lassen Sie sich also nun in der folgenden Zelle das Array ausgeben! (Da die Auflösung sehr groß gesetzt ist, ist auch das Array dementsprechend groß und wird nicht vollständig angezeigt. Deshalb kann man sich auch nur einen Ausschnitt des Arrays mit z.B. ```t[0:9]``` anzeigen lassen.)
# 

# In[ ]:


# Betrachten des Inhalts der Variable 't'.
[..]


# Es lassen sich noch weitere Eigenschaften der Variablen und des Inhalts anzeigen:

# In[ ]:


# Betrachtung der Eigenschaften:
t_length = len(t)
t_type = type(t)
t_entry_type = type(t[0])

# Setzen Sie in der print()-Eingabe anstelle [..] ein.

print("Array-Länge: {};   Arraytyp: {};   Elementtyp: {}".format( [..], [..], [..]))


# <h3> Exponentielle Funktion</h3>
# 
# Zur Erzeugung einer exponentiellen Funktion kann aus dem Modul `numpy` das Objekt [`exp`](https://numpy.org/doc/stable/reference/generated/numpy.exp.html) verwendet werden. Mit dem Objekt `plt` kann dann die exponentielle Funktion geplottet werden.

# In[ ]:


# Erzeugung eines Arrays mit exponentiellen y-Werten für alle Einträge in t.

m = 0.7                          # Wachstumsrate
s = np.exp(m*t)                  # Exponentialfunktion


# Graphische Darstellung
plt.gcf().set_size_inches(8, 5)  # Fenstergröße festlegen
plt.title(u's = exp(0.7*t)')     # Titel einfügen
plt.xlabel(u't  [Zeit]')         # x-Achsenbeschriftung einfügen
plt.ylabel(u's [Amplitude]')     # y-Achsenbeschriftung einfügen
plt.plot(t, s)                   # Festlegen der Variablen x und y
plt.show()                       # Plot zeigen


# Das Objekt ```np.exp()``` kann auch mit komplexen Exponenten verwendet werden.
# 
# Zum aneinanderfügen der Plots wird hier zusätzlich die Funktion [```subplot```](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.subplot.html) verwendet.

# In[ ]:


# komplexe Exponentialkomponente

m = complex(0.7, 7)      # 0.7 = Realteil, 7 = Imaginärteil

# Erzeugung eines Arrays mit exponentiellen y-Werten mit t als x-Werten.

s = [..] # Ergänzen Sie die korrekte Funktion.


# Graphische Darstellung mittels Subplots
plt.subplot(221)
plt.title(u'Realteil')
plt.xlabel(u't  [Zeit]')
plt.ylabel(u's [Re{Amplitude}]')
plt.plot(t,np.real(s))   # Plot des Realteils über np.real()
plt.subplot(222)
plt.title(u'Imaginärteil')
plt.xlabel(u't  [Zeit]')
plt.ylabel(u's [Im{Amplitude}]')
plt.plot(t,np.imag(s))   # Plot des Imaginörteils über np.imag()
plt.subplot(223)
plt.title(u'Absolut')
plt.xlabel(u't  [Zeit]')
plt.ylabel(u's [|Amplitude|]')
plt.plot(t,np.abs(s))    # Plot des Absolutwerts über np.abs()
plt.subplot(224)
plt.title(u'Phase')
plt.xlabel(u't  [Zeit]')
plt.ylabel(u's [Radiant]')
plt.plot(t,np.angle(s))  # Plot der Phase über np.angle()

plt.gcf().set_size_inches(15, 10)
plt.show()


# <h3> Sinus und Cosinus</h3>
# 
# Auch Sinus- und Cosinussignale lassen sich über Objekte aus dem numpy-Modul erzeugen.
# Folgende Objekte stehen dabei zur Verfügung:
# 
# - [`np.pi`](https://numpy.org/doc/stable/reference/constants.html): Wert von π,
# - [`np.sin()`](https://numpy.org/doc/stable/reference/generated/numpy.sin.html): Sinusfunktion,
# - [`np.cos()`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html): Cosinusfunktion.
# 
# 
# Implementieren Sie nun im Folgenden ein Array mit den Werten der Sinusfunktion mit der Kreisfrequenz von π/3 und eine Cosinusfunktion mit der Kreisfrequenz von 2/3 * π im zeitlichen Bereich von -5 bis 5 und einer Auflösung von 1001 Einheiten.

# In[ ]:


# Implementieren Sie ein Sinus- und Cosinussignal mit den vorgegebenen Kreisfrequenzen

t = [..]            # äquidistanter Wertebereich von -5 bis 5 und einer Auflösung von 1001 Einheiten.

s1 = [..]           # Sinus mit Kreisfrequenz π/3
s2 = [..]           # Cosinus mit Kreisfrequenz 2π/3


# Graphische Darstellung mittels Subplots
# w = π/3, Sinus:
plt.subplot(121)
plt.xlabel(u't  [Zeit]')
plt.ylabel(u's1 [Amplitude]')
plt.plot(t, s1)
plt.title(u'sin((π/3)*t)')

# w = 2π/3, Cosinus:
plt.subplot(122)
plt.xlabel(u't  [Zeit]')
plt.ylabel(u's2 [Amplitude]')
plt.plot(t, s2)
plt.title(u'cos((2π/3)*t)')

plt.gcf().set_size_inches(15, 5)
plt.show()


# <h3> Impuls- und Sprungsignale</h3>
# 
# Mit dem Objekt [`np.where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html) können Impulse und Sprünge implementiert werden. Das Objekts ist wie folgt aufgebaut: `np.where(Bedingung, True, False)`.
# Über die `Bedingung` lässt sich zwischen den vorgegebenen Variablen `True` und `False` schalten. Für einen Sprung benötigt man eine Bedingung, zum Beispiel (t >= 0). Für einen Impuls werden zwei Bedingungen benötigt (Beispiel: (t >= 0) & (t <= 1)).
# 
# 
# 
# 
# Implementieren Sie im Folgenden die vorgegebenen Signale im zeitlichen Bereich von -5 bis 5 und einer Auflösung von 1001 Werten.

# In[ ]:


#Impulsbreite = 0.1 um den Nullpunkt, Amplitude = 1, Vorzustand = 0.
s1 = np.where( [..] , 1, 0)

# Impuls mit Breite = 3 mit dem Mittelpunkt bei t = -0.5, Amplitude = 1, Vorzustand = 0.
s2 = [..]

# Sprung bei t >= -2, Amplitude = 1, Vorzustand = -0.2.
s3 = [..]


# Graphische Darstellung mittels Subplots
plt.subplot(221)
plt.title(u'Impulsbreite = 3')
plt.xlabel(u't  [Zeit]')
plt.ylabel(u's1 [Amplitude]')
plt.plot(t, s1)

plt.subplot(222)
plt.title(u'Impulsbreite = 0.1')
plt.xlabel(u't  [Zeit]')
plt.ylabel(u's2 [Amplitude]')
plt.plot(t, s2)

plt.subplot(223)
plt.title(u'Sprung')
plt.xlabel(u't  [Zeit]')
plt.ylabel(u's3 [Amplitude]')
plt.plot(t, s3)

plt.gcf().set_size_inches(15, 10)
plt.show()


# <h3> Diskrete Signaldarstellung</h3>
# 
# Alle bisherigen Beispiele sind trotz ihres Aussehens zeitdiskret, zwischen deren Punkten eine durchgehende Linie interpoliert wurde. Nur durch die große Anzahl an berechneten Punkten scheinen die Darstellungen zeitkontinuierlich zu sein. Um die zetdiskrete Eigenschaft graphisch besser darzustellen, kann [`plt.stem()`](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.stem.html) anstelle von `plt.plot()` verwendet werden.<br>
# Um ein einfaches inkrementelles Array zu erzeugen, wird [`np.arange()`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html) verwendet.
# 
# `np.arange()` und `plt.stem()` werden im Folgenden auf eine Exponentialfunktion angewendet:<br>
# Anmerkung: Die Option `use_line_collection = True` erzeugt die Graphik effizienter. Mehr Informationen dazu finden Sie in [der Dokumentation](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.stem.html).

# In[ ]:


# Erzeugen von 21 Samples 
n = np.arange(0, 20)


# Erzeugen eines Arrays mit dem exponentiellen Werten 
s = np.exp(-0.3*n)


# Graphische Darstellung
plt.ylim(-0.5, 1.5)          
plt.xlabel(u'n  [Messpunkte]')
plt.ylabel(u's [Amplitude]')
plt.stem(n, s, use_line_collection=True) # Erstellung des Stem plot

plt.gcf().set_size_inches(8, 5)
plt.show()


# Implementieren Sie nun im Folgenden die diskreten Signaldarstellungen für folgende Sinus- und Cosinusfunktionen:
# 
# - s1 = sin(n*π)
# - s2 = sin(n*π/6)
# - s3 = cos(n*π/9)
# - s4 = cos(2n)

# In[ ]:


# Implementieren Sie zwei Sinus- und zwei Cosinussignal mit den vorgegebenen Werten.

n =  [..] # Es sollen insgesamt 51 Samples (0-50) angezeigt werden.


s1 = [..] # sin(n ⋅ π)

s2 = [..] # sin(n ⋅ π/6)

s3 = [..] # cos(n ⋅ π/9)

s4 = [..] # cos(2 ⋅ n)


# Graphische Darstellung
plt.subplot(221)
plt.title(u'sin(nπ)')
plt.xlabel(u'n  [Sample-No.]')
plt.ylabel(u's1 [Amplitude]')
plt.stem(n, s1, use_line_collection=True)

plt.subplot(222)
plt.title(u'sin(nπ/6)')
plt.xlabel(u'n  [Sample-No.]')
plt.ylabel(u's2 [Amplitude]')
plt.stem(n, s2, use_line_collection=True)

plt.subplot(223)
plt.title(u'cos(nπ/9)')
plt.xlabel(u'n  [Sample-No.]')
plt.ylabel(u's3 [Amplitude]')
plt.stem(n, s3, use_line_collection=True)

plt.subplot(224)
plt.title(u'cos(2n)')
plt.xlabel(u'n  [Sample-No.]')
plt.ylabel(u's4 [Amplitude]')
plt.stem(n,s4, use_line_collection=True)

plt.gcf().set_size_inches(15, 10)
plt.show()


# In den Graphen s2 und s3 erkennt man gut den Sinus-/Cosinus-Verlauf. Als Ausgabepunkte für s1 sind die Nulldurchgänge gewählt worden und sollten alle theoretisch den Wert Null haben. Durch Rundungsfehler ist das Ergebnis der Rechnung nur nahe Null. Und in Graph s4 ist die Abtastung nicht synchronisiert, weshalb man die Frequenz nicht ersehen kann.
# 
# Implementieren Sie nun einen Impuls und ein Sprungsignal mit `np.where` und lasssen Sie sich den mit `plt.stem` ausgeben:
# - s1 = Impuls an Position n = -2
# - s2 = Sprung an Position n =-2 von 0 auf 1

# In[ ]:


# Implementieren Sie 

n = [..] # Es sollen insgesamt 21 Samples (-10 bis +10) angezeigt werden.


s1 = [..] # Impuls bei n = -2

s2 = [..] # Sprung bei n = -2 von 0 auf 1

# Graphische Darstellung
plt.subplot(121)
plt.title(u'Impuls')
plt.xlabel(u'n  [Sample-No.]')
plt.ylabel(u's1 [Amplitude]')
plt.stem(n, s1, use_line_collection=True)

plt.subplot(122)
plt.title(u'Sprung')
plt.xlabel(u'n  [Sample-No.]')
plt.ylabel(u's2 [Amplitude]')
plt.stem(n, s2, use_line_collection=True)

plt.gcf().set_size_inches(15, 4)
plt.show()


# <a id='signalop'></a><div><img src="img/IMG-signal.png" style="float:left"><h2 style="position: relative; top: 6px; left: 6px"> 2. Signaloperation</h2></div>
# 
# In Python können Signale leicht über die Grundrechenarten verknüpft werden oder aber auch mit externen Modulen gefaltet werden. Für die Grundrechenarten stehen interne Objekte zur Verfügung, die mit den zugehörigen einfachen Rechner-Zeichen verwendet werden, also  `+`, `-`, `*` & `/`.
# 
# 
# Ein paar Beispiele zur Verwendung der Grundrechenarten sind nun gegeben:

# In[ ]:


# Implementierung der Grundrechenarten

t = np.linspace(-5, 5, 1001)

s1 = np.sin(2*np.pi*t)
s2 = np.exp(-t/2)

s_add =  [..] # Addition von s1 und s2
s_mult = [..] # Multiplikation von s1 mit s2

# Graphische Darstellung
plt.subplot(221)
plt.title(u'Sinusfunktion')
plt.xlabel(u't [Zeit]')
plt.ylabel(u's1 [Amplitude]')
plt.plot(t, s1)

plt.subplot(222)
plt.title(u'Exponentialfunktion')
plt.xlabel(u't [Zeit]')
plt.ylabel(u's2 [Amplitude]')
plt.plot(t, s2)
plt.subplot(223)

plt.title(u'Addition')
plt.plot(t, s_add)
plt.xlabel(u't [Zeit]')
plt.ylabel(u's_add [Amplitude]')
plt.subplot(224)

plt.title(u'Multiplikation')
plt.plot(t, s_mult)
plt.xlabel(u't [Zeit]')
plt.ylabel(u's_mult [Amplitude]')

plt.gcf().set_size_inches(15, 10)
plt.show()


# Eine Faltung von Arrays kann mit Hilfe von `numpy` mit dem Objekt [`convolve()`](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html) durchgeführt werden. Lesen Sie dafür in der verlinkten Doku nach, wie Sie das Faltungs-Objekt nutzen können. Um Signale in einen Bereich zuzuschneiden, kann das schon für die Impulse und Sprünge verwendete Objekt `where` verwendet werden.

# In[ ]:


# Implementierung einer e-Funktion über den Bereich t mit dem Verlauf e_fun von -5 bis +4 und von +4 bis 5 einen Wert von 0.


t = np.linspace(-5, 5, 1001)

s1 = np.where((t >= -2) & (t <= 3), 1, 0) # Rechteckfunktion
e_fun = np.exp(0.7*t)
s2 = [..]   # ToDo: Exponentialfunktion


#Graphische Darstellung
plt.subplot(121)
plt.title(u'Rechteck')
plt.xlabel(u't [Zeit]')
plt.ylabel(u's1 [Amplitude]')
plt.plot(t, s1)

plt.subplot(122)
plt.title(u'Exponentialfunktion')
plt.xlabel(u't [Zeit]')
plt.ylabel(u's2 [Amplitude]')
plt.plot(t, s2)

plt.gcf().set_size_inches(10, 5)
plt.show()


# In[ ]:


# Implementierung des Operators convolve aus der Bibliothek numpy

s_conv = [..]
t_conv = np.linspace(-10, 10, len(s_conv))

# Graphische Darstellung
plt.title(u'Faltung')
plt.xlabel(u't [Zeit]')
plt.ylabel(u's1*s2 [Amplitude]')
plt.plot(t_conv, s_conv)
plt.show()


# <a id='fourier'></a><div><img src="img/IMG-Fourier.png" style="float:left"><h2 style="position: relative; top: 6px; left: 6px">  3. Diskrete Fourier-Transformation</h2>

# ![signal](img/signal.gif) 

# Hinweis: Die Beziehungen zwischen FS, FT, DTFT, DFT bzw. diskret vs. kontinuierlich und periodisch vs. nicht periodisch schauen Sie sich bitte die entsprechenden Folien in der Vorlesung an.  

# ![FS](img/fourier.gif) 

# In diesem Beispiel zur Fouriertransformation soll eine sinc-Funktion Fourier-transformiert und invers rücktransformiert werden. Dabei entsteht ideal im Frequenzbereich eine Rechteckfunktion. Da wir uns durch die Nutzung von Zahlenarrays im Zeit- und Wertdiskreten bewegen, ist die Fouriertransformation diskret. Die wichtigen Formeln sind 
# 
# 
# (1) Diskrete Fouriertransformation (DFT):
# \begin{equation*}
# H(n)=\frac{1}{N}\sum_{k=0}^{N-1}h(k)e^{-j2\pi n\frac{k}{N}},
# \end{equation*}  
# 
# (2) Inverse DFT (IDFT):
# \begin{equation*}
# h(k)=\sum_{n=0}^{N-1}H(n)e^{j2\pi k\frac{n}{N}},
# \end{equation*}  
# 
# (3) sinc-Funktion:
# \begin{equation*}
# sinc\left(\frac{x}{T}\right) = \frac{\sin(\frac{\pi x }{T})}{\frac{\pi x}{T}},
# \end{equation*}  
# 
# (4) Rechteckfunktion:
# \begin{equation*} 
# rect \left( \frac{x}{\tau} \right) = \begin{cases}
#     A     & \text{ if } |x| \leq \frac{\tau}{2} \\
#     0  & \text{ else }  \\
# \end{cases},
# \end{equation*}
# 
# (5) Beziehungen bei Fourier zwischen $\tau$ und T:
# \begin{equation*} 
# \tau = \frac{1}{T }.
# \end{equation*}
# 
# Zur Umsetzung der Transformationen wird die Fast-Fourier-Transformation durch die Objekte [fft.fft](https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.fft.html) und [fft.ifft](https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.ifft.html) aus dem Modul scipy verwendet. Die Verwendung der FFT beschleunigt die Berechnungszeit der Fouriertransformation, soll aber hier nicht weiter vertieft werden. Im Modul 1.1 wird näher die Umsetzung der Diskreten Fouriertransformation beschrieben.
# 
# Importieren Sie zunächst die Objekte fft und ifft aus der Bibliothek scipy.fftpack

# In[ ]:


# Import der Objekte fft und ifft aus der Bibliothek scipy.fftpack in den globalen Namensraum

[..]


# Zur Beschreibung der Sinc-Funktion werden zunächst die benötigten Variablen initialisiert:

# In[ ]:


# Variablendefinition für sinc-Funktion

N       = 201                              # Anzahl Abtastwerte
t_total = 10                               # zeitlicher Ausschnitt der Sinc-Funktion [-T_total/2, ..., T_total/2]
A_sinc  = 1                                # Flächeninhalt ("Amplitude") der Sinc-Funktion
T_sinc  = 1                                # 'Periode' der Sinc-Funktion (erster Nulldurchgang)


# Erzeugung der Sinc-Funktion

t = np.linspace(-t_total/2, t_total/2, N) # Erzeugung der äquidistanten x-Abtastpunkte
sinc = A_sinc* np.sinc(t/T_sinc)           # Definition der Sinc-Funktion

#Graphische Darstellung
plt.title(u'Sinc im Zeitbereich')
plt.xlabel(u'k⋅Δt [Zeit]')
plt.ylabel(u's [Amplitude]')    
plt.plot(t, sinc)
plt.plot([-t_total/2,t_total/2],[0,0], 'k')    # Nulllinie
plt.show()


# Nun wird die erzeugte Sinc-Funktion mittels der FFT-Funktion diskret Fourier-transformiert: Dazu muss zudem noch der Frequenzbereich berechnet werden.

# In[ ]:


# Diskrete Fourier-Transformation

# Erzeugung der Fouriertransformation
f = np.linspace(0, (N-1)/t_total, N)       # Bestimmung des Frequenzbereichs
H    = fft(sinc)                           # Fouriertransformation der Sinc-Funktion

# Graphische Darstellung
plt.title(u'Sinctransformierte im Frequenzbereich')
plt.xlabel(u'n⋅Δf [Frequenz]')
plt.ylabel(u'S [Amplitude]')
plt.plot(f, np.abs(H))                      # Betrachtung des Absolutwerts der nun komplexen Funktion
plt.show()


# Die Funktion sieht aus wie eine in der Mitte halbierte Rechteckfunktion. Wenn man nun die Periodizität mit bedenkt, kann man die Funktion in der Mitte teilen und den rechten Hälfte in den negativen Frequenzbereich verschieben. Dies kann mit der Funktion [fftshift](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html) aus der Bibliothek numpy.fft umgesetzt werden. Das Array für den Frequenzbereich muss dazu auch angepasst werden.<br>
# Zum Vergleich mit dem gewünschten Frequenzgang wird in den Plot noch ein ideales Rechteck eingefügt.

# In[ ]:


# Darstellung der Fouriertransformation unter Berücksichtigung der Periodizität
# und Vergleich mit idealem Rechteck


# Verschieben des Frequenzbereichs
f_shift = np.linspace(-(N-1)/(2*t_total), (N-1)/(2*t_total), N)  

# Verschieben der Fouriertransformierten
H_shift = np.abs(np.fft.fftshift(H))

# Berechnung der Variablen für das ideale Rechteck 
tau_rect = 1/T_sinc
Amp_rect = A_sinc * T_sinc * (N-1) / t_total

rect_ideal = [..] # ToDo: Erzeugen Sie den idealen Rechteck-Frequenzgang mittels np.where()

#Graphische Darstellung
plt.gcf().set_size_inches(15, 6)
plt.title(u'verschobene Sinctransformierte im Frequenzbereich')
plt.xlabel(u'n⋅Δf [Frequenz]')
plt.ylabel(u'S [Amplitude]')
plt.plot(f_shift, H_shift)
plt.plot(f_shift, rect_ideal,ls=':', c='r')
plt.show()


# Rücktransformation und Vergleich mit Start-Sinc:

# In[ ]:


# inverse disktrete Fouriertransformation der Fouriertransformation
h    = ifft(H)   

h_real = np.real(h)
# Wertevergleich
dif = sinc - h_real

# Graphische Darstellung
plt.subplot(211)
plt.title(u'Rücktransformierter Sinc')
plt.xlabel(u'k [Zeit]')
plt.ylabel(u'st [Amplitude]')
plt.plot(t, h_real)
plt.plot([-t_total/2,t_total/2],[0,0], 'k')    # Nulllinie
             
plt.subplot(212)
plt.title(u'Differenz')
plt.xlabel(u'k [Zeit]')
plt.ylabel(u'dif [Amplitude]')
plt.plot(t, dif)
plt.gcf().set_size_inches(15, 10)
plt.show()      


# Der maximale Wertunterschied zwischen den dem Original-Sinc und der Rücktransformierten liegt unter dem Bereich von $10^{-15}$. Die Sinc-Funktion konnte dadurch nahezu perfekt wieder rekonstruiert werden.
# 
# ---

# ### References
# 
# 1. Bild (Type of transformation) von [Steven W. Smith](http://www.dspguide.com/ch8/1.htm), Bild (Fourier Series) von [Lucas V. Barbosa](https://en.wikipedia.org/wiki/File:Fourier_series_and_transform.gif)   
# 2. [Offizielle Tutorials](https://docs.python.org/3.7/tutorial/) über Python
# 3. [Einführung](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html#Introduction) von Jupyter Notebook
# 4. Eine visuelle Einführung von Fourier-Transformation: [What is the Fourier Transform](https://www.youtube.com/watch?v=spUNpyF58BY)
# 5. DSP Guide: [The Scientist and Engineer's Guide to
# Digital Signal Processing](http://www.dspguide.com/pdfbook.htm)
# ---
# <div>Notebook erstellt von Arne-Lukas Fietkau, Yifei Li  und <a href="mailto:christoph.wagner@tu-dresden.de?Subject=Frage%20zu%20Jupyter%20Notebook%200.2%20Einführung" target="_top">Christoph Wagner</a></div>
