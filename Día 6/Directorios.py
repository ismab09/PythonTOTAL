import os
from pathlib import Path
#os.getcwd() *Sirve para mostrar la ruta o el lugar donde se ubica el archivo
#os.chdir() * Abre un archivo de otro lugar
#os.makedirs() * Creas una carpeta en la ruta elegida
#ruta = os.rmdir('C:\\Users\\Isma\\OneDrive\\Escritorio\\Nueva carpeta\\otra')
# en linux y mac se usa /



#os.path.basename * te muestra el nombre del archivo
#os.paht.dirname * te muestra la ruta del archivo
#os.paht.split * te muestra por separado las dos cosas
#os.rmdir * te borra una carpeta

carpeta = Path('C:\\Users\\Isma\\OneDrive\\Escritorio\\Nueva carpeta')
archivo1 = carpeta / 'otro archivo.txt'

archivo2 = open(archivo1)
print(archivo2.read())