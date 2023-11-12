from random import randint

estimado = 0
intentos = 0
numero_secreto = randint(1,100)

nombre = input('Dime tu nombre: ')

print(f'Bueno {nombre}, he pensado un número entre número 1 y 100\nTienes 8 intentos para adivinar')

while intentos < 8:
    estimado = int(input('¿Cuál es el número?: '))
    intentos += 1

    if estimado not in range (1,101):
        print ("Tú número no se encuentra en el rango")
    if estimado > numero_secreto:
        print ("Mi número es más bajo")
    elif estimado < numero_secreto:
        print ("Mi número es más alto")
    else:
        print (f"Felicitaciones {nombre}!! Has logrado adivinar el número en {intentos} intentos")
        break

if estimado != numero_secreto:
    print (f"Has perdido, el número secreto era {numero_secreto}")
