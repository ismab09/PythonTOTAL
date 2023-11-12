def suma():
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    print(n1 + n2)
    print('Gracias por sumar')




try:
    # Código que queremos probar
    suma()
except TypeError:
    # Código a ejecutar si no hay un error
    print('Estás intentando concatenar tipos distintos')
except ValueError:
    print('Ese no es un número')
else:
    # Código a ejecutar si no hay un error
    print('Hiciste todo bien')
finally:
    # Código que se va a ejecutar de todos modos
    print('Eso fue todo')

def pedir_numero():

    while True:
        try:
            numero = int(input('Dame un numero: '))
        except:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste el numero {numero}')
            break
    print('Gracias')

pedir_numero()