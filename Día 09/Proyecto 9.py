import os
from datetime import datetime
import re
import time
import math

patron = r'N\w{3}-\d{5}'

directorio_raiz = 'dia9\\Mi_Gran_Directorio'


def busqueda(directorio):
    archivos_encontrados = 0

    for directorio_actual, directorios, archivos in os.walk(directorio):

        for archivo in archivos:
            ruta_archivo = os.path.join(directorio_actual, archivo)
            nombre_archivo = os.path.basename(ruta_archivo)

            with open(ruta_archivo, 'r') as archivo_actual:
                contenido = archivo_actual.read()
                busqueda = re.search(patron, contenido)
                if busqueda == None:
                    pass

                else:
                    archivos_encontrados += 1
                    print(f'{nombre_archivo}\t{busqueda.group()}')

    return archivos_encontrados


tiempo = datetime.today()

inicio = time.time()
print('-' * 45)
print(f'Fecha de busqueda: {tiempo}')
print('Archivo\t        NRO. SERIE\n----         \t----')

re = busqueda(directorio_raiz)
final = time.time()
duracion = final - inicio

print(f'Números econtrados: {re} ')
print(f'Duración de la busqueda: {math.ceil(duracion)}s')

print('-' * 45)
