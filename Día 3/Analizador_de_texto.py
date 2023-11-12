texto = input("Ingresa un texto a elección: ")
letras = []

texto = texto.upper()

letras.append(input("Ingresa una letra: ").upper())
letras.append(input("Ingresa otra letra: ").upper())
letras.append(input("Ingresa una última letra: ").upper())

print("\n") #alt92 para la barra invertida
print("CANTIDAD DE LETRAS")
cantidad_de_letras1 = texto.count(letras[0])
cantidad_de_letras2 = texto.count(letras[1])
cantidad_de_letras3 = texto.count(letras[2])

print(f'En el texto colocado, la letra "{letras[0]}" está repetida {cantidad_de_letras1} vez/veces')
print(f'En el texto colocado, la letra "{letras[1]}" está repetida {cantidad_de_letras2} vez/veces')
print(f'En el texto colocado, la letra "{letras[2]}" está repetida {cantidad_de_letras3} vez/veces')

print("\n") #alt92 para la barra invertida
print("CANTIDAD DE PALABRAS")
palabras = texto.split() #sino pones nada dentro de los parentesis lo va a separar en palabras
print(f"En tu texto se encuentran {len(palabras)} palabras")

print("\n") #alt92 para la barra invertida
print("LETRAS DE INICIO Y DE FINAL")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f'La letra inicial de tu texto es "{letra_inicio}" y la letra final es "{letra_final}"')

print("\n") #alt92 para la barra invertida
print("TEXTO INVERTIDO EN PALABRAS")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f'Si ordenamos tu texto al revés este va a estar de la siguiente manera: "{texto_invertido}"')

print("\n") #alt92 para la barra invertida
print("BUSCA PALABRAS")
buscapalabras = input("Coloca una palabra en mayúscula para buscarla: ")
busca_palabras = buscapalabras in texto
dic = {True:"si", False:"no"}
print(f'La palabra "{buscapalabras}" {dic[busca_palabras]} se encuentra en tu texto')

#Uno no es lo que es por lo que escribe, sino por lo que ha leído