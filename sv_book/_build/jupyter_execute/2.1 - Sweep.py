#!/usr/bin/env python
# coding: utf-8

# # 2.1 - Sweep

# <img style="float: right" src="img/1-title.gif" width="600">
# 
# Sweeps sind eine beliebte Methode zur Messung der Übertragungsfunktion eines linearen Systems, da sie eine Reihe von positiven Eigenschaften aufweisen wie bspw. einen (einstellbaren) glatten Amplitudenfrequenzgang.
# 
# Das Thema der Sweeps wird in der Vorlesung in Thema 3: "Messung der Übertragungsfunktion und Impulsantworten" behandelt und das hier präsentierte Beispiel wird in der 6. Übungseinheit per Hand berechnet.
# 
# ## Inhalt  
# <table style="width:330px; border: 1px solid black; display: inline-block">
#     <tr>
#         <td style="text-align:right" width=64px><img src="img/TITLE-linear.png" style="float:left"></td>
#         <td style="text-align:left" width=300px>
#             <a style="color:black; font-size:14px; font-weight:bold; text-decoration:none" href='#1'>
#                 1. Sweep mit konstanter Hüllkurve
#             </a>
#         </td>
#     </tr>  
#     <tr>
#         <td style="text-align:right"><img src="img/TITLE-triang.png" style="float:left"></td>
#         <td style="text-align:left" width=128px>
#             <a style="color:black; font-size:14px; font-weight:bold; text-decoration:none" href='#2'>
#                 2. Sweep mit Dreieck-Hüllkurve
#             </a>
#         </td>
#     </tr>
#     <tr>
#         <td style="text-align:right"><img src="img/TITLE-Python.png" style="float:left"></td>
#         <td style="text-align:left" width=128px>
#             <a style="color:black; font-size:14px; font-weight:bold; text-decoration:none" href='#3'>
#                 3. Realisierung mit Python-Modulen
#             </a>
#         </td>
#     </tr>
# </table>
# 

# ---
# <a id='1'></a><div><img src="img/TITLE-linear.png" style="float:left"><h2 style="position: relative; top: 6px; left: 6px">1. Sweep mit konstanter Hüllkurve</h2></div>
# 
# Ein Sweep $x(t)$ im Zeitbereich ist eine harmonische Schwingung mit zeitabhängigem Phasenargument $\varphi (t)$, dessen Momentanfrequenz $\omega (t)$ mit der Zeit monoton zu- oder abnimmt (weswegen er auch Gleitsinus genannt wird, in Abgrenzung zu Sinusschwingungen mit einer konstanten Phase) :
# \begin{equation*}
# x(t)=x_{0} \cdot \sin (\varphi (t))\; \; mit \; \; \omega (t)=\frac{\mathrm{d} \varphi (t)}{\mathrm{d} t}\; \; 
# \rightarrow \; \;  x(t)=x_{0} \cdot \sin \left( \int \omega (t)dt + \varphi_{0} \right)
# \end{equation*}  
# In der Umgebung eines Zeitpunkts $t_{0}$ mit der _Momentanfrequenz_ $\omega _{0}$ nähert sich $x(t)$ einer Sinusfunktion mit der Frequenz $\omega _{0}$ an.
# 
# Zur Erzeugung eines Sweeps mit linearer Hüllkurve und linearer Frequenzänderung erhält man folgende Formel:
# 
# \begin{equation*}
# x(t)=x_{0} \cdot \sin \left( \omega_{start} \cdot t + \frac{\omega_{end} - \omega_{start}}{2 \cdot T_s} \cdot t^2 \right)
# \end{equation*}
# 
# ---
# 
# Neben den schon bekannten Modulen `matplotlib`, `numpy`, `scipy` und `simpleaudio`, wird in diesem Notebook das Modul [`ipywidgets`](https://ipywidgets.readthedocs.io/en/stable/) eingeführt. Damit lassen sich Benutzeroberflächen (user interface / UI) einfügen, wie zum Beispiel Schieberegler, mit denen sich Variablenwerte einstellen lassen. Dieses Modul müssen sie wahrscheinlich noch über `pip install` installieren. Wenn Sie das getan haben, können Sie nun alle für dieses Modul benötigten Module importieren:

