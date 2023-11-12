print('\n------------- \n ')
#Opción 1
menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)
print(menor)
print(mayor)

print('\n------------- \n ')
#Opción 2
lista = [58,96,72,64,35]
print(f'El menor número es {min(lista)} y el mayor es {max(lista)}')

print('\n------------- \n ')
#Opción 3
nombres = ['Juan','Pablo','Alicia','Carlos']

print(min(nombres)) #Busca primero las mayúsculas, para arreglarlo podemos poner .lower si es que hay solo un string

print('\n------------- \n ')
#Opción 4
dic = {'C1':45,'C2':11}
print(min(dic)) #se fija en la clave con valor inferior y si queremos el valor ponemos .value
