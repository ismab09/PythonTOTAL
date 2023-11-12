import time
import timeit

def prueba_f(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time()
prueba_f(1000000)
final = time.time()
print(final-inicio)

inicio = time.time()
prueba_while(1000000)
final = time.time()
print(final-inicio)


declaracion = '''
def prueba_f(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

'''

mi_setup = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''


duracion = timeit.timeit(declaracion, mi_setup, number = 999900000)
print(duracion)