# In[1]:


'''
Import externer Module
'''
# ToDo: Importieren Sie:
#    - numpy mit dem Alias np,
#    - simpleaudio mit dem Alias sa,
#    - Das Modul pyplot aus der Bibliothek matplotlib mit dem Alias plt,
#    - Die Module signal und fftpack aus der Bibliothek scipy in den globalen Namenraum,
#    - Das Modul interact_manual aus der Bibliothek ipywidgets in den globalen Namenraum.

[..]
[..]
[..]
[..]
[..]


# Die Variablen für die Berechnung des linearen Sweeps sind: 
#  - *fs_Hz*: Abtastfrequenz (für diese Aufgabe relativ beliebig),
#  - *A*: Amplitude des Sweeps (für diese Aufgabe relativ beliebig),
#  - *fStart_Hz*: Startfrequenz des Sweeps,
#  - *fEnd_Hz*: Endfrequenz des Sweeps,
#  - *T_s*: Dauer des Sweep.
#  
# Erstellen Sie zunächst eine Funktion "sweep_linear", die über die Eingabevariablen [`fs_Hz`, `fStart_lin_Hz`, `fEnd_lin_Hz`, `T_s` und `A`] die zwei Ausgabevariablen [`t_s` (Array mit Abtastzeitpunkten) und `sweep` (Array mit Werten des linearen Sweeps an den Zeitpunkten von `t_s`)] erzeugt.

# In[ ]:


'''
Definition der Funktion sweep_linear
'''
# ToDo: Erzeugen Sie eine Funktion, die die Abtastzeitpunkte und die zugehörigen Sweepwerte ausgibt.

def sweep_linear( [..] ):   # Eingangsvariablen sind fs_Hz, fStart_lin_Hz, fEnd_lin_Hz, T_s und A
    t_s = [..]              # lineares Array mit den Abtastzeitpunkten zwischen [0, T_s] Sekunden bei einer Abtastfreq von fs_Hz
    wstart_rad_per_s = [..] # Umrechnung von Start-Frequenz in Kreisfrequenz
    wend_rad_per_s = [..]   # Umrechnung von End-Frequenz in Kreisfrequenz
    sweep = [..]            # Berechnete Sweepwerte an den Abtastzeitpunkten von t_s
    return t_s, sweep


# Nun initialisieren Sie die Variablen für die Berechnung des Sweeps. Die Werte der Variablen sollen dabei wie folgt sein:
#  - *fs_Hz*: 16 kHz,
#  - *A*: 1,
#  - *fStart_Hz*: 50 Hz,
#  - *fEnd_Hz*: 400 Hz,
#  - *T_s*: 4 s.
#  
# Führen Sie mit diesen Variablen die Funktion "sweep_linear" aus und lassen Sie sich diese graphisch darstellen:

# In[ ]:


'''
Variableninitialisierung und Erzeugen der Zeitfunktion des Sweeps
'''
# Variableninitialisierung
# ToDo: Initialisieren Sie die Variablen
[..]
[..]
[..]
[..]
[..]

# Zeitbereich
time_s, sweep_lin = [..] # ToDo: Wenden Sie die Funktion sweep_linear an

# Graphische Darstellung des Sweeps
plt.title('Sweep von %d Hz bis %d Hz' %(fStart_Hz, fEnd_Hz))
plt.xlabel('Zeit [s]') 
plt.ylabel('x(t)') 
plt.plot(time_s, sweep_lin)
plt.gcf().set_size_inches(20, 5)
plt.show()


# Nun können Sie sich den erzeugten Sweep auch anhören! Erstellen Sie dafür eine Funktion "play_audio", die mittels `simpleaudio` Arrays ausgibt (wie in Kapitel 1.3 eingeführt). Nutzen Sie dann die neu definierte Funktion, um sich den Sweep auszugeben. <br>(Achtung: Das Signal ist sehr laut!)

# In[ ]:


