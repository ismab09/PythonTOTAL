class Pajaro:

    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro('Negro','Halcón')

palabra = 'hola'

print(mi_pajaro.color + ' - ' + mi_pajaro.especie)
print(Pajaro.alas)
print(mi_pajaro.alas)