import datetime
from datetime import datetime
from datetime import date

#mi_hora = datetime.time(17, 35)
#print(mi_hora)#puedo poner mi_hora.minute y me muestra los minutos, lo mismo con horas, etc.


#mi_dia = datetime.date(2028, 6, 26)
#print(mi_dia.ctime())#puedo poner mi_hora.year y me muestra el año, lo mismo con dias, etc.
#el ctime te muestra tmb el dia de la semana y la hora
#print(mi_dia.today())#te muestra la fecha actual
#from datetime import date -> hoy = date.today()


mi_fecha = datetime(2025,5,15,22,10,15,2500)

print(mi_fecha)

mi_fecha = mi_fecha.replace(month = 11)

print(mi_fecha)


nacimiento = date(1995,3,5)
fallecimineto = date(2095,6,19)

vida = fallecimineto - nacimiento

print(f'Esta persona ha vivido {vida} ')

despierta = datetime(2002,10,5,7,30)
duerme = datetime(2002,10,5,23,45)

despierto = duerme - despierta
print(despierto)