'''
Definition der Funktion play_audio
'''
# ToDo: Erstellen sie eine Funktion, die das Eingangsarray in ein INT16 verwandelt und dann via simpleaudio ausgibt.
def play_audio( [..] ):
    [..]


# In[ ]:


'''
Audioausgabe
'''
[..] # ToDo: wenden Sie die Funktion "play_audio" an, um sich "sweep_lin" anzuhören.


# Es ist zudem sehr interessant, wie das Signal im Frequenzbereich aussieht. Wenden Sie deswegen die in der folgenden Funktion "fft_sweep" definiert Fast-Fourier-Transformation auf den Sweep an:

# In[ ]:


'''
Definition der Funktion fft_sweep
'''
def fft_sweep(sweep, fs_Hz):
    N = sweep.size # Länge von FFT
    f_Hz = np.linspace(0, fs_Hz/2, int(N/2)) # Frequenzbereich
    sweep_fft = fftpack.fft(sweep, N)
    sweep_fft_plot = np.abs(sweep_fft[:len(f_Hz)]) / int(N/2)
    return f_Hz, sweep_fft_plot


# In[ ]:


'''
Erzeugen des Frequenzgangs des Sweeps
'''
# ToDo: Wenden Sie die Funktion "fft_sweep" auf das Sweepsignal an
f_Hz, sweep_fft_plot = [..]

# Graphische Darstellung
plt.title('Amplitudenfrequenzgang')
plt.xlabel('Frequenz [Hz]') 
plt.ylabel('|X(f)|') 
plt.plot(f_Hz, sweep_fft_plot)
plt.axis([fStart_Hz*0.5, fEnd_Hz*1.1, 0, np.max(sweep_fft_plot)*1.1])
plt.gcf().set_size_inches(20, 5)
plt.show()


# Der Frequenzgang zeigt an den Rändern des Frequenzbands eine starke Welligkeit auf. Um diese zu entfernen, kann die Frequenz mittels Ein- und Ausblenden geglättet werden. Dies soll hier mit einem Tukey-Fenster aus dem Objekt [`signal.get_window()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html) umgesetzt werden.

# In[ ]:


'''
Erzeugen des Tukey-Fensters
'''
window = [..] # ToDo: Erzeugen Sie mittels signal.get_window() ein Tukey-Fenster über folgende Var: ('tukey', 0.2), len(sweep_lin)

plt.title('Tukey-Fenster')
plt.xlabel('Zeit [s]') 
plt.ylabel('window(t)') 
plt.plot(time_s, window)
plt.gcf().set_size_inches(20, 5)
plt.show()


# In[ ]:


'''
Fensterung des Sweep-Signals
'''
# Zeitbereich
sweep_win = [..]           # ToDo: Fesntern Sie sweep_lin mit dem Tukey-Fenster

# Frequenzbereich
f_Hz, sweep_win_fft = [..] # ToDo: Wenden Sie eine FFT mittels der Funktion "fft_sweep" auf sweep_win an

# Graphische Darstellung
plt.subplot(211)
plt.title('Sweep von %d Hz bis %d Hz' %(fStart_Hz, fEnd_Hz))
plt.xlabel('Zeit [s]') 
plt.ylabel('x(t)') 
plt.plot(time_s, sweep_win)

plt.subplot(212)
plt.title('Amplitudenfrequenzgang')
plt.xlabel('Frequenz [Hz]') 
plt.ylabel('|X(f)|') 
plt.plot(f_Hz, sweep_win_fft)
plt.axis([fStart_Hz*0.5, fEnd_Hz*1.1, 0, np.max(sweep_fft_plot)*1.1])

plt.gcf().set_size_inches(20, 10)
plt.show()


# In[ ]:


'''
Audioausgabe
'''
[..] # ToDo: wenden Sie die Funktion "play_audio" an, um sich "sweep_win" anzuhören.


# Durch die Fensterung sollte die Welligkeit im Frequenzbereich verringert worden sein. Nur verringert sich dadurch auch die Amplitude der äußeren Frequenzen.
# 
# ---
# 
# Um sich die Veränderungen von Fenstern oder Frequenzen interaktiv anschauen zu können, wird nun das Modul [`ipywidgets`](https://ipywidgets.readthedocs.io/en/stable/index.html) genutzt. Durch dieses können Variablen verändert werden und mittels Drop-Down-Menüs oder Häckchen-Kästen die Ausgabe verändert werden. Probieren Sie es einfach aus. Sie müssen dafür noch in dem folgenden Code Ihre definierten Funktionen einfügen:

