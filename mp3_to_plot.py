import os
import librosa
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import warnings

"""

1- creamos una carpeta para los plots, si no existe
2- accedemos a los archivos de la carpeta mp3 (debería tener sólo archivos de canto de pájaros, pero podría tener cualquier otra cosa, o en un formato distinto que no abordamos todavía -ej. .wav-)
3- buscamos archivos .mp3 en la carpeta mp3
4- cargamos el archivo (establecemos el samplig rate -samples por seg- y recortamos el tiempo que vamos a registar -4 seg-) -> otra opción es que se repita el registro hasta llegar a un duration de X seg mayor.
5- filtramos los archivos que duren menos de 4 seg
6- hacemos un plot de amplitud vs tiempo y lo guardamos en la carpeta plots

"""

try:
    os.mkdir("plots")
except FileExistsError:
    pass

wd = os.getcwd()
files_folder = os.listdir(os.path.join(wd, 'mp3'))
warnings.filterwarnings("ignore", message="PySoundFile failed. Trying audioread instead")

for file in files_folder:
    if os.path.splitext(file)[1][1:] == "mp3":
        mp3_file = os.path.join(wd, 'mp3', file)
        duration=4
        amplitud, sr = librosa.load(mp3_file, sr=40000, duration=duration)
        if amplitud.shape[0] >= duration*sr:
            time = np.arange(0,len(amplitud))/sr
            plt.plot(time,amplitud)
            plt.axis('off')
            plt.savefig(os.path.join(wd, "plots/", file[:-4]))
            plt.close("all")
