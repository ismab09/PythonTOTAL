
mi_texto = "Hola, ¿cómo estás?"
resultado = mi_texto[-6]
print(resultado)
#entre las llaves podemos poner números naturales (positivos) y negativos


#otra opción, con el index
resultado = mi_texto.index("o")
print(resultado)
#si buscas una letra repetida te aparece la primera desde la izquierda


#podemos decirle que comienze a contar después  que termine o sin fin
resultado = mi_texto.index("o",5,11)
print(resultado)
#si ponemos que busque una o no aparecerá si esta tiene tilde


#la siguiente sirve para que la búsqueda sea desde la derecha hacía la izquierda
resultado = mi_texto.rindex("o")
print(resultado)
#también podemos poner palabras enteras y te indicará cuando empieza esta.