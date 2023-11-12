
#Forma larga
palabra = 'phyton'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

#Forma corta
lista = [letra for letra in 'phyton']

print(lista)

#con números
lista = [n / 2 if n * 2 > 10 else 'no' for n in range(0,21,2) ] #si queres
print(lista)

pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]
print(metros)