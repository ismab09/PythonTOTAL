mi_tuple = (1,2,3,4)
print(type(mi_tuple))



t = (5,5.6,"f")
print(t[-2])


y = (1,2,(10,20),4)
print(y[2][1])

y = list(y)
print(type(y))


print("---------------------------------------------")
#-----------------------------------------------
h = (1,2,3)
x,y,z = h
print(x,y,z)
#-----------------------------------------------
s = (1,2,3,1)
print(len(s))
print(s.count(1)) #pregunta cuantas veces aparece
print(s.index(2)) #pregunta su posición