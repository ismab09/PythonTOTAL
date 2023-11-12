diccionario = {"clave1":"valor1","clave2":"valor2"}#diccionario = dict
print(diccionario)

resultado = diccionario["clave1"]
print(resultado)

#-------------------------------------------------------------------------------
cliente = {"nombre":"Ismael","apellido":"Benabare","matrícula":"sbg2985"}
consulta = (cliente["apellido"])
print(consulta)

#-------------------------------------------------------------------------------
dic = {"c1":55,"c2":[10,20,30],"c3":{"s1":100,"s2":200}}
print(dic["c3"]["s2"])
#puedo buscar por clave y si agrego otro corchete me busca el indice o si pongo la clave me la busca

#-------------------------------------------------------------------------------
dic2={"c1":["a","b","c"],"c2":["d","e","f"]}
print(dic2["c2"][1].upper())

#-------------------------------------------------------------------------------
dic2["c3"] = "g" #agrega
print(dic2)

#-------------------------------------------------------------------------------
dic2["c2"] = "h" #cambia
print(dic2)

#-------------------------------------------------------------------------------
print(dic2.keys())#muestra claves
print(dic2.values())#muestra valores)
print(dic.items())#muestra todos

