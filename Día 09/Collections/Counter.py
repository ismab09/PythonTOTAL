from collections import Counter

#Counter

numeros = [8,6,9,3,2,5,4,5,2,3,1,2,3,5,8,9,7,5,6]
frase = 'al pan pan y al vino vino'

#con números
print(Counter(numeros))

#con letras
print(Counter('mississippi'))

#con palabras
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,4])
print(serie.most_common()) #si dentro del parentesis pongo un número PE: 3 me va a mostrar desde el primero hasta el tercer número más repetido
print(list(serie)) #obtengo los elementos únicos de la lista
