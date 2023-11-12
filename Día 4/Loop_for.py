lista = ['a','b','c','d']

for letra in lista:
    print('Letra:' + letra) #no importa que nombre le pongas a la variable interior (siempre funciona pero no siempre es legible
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

#-----------------------------------------------------------------------------------------------------------------------------------------------------

lista2 = ['pablo','laura','fede','luis','julia']

for nombre in lista2:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que o comienza con L')

#-----------------------------------------------------------------------------------------------------------------------------------------------------

numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero

    print(mi_valor) #si pones tabulacion el resultado es por cada numero  si no es al terminar de pasar por todos los numeros

#-----------------------------------------------------------------------------------------------------------------------------------------------------

for letra in 'python':
    print(letra)
