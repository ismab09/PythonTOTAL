texto = "Este es el MEJOR texto del mundo"

#Upper
resultado = texto[2].upper()
print(resultado)

#Lower
resultado = texto.lower()
print(resultado)

#Split
resultado = texto.split("t") #si pongo una letra el criterio de separación va a ser cada vez que encuentre una letra
print(resultado)

#Join
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = "-".join([a,b,c,d])
print(e)

#Find
resultado = texto.find("s")#busca una letra, y si esta no existe te pone un -1.
print(resultado)

#Replace
resultado = texto.replace("mundo","universo") #puede replazar palabras y letras, si pongo una me cambiará todas.
print(resultado)