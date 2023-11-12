#SIN ENUMERADOR

lista = [1,2,3]
indice = 0

for item in lista:
    print(indice,item)
    indice += 1


#CON ENUMERADOR

lista = ["a","b","c"]

for ite in enumerate(lista):
    print(ite)

#--------------#

lista = ["a","b","c"]

for indice,ite in enumerate(lista):
    print(indice,ite)

#--------------#

lista = ["a","b","c"]

for indice,ite in enumerate(range(50,55)):
    print(indice,ite)

lista = ["a", "b", "c"]

tuples = list(enumerate(lista))
print(tuples[1][0])