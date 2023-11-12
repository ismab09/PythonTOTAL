#13%
nombre = input("¿Cuál es tu nombre?")
ventas = int(input("¿Cuánto haz vendido este mes?"))

respuesta = round(ventas * 13 / 100,2)

print(f"Hola  {nombre} , este mes haz cobrado $ {respuesta}")
