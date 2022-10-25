#!/usr/bin/env python
# coding: utf-8

# # 0.1 - Installationsanleitung

# <img style="float: right; margin:5px 0px 0px 10px" src="img/Titel.png" width="400">
# Begleitend zur Übung des Fachs Signalverarbeitung wird Ihnen eine Reihe an Jupyter-Notebooks zur Verfügung gestellt. Diese soll Ihnen sowohl beim Verständnis der in der Vorlesung und Übung behandelten Themen helfen, als auch die Fähigkeit zur selbstständigen Lösung eigener Problemstellungen geben.
# 
# Die Bearbeitung der Notebooks ist dabei komplett freiwillig. Falls Sie aber Probleme, Fragen und Anmerkungen haben, posten Sie diese gerne ins Opal-Forum oder senden Sie uns eine Mail. 
# 
# 
# Dieses Notebook soll Ihnen beim Einstieg mit Python und der Installation von Modulen helfen. Weitere Notebooks werden zeitnah zur jeweiligen Übung online gestellt.
# 
# 
# ## Inhalt  
# <table style="width:256px; border: 1px solid black; display: inline-block">
#     <tr>
#     <td  style="text-align:right" width=64px><img src="img/IMG-binder.svg" style="float:left"></td>
#       <td style="text-align:left" width=256px>
#           <a style="color:black; font-size:14px; font-weight:bold; text-decoration:none" href='#binder'>1. Binder</a>
#       </td>
#   </tr>  
#     <tr>
#     <td  style="text-align:right" width=64px><img src="img/IMG-Python.png" style="float:left"></td>
#       <td style="text-align:left" width=256px>
#           <a style="color:black; font-size:14px; font-weight:bold; text-decoration:none" href='#python'>2. Python</a>
#       </td>
#   </tr>  
#   <tr>
#     <td style="text-align:right"><img src="img/IMG-jupyter.png" style="float:left"></td>
#     <td style="text-align:left" width=128px><a style="color:black; font-size:14px; font-weight:bold; text-decoration:none" href='#jupyter'>3. Jupyter Notebooks</a>
#       </td>
#   </tr>
# </table>

# <a id='binder'></a><div><img src="img/IMG-binder.svg" width=24px style="float:left"><h2 style="position: relative; top: 6px; left: 6px">  1. Binder </h2></div>
# 
# Sie schauen sich dieses Notebook sicherlich zuerst über den Service [```Binder```](https://mybinder.org/) an. Dieses Tool erlaubt es, auf Github hochgestellte Jupyter-Notebooks -wie zum Beispiel dieses- über einen externen Server auszuführen. Das gibt einem die Möglichkeit, sich Projekte ohne Download der Daten und ohne lokal installiertes Python anzuschauen. Gestartete Sessions werden aber nach ungefähr 10 Minuten Inaktivität vom Server geschlossen und alle Änderungen gehen damit verloren. [Hier gibt es weitere Informationen dazu.](https://mybinder.readthedocs.io/en/latest/about/about.html)
# 
# Falls Sie also die von Ihnen bearbeiteten Notebooks gerne wiederverwenden möchten, ist eine Installation von Python notwendig. Eine Anleitung zur Installation unter Windows gibt es in den folgenden Kapiteln.
# 
# ***

