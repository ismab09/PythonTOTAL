from random import randint

aleatorio = randint(1,100)
print(aleatorio)

from random import *

aleatorio = round(uniform(1,100),2) #se pone el round para elegir la cantidad de decimales
print(aleatorio)

aleatorio = random() #es bueno para trabajar con fracciones o porcentajes
print(aleatorio)

colores = ['azul','rojo','verde','amarillo','violeta','naranja']
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(0,100,10))
shuffle(numeros)
print(numeros)