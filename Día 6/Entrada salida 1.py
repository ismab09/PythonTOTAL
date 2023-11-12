mi_archivo = open('prueba.txt')
print (mi_archivo) #muesta lo siguiente: <_io.TextIOWrapper name='prueba.txt' mode='r' encoding='cp1252'>

readline = (mi_archivo.readline()) #muestra una linea # si lo repito puedo ver las otras lineas
para_mostrar_todo_el_texto = mi_archivo.read()#te muestra el texto

#.rstrip sirve para q no aparezca el salto de linea

me = mi_archivo.readlines()

mi_archivo.close() #lo cierra