# <a id='python'></a><div><img src="img/IMG-Python.png" style="float:left"><h2 style="position: relative; top: 6px; left: 6px">  2. Python </h2></div>
# 
# <h4> Allgemeines</h4>
# 
# 
# Python ist eine Skriptsprache auf hoher Ebene, die Interpretation, Kompilierung, Interaktivität und Objektorientiertheit kombiniert. Python ist leicht zu erlernen, einfach zu lesen, und hat eine breite Palette von Standardbibliotheken. Einer der größten Vorteile von Python ist seine umfangreiche Bibliothek, die plattformübergreifend und mit UNIX, Windows und Macintosh kompatibel ist. Es gibt viele Tutorials über Python wie zum Beispiel auf [w3schools](https://www.w3schools.com/python/).   
# 
# Falls Sie Python auf Ihren Rechner installieren wollen, gibt es im Folgenden eine Anleitung für Windows-Nutzer*innen, da die Installation und Nutzung von Python zum Teil sehr Kommandozeilen-intensiv sind.
# 
# *Hinweis:* Es gibt zudem auch die Software `Anaconda`, die die Nutzung von Python und Jupyter-Notebooks vereinfacht. Bei Anaconda sind viele weitere externe Module schon vorinstalliert. Wir wollen Ihnen aber im Folgenden eine Anleitung geben, wie sie mit dem normalen Python umgehen. Falls Sie also Probleme bei der direkten Installation von Python haben, können Sie als Option auf die [Anaconda-Software zurückgreifen.](https://www.anaconda.com/products/individual) Sie können sich aber zuerst auch gerne an uns wenden.
# 
# <br>
# 
# <h4>Installations- und Nutzungsanleitung von Python</h4>
# 
# Nun wird Ihnen Schritt für Schritt erklärt, wie Sie Python installieren können. Zuerst sollten Sie auf Ihren PC nachschauen, ob Sie schon eine Pythonversion installiert haben.
# 
# 1. **Kontrolle auf installierte Python-Versionen** <br>
# Öffnen Sie eine Eingabeaufforderung (cmd) und geben Sie den Befehl `py -0p` ein. Mit diesem Kommando wird -wenn verfügbar- der Python Launcher `py` ausgeführt, der nach ausführbaren Pythoninstallationen (sogenannten executables) sucht und diese nach ihren Versionen auflistet. Wenn dieser Befehl nicht gefunden wurde, haben Sie mit hoher Wahrscheinlichkeit kein Python installiert. Falls doch, schauen Sie über den angezeigten Pfad nach, ob es sich um ein von einem anderen Programm intern installiertes Python handelt. Falls dies der Fall ist, sollten Sie es lieber nicht verändern und ein neues Python installieren. Wenn Sie ein veraltetes Python installiert haben, können Sie die Zeit jetzt nutzen und eine neue Version installieren und Ihre alte Version entweder löschen oder behalten. Sie können nämlich unterschiedliche Python-Versionen nebeneinander installiert haben
# 
# 
# 2. **Installation von Python:** <br>
# Die neuesten Versionen von Python [finden Sie hier](https://www.python.org/downloads/). Wählen Sie bei der Installation auch die Option "Add Python 3.X to PATH" aus! Diese Funktion fügt den Speicherort von "python.exe" (..\Python3X\) und den der externen Module (..\Python3X\Scripts\) in die Umgebungsvariable "PATH", damit bei Funktionsaufrufen über die Eingabeaufforderung auch diese Ordner durchsucht werden. <br>
#    *Hinweis:* Bei der Erstellung dieses Notebooks ist die Version 3.9.0 kürzlich veröffentlicht worden. Deshalb waren einige externe Module bis zur Fertigstellung des Notebooks immer noch nicht aktualisiert worden und konnten nicht über den normalen Weg für Python 3.9 installiert werden. Probieren Sie es aber zuerst aus, die neueste Python-Version zu installieren. Falls Sie jetzt immer noch Probleme haben sollten, lassen Sie Python 3.9 einfach installiert und laden sich die Version 3.8 herunter, womit Sie zunächst arbeiten können. Die Probleme mit den inkompatiblen Modulen für Python 3.9 sollten nur eine Frage der Zeit sein, bis diese behoben sind. Zudem ist das zweimalige Installieren von Python eine gute Übung! ;)
# 
# 
# 3. **Starten von Python:**<br>
# Python können Sie über die Eingabeaufforderung von Windows starten. Zum Öffnen der Eingabeaufforderung drücken Sie dafür zum Beispiel `Windows-Taste` + `R`, geben Sie "*cmd*" ein und drücken `Enter`.
# In der sich nun geöffneten Kommando-Shell können Sie Python über zwei unterschiedlichen Kommandos starten:
#  - Bei dem Befehl `python` sucht die Shell alle im "PATH"-Verzeichnis eingetragenen Ordner nach einer executable (.exe) mit dem Namen python (also python.exe). Dabei werden die Verzeichnisse systematisch von oben nach unten durchgegangen und beim ersten Treffer hört die Suche auf und die .exe wird ausgeführt. Falls Sie nur eine Version installiert haben, sind Sie damit vollkommen zufrieden. Falls Sie aber mehrere Python-Versionen installiert haben, würde dies bedeuten, dass Sie immer die Verzeichnisse (..\Python3X\) und (..\Python3X\Scripts\) der gewünschten Python-Version nach oben schieben müssen.
#  - Mit dem Befehl [`py`](https://www.python.org/dev/peps/pep-0397/) wird der "Python Launcher" aufgerufen, der bei der Installation von Python in das Verzeichnis C:\Windows\ installiert wird. Wenn dieser ohne weitere Bedingungen von Ihnen gestartet wird, läuft der Befehl ab wie der Befehl `python`. Mit dem "Python Launcher" kann aber bestimmt werden, welche Python-Version gestartet werden soll. Um zum Beispiel Python mit Version 3.8 zu starten, hängt man einfach ein `-3.8`an. Also als komplettes Kommando: `py -3.8`. (Wenn Sie mehr Interesse an einzelnen Funktionen haben, können Sie immer ein `-h` hinter jede Funktion schreiben. Z.B.: `py -h` oder `python -h`.)
# 
# Ein Python-Kernel startet und Ihnen sollte die Versionsnummer von dem von Ihnen installierten Python angezeigt werden. Falls dies nicht der Fall ist, müssen Sie gegebenenfalls den "PATH" in den Umgebungsvariablen editieren. Eine Anleitung dazu [finden Sie hier.](https://datatofish.com/add-python-to-windows-path/)
# 
# Sie können jetzt Python verwenden, indem Sie Ihren Code zeilenweise in die Eingabeaufforderung eingeben. Probieren Sie zum Beispiel folgenden Code aus:
# 
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# 
# 2 + 3 *[Enter]*
# 
# a = 6 *[Enter]*
# 
# b = 12 *[Enter]*
# 
# c = a + b *[Enter]*
#     
# c *[Enter]*                              #Kommentar: Ausgabe von c 
#     
# A = [[1,2,3], [4,5,6]] *[Enter]*         #Kommentar: Erstellen einer 2x3-Matrix 
#     
# A *[Enter]*                              #Kommentar: Ausgabe von A, equivalent zu print(A)
# </div>
# 
# Zum Schließen des Kernels können Sie entweder "*exit()*" oder  `Strg` + `Z` eingeben und mit `Enter` bestätigen.
# 
# <br>
# 
# <h4> Nutzung von Modulen </h4>
# 
# 
# Es gibt built-in und externe Module (auch Packages oder Libraries genannt, hier aber ein [Link über die genaue Wortdefinition](https://docs.python.org/3/tutorial/modules.html)).
# 
# Built-in Module können direkt verwendet werden und stellen die Basis zur Programmierung in Python dar. Zum Beispiel gibt es das Modul ```cmath``` für [komplexe Zahlen](https://docs.python.org/3/library/cmath.html#module-cmath). Daraus können Sie das Objekt ```complex()``` direkt nutzen, um eine komplexe Zahl zu erzeugen. Testen Sie den folgenden Code hier in der ausführbaren Zelle aus oder in Ihrer Eingabeaufforderung:

