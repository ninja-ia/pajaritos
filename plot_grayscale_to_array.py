import cv2
import os

"""

1-Pasamos los plots a grayscale y los guardamos en una nueva carpeta (mejor sobreescribirlos probablemente)
2-Creamos 2 listas: lista_input con numpy.ndarrays para los plots y lista_outputs con strs para los nombres (en este caso género del pájaro)

*la lista_outputs SÓLO funciona para la base de datos https://avibase.bsc-eoc.org/

"""

try:
    os.mkdir("plots_grayscale")
except FileExistsError:
    pass

wd = os.getcwd()
files_folder = os.listdir(os.path.join(wd, 'plots'))
lista_inputs=[]
lista_outputs=[]

for file in files_folder:
    originalImage = cv2.imread(os.path.join(wd, 'plots', file))
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(wd, 'plots_grayscale', file), grayImage)
    lista_inputs.append(grayImage)
    lista_outputs.append(file.rsplit(' - ', 2)[1])

#uno de los nombres tiene ", a diferencia del resto que tiene ', no sé por qué
