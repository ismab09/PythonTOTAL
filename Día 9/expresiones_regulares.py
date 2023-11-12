import re

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

patron = 'ayuda'

busqueda = re.search(patron, texto)
print(busqueda) #si ponemos .span vamos a ver la ubicación de la palabra encontrada
#.start ubicacion inicial .end ubicacion final

busqueda = re.findall(patron, texto)
print(busqueda)
print(len(busqueda))
for hallazgo in re.finditer(patron ,texto):
    print(hallazgo.span())

texto1 = 'Llama al 564-525-6588 ya mismo'
patron1 = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron1, texto1)

print(resultado)
print(resultado.group())

patron1 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron1, texto1)
print(resultado.group(2))


clave = input('Clave: ')
patron2 = r'\D{1}\w{7}'
chequear = re.search(patron2, clave)
print(chequear)

texto2 = 'no atendemos los lunes por la tarde'

buscar = re.search(r'lunes|martes', texto2)
print(buscar)
buscar = re.search(r'....demos....', texto2)
print(buscar)
buscar = re.search(r'^\D$', texto2)
print(buscar)
buscar = re.findall(r'[^\s]+', texto2)
print(buscar)
buscar = re.findall(r'[^\s]+', texto2)
print(''.join(buscar))