# In[ ]:


# Starten Sie den Code, indem sie die Zelle auswählen und den Run-Button drücken 
# oder mit Shift + Enter

c = complex(1.4, -3)  # Caste die Variable c als komplexe Zahl mit dem Wert 1.4 -3j
print(c)              # Ausgabe des Inhalts von c


# Die graphische Darstellung des Werts in einem Plot ist mit den internen Modulen aber zum Beispiel nicht mehr möglich. Dafür muss man sich mit einem externen Modul behelfen, zum Beispiel `matplotlib`. Diese externen Module müssen in Python installiert werden und für jedes Projekt importiert werden. Im Folgenden sind zwei Code-Zellen als Beispiel für installierte und nicht installierte Pakete im `Binder`-Projekt dargestellt.<br>
# Zuerst ein installiertes Modul zur Erzeugung von Plots:

# In[ ]:


# Starten Sie den Code, indem sie die Zelle auswählen und den Run-Button drücken
# oder mit Shift + Enter
import matplotlib.pyplot as plt

plt.scatter(c.real,c.imag, s=100)   # Ausgabe eines Punkts
plt.show()                          # Plot zeigen


# *Hinweis:* Falls Sie `matplotlib` schon lokal installiert haben und diesen über die Eingabeaufforderung nutzen, werden die Kommandos ausgeführt, nur wegen fehlender Ausgabemöglichkeit seitens der Eingabeaufforderung kann Ihnen der Plot nicht angezeigt werden.
# 
# Als Beispiel für einen nicht ausführbaren Code in dem `Binder`-Projekt ist die folgende Zelle mit dem Modul `pandas`, das nicht mitinstalliert wurde (und im Weiteren auch nicht benötigt wird). 

