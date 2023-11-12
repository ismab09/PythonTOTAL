import cv2
import face_recognition as fr

# Cargar imagenes
foto_control = fr.load_image_file('foto_a.jpg')
foto_prueba = fr.load_image_file('foto_b.jpg')
foto_prueba = fr.load_image_file('foto_c.jpg')

# Pasar imagenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_a = fr.face_locations(foto_control)[0]
cara_codificada_a = fr.face_encodings(foto_control)[0]

# Localizar cara prueba
lugar_cara_b = fr.face_locations(foto_prueba)[0]
cara_codificada_b = fr.face_encodings(foto_prueba)[0]

# Mostrar rectangulos
cv2.rectangle(foto_prueba,
              (lugar_cara_b[3],lugar_cara_b[0]),
              (lugar_cara_b[1],lugar_cara_b[2]),
              (0, 255, 0),
              2)
cv2.rectangle(foto_control,
              (lugar_cara_a[3],lugar_cara_a[0]),
              (lugar_cara_a[1],lugar_cara_a[2]),
              (0, 255, 0),
              2)

# Realizar comparacion
resultado = fr.compare_faces([cara_codificada_a],cara_codificada_b,0.6)

print(resultado)




# Medida de la distancia
distancia = fr.face_distance([cara_codificada_a], cara_codificada_b)

print(distancia)

# Mostrar resultado
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)

# Mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# Mantener programa abierto
cv2.waitKey(0)




