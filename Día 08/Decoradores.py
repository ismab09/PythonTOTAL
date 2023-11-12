def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')
    return otra_funcion

@decorar_saludo
def mayusculas(texto):
    print(texto.upper())

@decorar_saludo
def minusculas(texto):
    print(texto.lower())



minusculas('PyThOn')

mayuscula_decorada = decorar_saludo(mayusculas)
mayuscula_decorada('isma')