# In[ ]:


'''
Initialisierung fester Variablen
'''
fs_Hz = 16e3
amplitude = 1


# In[ ]:


'''
Interaktive Sweepdarstellung
'''
@interact_manual(T_s_i=(0.1, 5, 0.1), fStart_Hz_i=(10, 5000, 10), fEnd_Hz_i=(10, 5000, 10), windowing_i = False, window_type_i=[('tukey', 1), ('triang', 2)], win_alpha_i=(0, 1, 0.01), output_sound_i = True)
def interactive_linear_sweep(T_s_i=2, fStart_Hz_i=10, fEnd_Hz_i=100, windowing_i=False, window_type_i='tukey', win_alpha_i=0.2, output_sound_i=True):
    # Erzeugung des Sweeps
    time_s, sweep = [..] # ToDo: Fügen Sie die Funktion zur Erzeugung eines linearen Sweeps ein.
    
    # Optionales Fenstern des Sweeps
    if windowing_i == True:
        if window_type_i == 1:
            window = signal.get_window(('tukey', win_alpha_i), len(sweep))
        elif window_type_i == 2:
            window = signal.get_window('triang', len(sweep))
        sweep = sweep * window
    
    # Graphische Darstellung des Zeitbereichs
    plt.title('Sweep von %d Hz zu %d Hz' %(fStart_Hz_i, fEnd_Hz_i))
    plt.xlabel('Zeit [s]') 
    plt.ylabel('x(t)') 
    plt.plot(time_s, sweep)
    plt.gcf().set_size_inches(20, 5)
    plt.show()
    
    # FFT des Sweeps
    f_Hz, sweep_fft_plot = [..] # ToDo: Fügen Sie die Funktion zur Erstellung der FFT ein.

    # Graphische Darstellung des Frequenzbereichs
    plt.title('Amplitudenfrequenzgang')
    plt.xlabel('Frequenz [Hz]') 
    plt.ylabel('|X(f)|') 
    plt.plot(f_Hz, sweep_fft_plot)
    if fStart_Hz_i <= fEnd_Hz_i:
        plt.axis([fStart_Hz_i*0.5, fEnd_Hz_i*1.2, 0, np.max(sweep_fft_plot)*1.1])
    else:
        plt.axis([fEnd_Hz_i*0.5, fStart_Hz_i*1.2, 0, np.max(sweep_fft_plot)*1.1])
    plt.gcf().set_size_inches(20, 5)
    plt.show()
    
    
    # Optionale Audioausgabe
    if output_sound_i == True:
        [..] # ToDo: Fügen Sie die Funktion zum Abspielen des Signals ein


# <a id='2'></a><div><img src="img/TITLE-triang.png" style="float:left"><h2 style="position: relative; top: 6px; left: 6px">2. Sweep mit Dreieck-Hüllkurve</h2></div>
# 
# Im Nachfolgenden soll der in Übung 6.1 händisch berechnete Sweep implementiert und visualisiert werden. Dabei soll der Sweep im Frequenzbereich eine konstante Amplitude in seinem Band erhalten. Um das Frequenzverhalten eines linearen Sweeps zu betrachten, welches mit einem Dreieck gefenstert wurde, kann in der vorherigen Zelle betrachtet werden, wenn man das Fenster 'triang' wählt.
# 
# ---
# 
# Zunächst werden die Grundparameter definiert. Die Start- und Endfrequenz $f_{start} = 200 \ Hz$ und $f_{end} = 1000 \ Hz$ bzw. $\omega_{start}$ und $\omega_{end}$ sowie die notwendige Abtastfrequenz $f_s = 16 \ kHz$ festgelegt:

# In[ ]:


