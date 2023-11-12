class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):
    def __init__(self, edad, color, altura):
        super().__init__(edad, color)
        self.altura = altura

    def hablar(self):
        print('pio')

    def volar(self,metros):
        print(f'el pajaro vuela {metros} metros')


piolin = Pajaro(2,'blanco',60)

mi_animal = Animal
piolin.hablar()

# ----------------------------

class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('Ja Ja')

    def hablar(self):
        print('Buenas')

class Hijo(Padre, Madre): #hereda el primero
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()

mi_nieto.hablar()
print(Nieto.__mro__)