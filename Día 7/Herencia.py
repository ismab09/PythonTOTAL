class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

class Pajaro(Animal):
    pass

#print(Animal.__subclasses__()) significa q muestra sus heredencias, mientras q __bases__ muestra sus bases

piolin = Pajaro(2,'blanco')

piolin.nacer()
print(piolin.color)