'''
Grundparameter definieren:
'''
# Initialisieren Sie die Variablen mit den richtigen Werten
fs_Hz = [..]     # Abtastfrequenz (für diese Aufgabe relativ beliebig)
dt_s = 1/fs_Hz   # Zeitintervall
fStart_Hz = [..]  # Startfrequenz [Hz]
fEnd_Hz = [..]   # Endfrequenz [Hz]
wStart_rad_per_s = [..]  # Startfrequenz [rad/s]
wEnd_rad_per_s = [..]  # Endfrequenz [rad/s]
wm_rad_per_s = [..]  # Mittenfrequenz [rad/s]


# Anschließend werden die Funktionen für die Phasenwinkel $\varphi_1(t)$ und $\varphi_2(t)$ definiert. Nutzen Sie dafür die berechneten Formeln aus 6.1 c):

# In[ ]:


'''
Definition der Funktion calculatePhi1
'''
def calculatePhi1( [..] ): # ToDo: Die Eingänge der Funktion sind t_s, wStart_rad_per_s, k und T_s
    phi = [..]             # ToDo: Bestimmen Sie die Gleichung zur Berechnung von Phi1
    [..]                   # ToDo: Geben Sie Phi zurück


# In[ ]:


'''
Definition der Funktion calculatePhi2
'''
def calculatePhi2( [..] ): # ToDo: Die Eingänge der Funktion sind t_s, wStart_rad_per_s, k und T_s
    phi = [..]             # ToDo: Bestimmen Sie die Gleichung zur Berechnung von Phi2
    [..]                   # ToDo: Geben Sie Phi zurück


# Durch die Diskontinuität in der Einhüllenden ($a(t)$) müssen in diesem Spezialfall zusätzliche Bedingungen erfüllt werden, damit die Phase an der Übergangssstelle kontinuierlich verläuft. Zum einen muss der Sweep-Phasenwinkel $\varphi(t)$ an der Stelle $T/2$ gleich sein:
# \begin{equation}
# \sin\left(\varphi_1\left(\frac{T}{2}\right)\right) = \sin\left(\varphi_2\left(\frac{T}{2}\right)\right) 
# \end{equation}
# 
# Substituiert man hier die berechneten Gleichungen aus der Übung für $\varphi_1(T/2)$ und $\varphi_2(T/2)$ ergibt sich die erste Bedingung
# \begin{equation}
# \sin\left(\frac{T\cdot(7\omega_1 + \omega_2)}{16}\right) = \sin\left(0\right) = 0.
# \end{equation}
# 
# Zum anderen muss auch die Ableitung des Sweep-Phasenwinkels, $\frac{\mathrm{d}\varphi(t)}{\mathrm{d}t}$ gleich sein, d.h. aus der ersten Bedingung folgt (innere Ableitung nicht vergessen):
# 
# \begin{align}
# &\cos\left(\frac{T\cdot(7\omega_1 + \omega_2)}{16}\right)\cdot \left(\frac{\omega_1 + \omega_2}{2}\right) = \cos\left(0\right)\cdot \left(\frac{\omega_1 + \omega_2}{2}\right) = 1 \\
# &\Leftrightarrow \cos\left(\frac{T\cdot(7\omega_1 + \omega_2)}{16}\right) = 1.
# \end{align}
# 
# Beide Gleichungen sind erfüllt, wenn das Argument ein Vielfaches von $2\pi$ ist. Damit kann die Sweepdauer $T$ explizit durch
# 
# \begin{equation}
# \frac{T}{16}\left(\omega_1 + \omega_2\right) = 2\pi\cdot n,\qquad n=0,1,2,3,\dots
# \end{equation}
# 
# berechnet werden und ist durch $n\in \mathbb{N}$ nicht komplett frei wählbar.
# Dieser Zusammenhang für die Periode $T$ soll nun in der nachfolgenden Funktion definiert:

# In[ ]:


'''
Definition der Funktion calculatePeriod
'''
def calculatePeriod( [..] ): # ToDo: Die Eingänge der Funktion sind wStart_rad_per_s, wEnd_rad_per_s und n_periods
    T_s = [..]               # ToDo: Setzen Sie die obige Gleichung zur Berechnung von T_s ein.
    [..]                     # ToDo: Geben Sie T_s zurück


