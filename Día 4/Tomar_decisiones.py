if 10 > 9:
    print('Es correcto')
else:
    print('No es correcto')

mascota = 'perro'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No se qué animal tienes')

edad = 16
calificacion = 12

if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 6:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')