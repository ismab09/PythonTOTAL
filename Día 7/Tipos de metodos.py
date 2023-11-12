class Pajaro:

    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio pio, mi color es {}'.format(self.color))

    def volar(self,metros):
        print(f'El pajaron ha volado {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    @classmethod #no pueden acceder a los atributos de instancia
    def poner_huevos(cls,cantidad): #pero si podes acceder a los atributos de clase
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod  #no pueden acceder a los atributos de instancia ni a los de clase
    def mirar():
        print('El pajaro mira')



piolin = Pajaro('amarillo','canario')

piolin.pintar_negro()
piolin.volar(23)
print(piolin.alas)

Pajaro.poner_huevos(4) #no puedo ejecutarlo con un metodo de instancia, pues necesita un argumento posicional, self

Pajaro.mirar()