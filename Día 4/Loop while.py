monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1 #esto es igual a poner monedas = monedas - 1
else:
    print('No tengo más dinero')

#--------------------------------------------------------------------------------------------------

respuesta = 's'
while respuesta == 's':
    respuesta = input("quieres seguir? (s/n)")
else:
    print("gracias")

# --------------------------------------------------------------------------------------------------

while respuesta == 'h':
    pass #salta el while
nombre = input('Dime tu nombre: ')
for letra in nombre:
    if letra == 'r':
        break #interrumpe y el programa termina
    print(letra)

apellido = input('Dime tu apellido: ')
for letra in apellido:
    if letra == 'r':
        continue  # interrumpe y el programa continua
    print(letra)

