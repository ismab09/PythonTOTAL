# -------------------------------------------------------
#Implicitas
num1 = 43
num2 = 49.74

num1 = num1 + num2

print(type(num1))
print(type(num2))

# -------------------------------------------------------
#Explicitas
#Cuando los float los cambias a int solo elimina los decimales no lo aproxima

num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1)

print(num2)
print(type(num2))

num1 = "7.5"
num2 = "10"

# -------------------------------------------------------

edad = input("Dime tu edad: ")
print(type(edad))

edad = int(edad)
print(type(edad))

nueva_edad = 1 + edad
print(nueva_edad)



