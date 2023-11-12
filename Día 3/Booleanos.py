#> mayor que
#< menor que
#>= mayor o igual que
#<= menor o igual que
#== igual que
#!= diferente que

var1 = True #siempre la t y la f tienen que estar en mayúscula
var2 = False
print(type(var1))
print(var1)

print("--------------------------------------------")

numero = 5 > 2+4
print(type(numero))
print(numero)

print("--------------------------------------------")

numero5 = 5 == 2+3
print(type(numero5))
print(numero5)

print("--------------------------------------------")

numero6 = 5 != 2+3
print(type(numero6))
print(numero6)

print("--------------------------------------------")

numero7 = bool(5<6)
print(type(numero7))
print(numero7)

print("--------------------------------------------")

numero8 = bool()
print(type(numero8))
print(numero8)

print("--------------------------------------------")

lista = [1,2,3,4]
control = 4 in lista
print(type(control))
print(control)