# Zudem muss der Faktor k aus 6.1.b) berechnet werden. Dafür wird nun auch eine Funktion definiert:

# In[ ]:


'''
Definition der Funktion calculatek
'''
def calculatek( [..] ): # ToDo: Die Eingänge der Funktion sind wStart_rad_per_s, wEnd_rad_per_s und T_s
    k = [..]            # ToDo: Bestimmen Sie die Gleichung zur Berechnung von k.
    [..]                # ToDo: Geben Sie k zurück


# Zu guter Letzt werden noch die beiden Funktionen für die Berechnung der Amplitudenmodulaton $a(t)$ für beide Hälften definiert. Nutzen Sie dafür die Formeln aus 6.1 a):

# In[ ]:


'''
Definition der Amplituden-Funktionen
'''
def calculateAmplitude1( [..] ):   # ToDo: Die Eingänge der Funktion sind t_s und T_s
    a = [..]                       # ToDo: Bestimmen Sie die Gleichung zur Berechnung von a_1
    [..]                           # ToDo: Geben Sie a zurück

def calculateAmplitude2( [..] ):   # ToDo: Die Eingänge der Funktion sind t_s und T_s
    a = [..]                       # ToDo: Bestimmen Sie die Gleichung zur Berechnung von a_2
    [..]                           # ToDo: Geben Sie a zurück


# Nun berechnen wir zuerst die Sweepdauer, indem wir die Funktion "calculatePeriod" verwenden und dafür die Variable n_periods auf 300 festsetzen (der Wert ist hier egal). Daraus lässt sich zudem die Konstante k aus 6.1. b) bestimmen:

# In[ ]:


'''
Berechnung von T_s und k
'''
n_periods = 300;

# Sweepdauer T berechnen in Abhängigkeit von ganzen Perioden 2*pi*n:
T_s = [..]  # ToDo: Verwenden Sie die Funktion "calculatePeriod" zur Berechnung von T_s
print("Sweepdauer: {} Sekunden.\n".format(T_s))

# Konstante k:
k = [..]    # ToDo: Verwenden Sie die Funktion "calculatek" zur Berechnung von k


# Jetzt können wir den Sweep damit berechnen und plotten:

# In[ ]:


'''
Implementierung des Sweeps nach Übung 6.1
'''
# Laufvariable t definieren:
t1_s = np.linspace(0, T_s/2, int(fs_Hz*T_s/2))
t2_s = np.linspace(T_s/2+dt_s, T_s, int(fs_Hz*T_s/2-1))

# Phasenwinkel für beide Abschnitte:
phi1_rad = [..] # ToDo: Verwenden Sie die Funktion "calculatePhi1"
phi2_rad = [..] # ToDo: Verwenden Sie die Funktion "calculatePhi2"

# Einhüllende für beide Abschnitte:
a1 = [..] # ToDo: Verwenden Sie die Funktion "calculateAmplitude1"
a2 = [..] # ToDo: Verwenden Sie die Funktion "calculateAmplitude2"

# Vollständigen Sweep zusammensetzen:
sweep1 = a1 * np.sin(phi1_rad)
sweep2 = a2 * np.sin(phi2_rad)
t_s = np.append(t1_s, t2_s)        
sweep = np.append(sweep1, sweep2)

# Plot
plt.title('Sweep von %d Hz bis %d Hz' %(fStart_Hz, fEnd_Hz))
plt.xlabel('Zeit [s]') 
plt.ylabel('x(t)') 
plt.plot(t_s, sweep)
plt.gcf().set_size_inches(20, 5)
plt.show()


# Um sicherzustellen, dass der Sweep tatsächlich das (annähernd) glatte Spektrum über den definierten Frequenzbereich von $f_{start}$ bis $f_{end}$ besitzt, wird der Amplitudenfrequenzgang $|X(k)|$ über die FFT berechnet. Dazu kann die im ersten Teil definierte Funktion "fft_sweep" verwendet werden:

# In[ ]:


'''
Aufgabe: Spektrum des Sweeps berechnen
'''
f_Hz, sweep_fft_plot = [..] # ToDo: Verwenden Sie die Funktion "fft_sweep()" zur FFT von sweep