# In[ ]:


# Starten Sie den Code, indem sie die Zelle auswählen und den Run-Button drücken
# oder mit Shift + Enter
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
# Es sollte ein ModuleNotFoundError entstehen.


# Für das Einbinden von externen Modulen gibt [es folgende Kommandos](https://docs.python.org/3/tutorial/modules.html#more-on-modules):
# 
# *A) Import der kompletten Bibliothek*
# 
# ```python
# import numpy
# 
# ```
# - Der Befehl importiert die gesamte Bibliothek des Moduls mit dem eigenem Namensraum `numpy`. Das Modul numpy besitzt zum Beispiel die Objekte `cos()`, `sin()` oder `pi`. Durch den obigen Import lassen sich die Objekte aufrufen, indem man zuerst das Modul nennt: `numpy.cos()`, `numpy.sin()` oder `numpy.pi`.
# 
# 
# 
# *B) Import der kompletten Bibliothek mit alias*
# 
# ```python
# import numpy as np
# 
# ```
# - Wie bei A) importiert der Befehl die gesamte Bibliothek des Moduls, nur heißt der Namensraum nun `np`. Die Objekte `cos()`, `sin()` oder `pi` lassen sich nun folgendermaßen aufrufen: `np.cos()`, `np.sin()` oder `np.pi`.
# 
# 
# *C) Import einzelner Module aus der Bibliothek*
# 
# ```python
# from numpy import cos, sin, pi
# 
# ```
# - Mit diesem Befehl werden die einzelnen Objekte `cos()`, `sin()` und `pi` in den globalen Namensraum importiert. Diese können nun direkt aufgerufen werden, also mittels: `cos()`, `sin()` oder `pi`. Passen Sie dabei auf, dass der Name nicht schon belegt ist und es zur Kollision von gleichnamigen Objekten gibt, die dann nicht mehr aufrufbar sind.
# 
# 
# *D) Import aller Module aus der Bibliothek*
# 
# ```python
# from numpy import *
# 
# ```
# - Der Befehl bindet alle Objekte und Module von `numpy` direkt in den globalen Namensraum ein. Nun können alle Module direkt aufgerufen werden, also mittels: `cos()`, `sin()` oder `pi`. Dieser Import ist **nicht empfehlenswert**, da so die große Gefahr der Namenskollision besteht, und sollte daher nicht genutzt werden.
# 
# 
# *E) Import einzelner Module aus der Bibliothek mit Alias*
# 
# ```python
# import numpy.cos as cosin
# oder
# from numpy import cos as cosin
# 
# ```
# - Bei dieser Art des Imports wird nur jeweils das aufgerufene Modul der Bibliothek mit dem vorgegebenen Alias eingebunden. 
# 
# <br>
# 
# Durch das Importieren von externen Modulen kann man also die Funktionalität von Python erweitern. Jedes externe Modul sollte aber nur dann in das Projekt eingebunden werden, wenn dieses auch wirklich verwendet wird. Externe Module können dabei auch in anderen Programmiersprachen geschrieben sein. `numpy` zum Beispiel ist vorwiegend in *C* geschrieben.
# 
# Die in dem folgenden Einführungs-Notebook (0.2) verwendeten Module und deren Funktionen sind:
# - [```numpy```](https://numpy.org): für [Arrays und Matrizen](https://www.python-kurs.eu/numpy.php),
# - [```matplotlib```](https://matplotlib.org/contents.html): Erstellung von mathematischen Darstellungen,
# - [```scipy```](https://docs.scipy.org/doc/scipy/reference/): Nutzung wissenschaftlicher Funktionen.
#   
# 
# <br>
# 
# <h5>Installation von externen Modulen</h5>
# 
# Für die Installation von externen Modulen steht das Paketverwaltungsprogramm [`pip`](https://pip.pypa.io/en/stable/) zur Verfügung. Es lädt die Module aus dem [*Python Package Index (PyPI)*](https://pypi.org/) herunter, in dem die wichtigsten Projekte gelistet sind, und installiert diese. `pip` kümmert sich auch darum, bei Abhängigkeiten zu fehlenden Modulen diese automatisch mit zu installieren. Das Paketverwaltungsprogramm nutzt man direkt über die Eingabeaufforderung von Windows. Dabei ist zu beachten, dass Python nicht in derselben Eingabeaufforderung gestartet ist. Alle laufenden Python-Ausführungen können in anderen Eingabeaufforderungen weiterlaufen.
# 
# *Hinweis:* Falls Sie wegen mehreren installierten Python-Version auf den Python-Launcher zurückgreifen, müssen Sie bei allen im Folgenden beschriebenen Befehlen das `python` mit `py -3.X` ersetzen.
# 
# Mit `python -m pip -V` können Sie sich den Speicherort der pip-Version ausgeben lassen. Kontrollieren Sie, dass der richtige Pfad angezeigt wird, indem Sie die Python-Version installiert haben. Falls dies nicht der Fall ist, müssen Sie die Umgebungsvariablen editieren oder auf den Python Launcher `py` zurückgreifen (siehe dafür vorheriges Unterkapitel: Installation von Python).
# 
# Über den Befehl `python -m pip list` oder in einem Pythonkernel über `help("modules")` kann man sich eine Liste der installierten Module ausgeben lassen.
# 
# Bevor Sie Module installieren, sollte pip geupdated werden. Dies kann mit folgendem Befehl getan werden. <br>
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# python -m pip install --upgrade pip
# </div>
# 
# Zudem ist es sinnvoll, daraufhin das Modul [`wheel`](https://pypi.org/project/wheel/) zu installieren. Mit diesem Modul kann `pip` vorgepackte und -kompilierte Packages von PyPi herunterladen, was den Download und die Installation beschleunigt (siehe [Link für mehr Erklärung](https://realpython.com/python-wheels/)). Installiert wird `wheel` über  folgenden Befehl:<br>
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# python -m pip install wheel
# </div>
# 
# 
# 
# 1. **Installation von Numpy:** <br>
# Da [`numpy`](https://numpy.org/doc/stable/user/whatisnumpy.html) primär in *C* geschrieben ist, werden Libraries und Interpreter auf dem PC benötigt, um numpy zu installieren. Probieren Sie aber zuerst, die Installation mit folgendem Code zu starten.
# <br>
# Öffnen Sie eine eine Eingabeaufforderung und geben Sie folgenden Code ein und drücken `Enter`:<br>
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# python -m pip install numpy
# </div>
# 
#    Falls dies mit einem Fehler abbricht, liegt das wahrscheinlich daran, dass Sie die C-Libraries installieren müssen. Diese können Sie mit [C++-Buildtools](https://visualstudio.microsoft.com/de/visual-cpp-build-tools/) installieren. Wählen Sie nach Starten des Installationsassistenten im Installationsmenü *C++-Buildtools* aus. Hinweis: entfernen Sie keine Häkchen bei den vorausgewählten optionalen Modulen. Und ja, leider sind das um die 5 Gigabyte an Speicherplatz..<br>
# Danach geben Sie nochmal den obigen Code ein, um die Installation ein weiteres Mal zu starten. 
# 
# 
# 2.  **Installation von matplotlib:** <br>
#    Wenn `numpy` und `wheel` installiert sind, kann die Installation von [`matplotlib`](https://matplotlib.org/users/installing.html) über folgenden Befehl gestartet werden:<br>
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# python -m pip install matplotlib
# </div>
# 
#    Wenn Sie sich nun die Liste der installierten externen Module anschauen (`pip list`), wird Ihnen auffallen, dass durch die Installation von `matplotlib` noch weitere Module mit installiert wurden. Die sind automatisch mitinstalliert worden, da `matplotlib` sich auf diese bezieht.
# 
# 
# 3.  **Installation von scipy:** <br>
# `Scipy` auf einem Windows-Betriebssystem über den regulären Weg zu installieren [ist sehr aufwendig](https://scipy.org/install.html). Um diesen Aufwand zu umgehen, wird über den Dienst `wheel` eine vorgepackte Version heruntergeladen und installiert. Dies wird über folgenden Befehl gestartet:
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# python -m pip install scipy
# </div>
# 
#    Falls dies mit Fehlern endet, kann dies an folgenden Problemen liegen:
#     - das Package [`mkl`](https://pypi.org/project/mkl/) muss vorinstalliert werden.<br>
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# python -m pip install mkl
# </div><br>
# Starten Sie danach nochmal die Installation von `scipy`.
#     - Falls Sie die Pythonversion 3.9 installiert haben, kann das Wheel gegebenenfalls noch nicht zur Verfügung stehen. Dafür stehen Ihnen zwei Möglichkeiten zur Verfügung. Zum einen können Sie die Python-Version 3.8. installieren und darüber nochmal alle externen Module installieren, was wir Ihnen empfehlen.<br>
#     Zum anderen gibt es die Möglichkeit, sich kompilierte Binary-Dateien von anderen Anbietern zu downloaden und installieren. Eine Webseite mit solchen Binary-Dateien ist über [diesen Link zu finden](https://www.lfd.uci.edu/~gohlke/pythonlibs/). Um nun `scipy` darüber zu installieren, müssen Sie zunächst `numpy` und `mkl` deinstallieren und ein vorgepacktes .whl für `numpy + mkl` und eines für `scipy` herunterladen. Dazu müssen Sie aus den Listen die korrekten binary-Files aussuchen. [Hier die Liste für scipy mit einem Link zu numpy + mkl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy). Die Deinstallation der schon installierten Module und die Installation der lokalen `.whl` -Dateien folgt  über folgende Kommandos. Dabei müssen Sie den Pfad und den Dateinamen noch anpassen.<br>
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# python -m pip uninstall numpy<br>
# python -m pip uninstall mkl<br>
# python -m pip install C:\Users\~User\Downloads\numpy-1.19.2+mkl-cp3X-cp3X-win_amd64.whl<br>
# python -m pip install C:\Users\~User\Downloads\scipy-1.5.X-cp3X-cp3X-win_amdXX.whl
# </div>
# 
#       Diese Möglichkeit sollte aber immer nur als "letzte Option" gesehen werden, da es experimentelle binarys sind, und wird Ihnen in diesem Fall auch abgeraten. Falls Sie also (noch) nicht normal `scipy` installieren können, dann nutzen Sie lieber Python v3.8. Lassen Sie Python 3.9 aber einfach installiert und probieren Sie die Installation einfach ein paar Tage später aus. Vielleicht ist bis dahin ja ein wheel erstellt worden.
# 
# Eine Installation von mehreren Packages kann man auch mit nur einem `pip install`-Kommando durchführt, indem man die externen Pakete nacheinander schreibt. Zum Beispiel über: `python -m pip install wheel numpy matplotlib scipy`.
# 
# Nun sollten alle externen Module - bis auf Jupyter Notebook - auf Ihrem Computer installiert sein, die sie für das Einführungs-Notebook (0.2) benötigen. Falls Sie weitere Informationen benötigen, welche Möglichkeiten Ihnen bei der Installation und Update mit pip zur Verfügung stehen, können Sie sich noch folgende Links anschauen [(1)](https://packaging.python.org/tutorials/installing-packages/) [(2)](https://pip-python3.readthedocs.io/en/latest/reference/pip_install.html#pip-install-examples) [(3)](https://pip.pypa.io/en/latest/user_guide/#installing-from-wheels).
# 
# ***

