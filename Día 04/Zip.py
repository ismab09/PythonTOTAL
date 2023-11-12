nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Madrid','Montevideo']

combinados = list(zip(nombres,edades,ciudades)) #sino pongo como lista no funcionará
print(combinados) #llega hasta el largo de la lista más corta

for nombres,edades,ciudades in combinados:
    print(f"{nombres} tiene {edades} años y vive en {ciudades}")