# Plot 
plt.title('Amplitudenfrequenzgang')
plt.xlabel('Frequenz [Hz]') 
plt.ylabel('|X(f)|') 
plt.plot(f_Hz, sweep_fft_plot)
plt.axis([fStart_Hz*0.5, fEnd_Hz*1.2, 0, np.max(sweep_fft_plot)*1.1])
plt.gcf().set_size_inches(10, 5)
plt.show()


# Abspielen des Sweepssignal $x(t)$ ergibt das charakteristische Sweepgeräusch. Hierzu können Sie auch die aus dem ersten Part definierte Funktion "playaudio()" verwenden:

# In[ ]:


'''
Audioausgabe
'''
[..] # ToDo: wenden Sie die Funktion "play_audio" an, um sich "sweep" anzuhören.


# ----
# Zum Schluss wollen wir uns das Ergebnis noch einmal als interaktives Modul anschauen. Dazu wird wieder die Funktion `interact` aus dem Modul `ipywidgets` verwendet:

# In[ ]:


'''
Initialisierung fester Variablen
'''
fs_Hz = 16e3
dt_s = 1/fs_Hz


# In[ ]:


'''
Interaktive Sweepdarstellung
'''
@interact_manual(n_periods_i=(1, 1000, 1), fStart_Hz_i=(10, 5000, 10), fEnd_Hz_i=(10, 5000, 10), output_sound_i = True)
def interactive_rect_sweep(n_periods_i=300, fStart_Hz_i=200, fEnd_Hz_i=1000, output_sound_i=True):
    
    
    # Berechnung der Koeffizienten
    wStart_rad_per_s_i = fStart_Hz_i * 2 * np.pi  # Startfrequenz [rad/s]
    wEnd_rad_per_s_i = fEnd_Hz_i * 2 * np.pi  # Endfrequenz [rad/s]
    T_s_i = [..]  # ToDo: Verwenden Sie die Funktion "calculatePeriod" zur Berechnung von T_s
    k_i =   [..]  # ToDo: Verwenden Sie die Funktion "calculatek" zur Berechnung von k

    # Laufvariable t definieren:
    t1_s_i = np.linspace(0, T_s_i/2, int(fs_Hz*T_s_i/2))
    t2_s_i = np.linspace(T_s_i/2+dt_s, T_s_i, int(fs_Hz*T_s_i/2-1))
    
    # Phasenwinkel für beide Abschnitte:
    phi1_rad_i = [..] # ToDo: Verwenden Sie die Funktion "calculatePhi1"
    phi2_rad_i = [..] # ToDo: Verwenden Sie die Funktion "calculatePhi2"

    # Einhüllende für beide Abschnitte:
    a1_i = [..] # ToDo: Verwenden Sie die Funktion "calculateAmplitude1"
    a2_i = [..] # ToDo: Verwenden Sie die Funktion "calculateAmplitude2"

    # Vollständigen Sweep zusammensetzen:
    sweep1_i = a1_i * np.sin(phi1_rad_i)
    sweep2_i = a2_i * np.sin(phi2_rad_i)
    t_s_i = np.append(t1_s_i, t2_s_i)        
    sweep = np.append(sweep1_i, sweep2_i)
    
    # Graphische Darstellung des Zeitbereichs
    plt.title('Sweep von %d Hz zu %d Hz' %(fStart_Hz_i, fEnd_Hz_i))
    plt.xlabel('Zeit [s]') 
    plt.ylabel('x(t)') 
    plt.plot(t_s_i, sweep)
    plt.gcf().set_size_inches(20, 5)
    plt.show()
    
    # FFT des Sweeps
    f_Hz, sweep_fft_plot = fft_sweep(sweep, fs_Hz)

    # Graphische Darstellung des Frequenzbereichs
    plt.title('Amplitudenfrequenzgang')
    plt.xlabel('Frequenz [Hz]') 
    plt.ylabel('|X(f)|') 
    plt.plot(f_Hz, sweep_fft_plot)
    if fStart_Hz_i <= fEnd_Hz_i:
        plt.axis([fStart_Hz_i*0.5, fEnd_Hz_i*1.2, 0, np.max(sweep_fft_plot)*1.1])
    else:
        plt.axis([fEnd_Hz_i*0.5, fStart_Hz_i*1.2, 0, np.max(sweep_fft_plot)*1.1])
    
    plt.gcf().set_size_inches(20, 5)
    plt.show()
    
    
    # Optionale Audioausgabe
    if output_sound_i == True:
        play_audio(sweep)