# <a id='jupyter'></a><div><img src="img/IMG-jupyter.png" style="float:left"><h2 style="position: relative; top: 6px; left: 6px">3. Jupyter Notebook </h2></div>
# 
# `Jupyter Notebook` ist eine interaktive Computerumgebung, mit der Benutzer Notizbuchdokumente erstellen können, die Folgendes umfassen: - Live-Code - Interaktive Widgets - Diagramme - Erzähltext - Gleichungen - Bilder - Video usw.  
# Über die Kernel- und Messaging-Architektur von Jupyter ermöglicht das Notebook die Ausführung von Code in verschiedenen Programmiersprachen. Für jedes Notizbuchdokument (auch Notebook), das ein Benutzer öffnet, startet die Webanwendung einen Kernel, der den Code für dieses Notizbuch ausführt. Hier benutzen wir Python3 als Kernel.  
#     
# Folgende Informationen zum Umgang sind wichtig zu wissen:
# 
# - Der Aufbau ist in Zellen. Dabei kann eine Zelle zum Beispiel Pythoncode (```Code```) oder Text/Bilder (```Markdown```) beinhalten. 
# - Zellen mit Code können ausgeführt werden, indem man auf den Run-button klickt oder auf ```Umschalt``` + ```Enter```.
# - Auch Zellen mit Text können (wenn sie im Bearbeitungsmodus sind) mittels Run-Button oder ```Umschalt``` + ```Enter``` ausgeführt werden. 
# - Die Ergebnisse aller ausgeführten Zellen bleiben dabei gespeichert und können in der nächsten Zelle wieder verwendet werden.
# - Löschen der kompletten Ausgabe geht über das Menüband unter ```Kernel``` -> ```Restart & Clear All Output```.
# 
#     
# Weitere Hinweise zu dessen Verwendung finden Sie [hier](https://jupyter.org/index.html).
# 
# <br>
# 
# <h5>Installation von Jupyter Notebook</h5>
# 
# Zur Installation von [`Jupyter Notebook`](https://pypi.org/project/jupyter/) wird wieder `pip`verwendet. Nutzen Sie dafür folgendes Kommando:<br>
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# python -m pip install jupyter<br>
#    -- beziehungsweise --<br>
# py -3.X -m pip install jupyter
# </div><br>
# 
# Starten können sie `Jupyter Notebook` genau wie `python` oder `pip` über die Eingabeaufforderung von Windows mittels folgendem Kommando:<br>
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# jupyter notebook
# </div>
# 
# Daraufhin startet in der Eingabeaufforderung `Jupyter Notebook` und Ihr Standardbrowser öffnet sich mit dem Notebook-Fenster. Sie können das Programm auch mit einem anderen Browser verwenden, indem Sie den in der Eingabeaufforderung mit ausgegebenen http:\-Link nutzen.
# Wenn Sie nun im Browser ein oder mehrere Notebooks (`.ipynb`) öffnen, wird in der Eingabeaufforderung für jedes Notebook ein neuer Python-Kernel gestartet.
# 
# <br>
# 
# <h5>Hilfe bei mehreren Python-Versionen</h5>
# 
# Wenn Sie mehrere Python-Versionen installiert haben, können auch mehrere Python-Versionen den Kernel für die Notebooks stellen. Das Problem daran ist, dass der Kernel immer gleichnamig mit `python3` betitelt wird. Das sorgt dafür, dass es keine wirkliche Kontrolle gibt, welche Version gerade für den Kernel genutzt wird. Es wird in dieser Konfiguration meistens die Python-Version genommen, die im "PATH" zuerst kommt. Um eine Kontrolle über die Python-Kernel-Version einzurichten, können Sie folgende Befehle verwenden.
# 
# Zeigen Sie sich alle Kernelspezifikationen an über: 
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# jupyter kernelspec list
# </div>
# Diese Liste muss dabei nicht stimmen, da Namensdopplungen nicht angezeigt werden!
# 
# Installieren Sie weitere Kernelspezifikationen mit anderem Namen über folgenden Befehl (hier für Python 3.8):
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# py -3.8 -m ipykernel install --name python_3.8 --display-name "Python 3.8"
# </div>
# Wiederholen Sie das für alle Python-Versionen, die mit Jupyter Notebook verwendet werden sollen.
# 
# Sie können die nun redundant gewordene Spezifikation `python3` über folgenden Befehl löschen: 
# <div style="background-color:rgba(0, 0, 0, 0.0470588); padding:10px 10px;font-family:monospace;">
# jupyter kernelspec uninstall python3
# </div>
# 
# Wenn Sie dann ein Notebook geöffnet haben, können Sie über das Menüband unter `Kernel` -> `Change Kernel` die Python-Version auswählen, mit die der Kernel laufen soll. Auch können Sie bei einer Erstellung eines neuen Noteboks direkt auswählen, mit welchem Kernel dieser bei der Erstellung gestartet wird. Für die weitere Nutzung ist diese Auswahl aber irrelevant, da der Python-Code zwischen den Versionen zum großen Teil kompatibel ist.
# 
# ---
# 
# Falls Sie jetzt erfolgreich Python mit den externen Packages installieren konnten und Jupyter Notebook lokal nutzen können, sind Sie gewappnet für die nächsten Notebooks! Herzlichen Glückwunsch und viel Spaß mit den neu gewonnen Möglichkeiten durch ein frisch installiertes Python.
# 
# Melden Sie sich gerne, wenn Sie Anmerkungen zu dieser Anleitung haben.

# ---
# <div>Notebook erstellt von Arne-Lukas Fietkau, Yifei Li  und <a href="mailto:christoph.wagner@tu-dresden.de?Subject=Frage%20zu%20Jupyter%20Notebook%200.1%20Einführung" target="_top">Christoph Wagner</a></div>
