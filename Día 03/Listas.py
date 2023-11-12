lista = ["a","b","c"]
resultado = len(lista)
lista2 = ["hola", 43, 2.5]
resultado2 = lista2[0::2]
lista3 = lista+lista2
print(type(lista))
print(resultado)
print(resultado2)
print(lista+lista2)

#-------------------------------------------------------------------------------
lista3[0] = "alfa" #cambia
print(lista3)
#-------------------------------------------------------------------------------
lista3.append("5.0") #agrega
print(lista3)
#-------------------------------------------------------------------------------
lista3.pop()#quita (si no pones nada saca el último)
print(lista3)
#-------------------------------------------------------------------------------
eliminado = lista3.pop()#quita pero lo guarda
print(eliminado)
#-------------------------------------------------------------------------------
lista4 = ["g","o","b","m","c"]
lista4.sort()#los ordena alfabeticamente o numericamente
print(lista4)
#-------------------------------------------------------------------------------
lista5 = lista4.sort()#no tiene valor (none), no te devuelve nada
print(lista5)
#-------------------------------------------------------------------------------
lista4.reverse()#lo ordena para atras, de z a a y de infinito a 0
print(lista4)