# ----
# 
# <a id='3'></a><div><img src="img/TITLE-Python.png" style="float:left"><h2 style="position: relative; top: 6px; left: 6px">3. Realisierung mit Python-Modulen</h2></div>
# 
# Im Modul scipy ist die Funktion [signal.chirp()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.chirp.html) als Frequenzgesteuerter Kosinusgenerator vorhanden, dadurch können Sweeps deutlich einfacher erzeugt werden. Zudem kann mit dem Modul [signal.spectrogram()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.spectrogram.html) das Signal in einem Spektrogramm betrachtet werden.

# In[ ]:


'''
Erzeugen des Sweep mittels signal.chirp()
'''
from scipy.signal import chirp, spectrogram

# Sweep-Parameter definieren:
fsChirp_Hz = 16000
TChirp_s = 3
tChirp_s = np.linspace(0, TChirp_s, TChirp_s*fsChirp_Hz, endpoint=False)
chirpStartFreq_Hz = 200
chirpEndFreq_Hz = 1000

# Sweep und dessen Amplitudenfrequeuzgang berechnen:
xSweep = chirp(tChirp_s, chirpStartFreq_Hz, TChirp_s, chirpEndFreq_Hz, 'linear')
fChirp_Hz, tChirpSg_s, XSweep_f = spectrogram(xSweep, fsChirp_Hz, nperseg=250)

# Plot
plt.subplot(121)
plt.title('Linearer Chirp, f(0)=%d Hz, f(%d)=%d Hz' %(chirpStartFreq_Hz, TChirp_s, chirpEndFreq_Hz))
plt.xlabel('Zeit [s]') 
plt.ylabel('$x_{sweep}$(t)') 
plt.plot(tChirp_s, xSweep)
plt.subplot(122)
plt.title('Spektrogramm')
plt.xlabel('Frequenz [Hz]') 
plt.ylabel('|$X_{sweep}$(f)|') 
plt.pcolormesh(tChirpSg_s, fChirp_Hz, XSweep_f,shading='gouraud')
plt.gcf().set_size_inches(15, 5)
plt.show()


# In[ ]:


'''
Aufgabe: Sweep abspielen
'''
# Werte in 16-Bit-Daten konvertieren
sound = (xSweep*(2**15-1)/np.max(np.abs(xSweep))).astype(np.int16)

# Abspielen
play_obj = sa.play_buffer(sound, 1, 2, int(fsChirp_Hz))
play_obj.wait_done()


# Die Verwendung eines Spektrogramms statt eines einfachen Spektrums zur Darstellung des Frequenzbereiches (in diesem Falle in zusätzlicher Abhängigkeit von der Zeit) wird im nächsten Notebook noch ausführlich behandelt.
# 
# ---
# 
# ### References
# 
# 1. Titelbild von [wikimedia](https://commons.wikimedia.org/wiki/File:Chirp_animation.gif?uselang=de)  
# 2. [Sweep (Signalverarbeitung)](https://de.wikipedia.org/wiki/Sweep_(Signalverarbeitung))  
# 3. [Sinusoidal Sweep Signals](https://learn.digilentinc.com/Documents/132)  
# 4. [Sine Sweep](https://theaudioprogrammer.com/signal-analysis-ii-linear-vs-logarithmic-sine-sweep/)  
# ---
# <div>Notebook erstellt von Arne-Lukas Fietkau, Yifei Li  und <a href="mailto:christoph.wagner@tu-dresden.de?Subject=Frage%20zu%20Jupyter%20Notebook%201.2%20IIR%20Filterentwurf" target="_top">Christoph Wagner</a></div>
