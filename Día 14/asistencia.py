import cv2
import face_recognition as fr
import os
import numpy

# Crer base de datos
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}\\{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

# Codificar imagenes
def codificar(imagenes):

    # Crear una lista nueva
    lista_codificada = []

    # Pasar todas las imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        # Codificar
        codificado = fr.face_encodings(imagen)[0]

        # Agregar a la lista
        lista_codificada.append(codificado)

    # Devolver lista codificada
    return lista_codificada

lista_empleados_codificada = codificar(mis_imagenes)

# Tomar una imagen de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer imagen de la camara
exito, imagen = captura.read()

if not exito:
    print('No se ha podido tomar la captura')
else:

    # Reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    print(len(cara_captura))

    if len(cara_captura) == 0:
        cv2.imshow('Imagen web', imagen)
        cv2.waitKey(0)
        print('No se han distingido rostros en la imagen capturada')
    else:
        # Codificar cara capturada
        cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

        # Buscar coincidencias
        for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
            print('entre al for')
            coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
            distancias = fr.face_distance(lista_empleados_codificada, caracodif)

            print(distancias)

            indice_coincidencias = numpy.argmin(distancias)

            # Mostrar coincidencias si las hay
            if distancias[indice_coincidencias] > 0.6:
                print('No coincide')
            else:

                # Buscar nombre del pibe
                nombre = nombres_empleados[indice_coincidencias]

                # Mostrar la imagen
                cv2.imshow('Imagen web', imagen)

                # Mantener imagen abierta
                cv2.waitKey(0)



