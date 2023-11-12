from random import choice

#me faltan congo, republica democratica del congo, República Centroafricana, República Checa / Chequia, Myanmar
paises = ['afganistan','albania','alemania','andorra','angola','antigua y barbuda','arabia saudita','argelia','argentina','armenia','australia','austria','azerbaiyan','bahamas','bangladesh','barbados','barein','belgica','belice','bielorrusia','benin','bolivia','bosnia y herzegovina','botsuana','brasil','brunei','bulgaria','burkina faso','burundi','butan','cabo verde','camboya','camerun','canada','catar','chad','chile','china','chipre','colombia','comoras','corea del norte','corea del sur','costa de marfil','costa rica','croacia','cuba']
letras_adivinadas = []
letras_falladas = []
vidas = 7
aciertos = 0
juego_terminado = False


def elegir_palabra(lista_paises):
    palabra_elegida = choice(lista_paises)
    largo_palabra = len(set(palabra_elegida))

    return palabra_elegida, largo_palabra



def pedir_letras():
    letra_elegida = ''
    validez = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not validez:
        letra_elegida = input('Elige una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) ==1:
            validez = True
        elif letra_elegida in abecedario and len(letra_elegida) > 1:
            print('Elige solamente una letra')
        else:
            print('Solo se aceptan letras, por favor no ingresar números ni palabras ni símbolos')

    return letra_elegida


def mostrar_guiones(palabra_elegida):

    lista_palabra_oculta = []
    for letra in palabra_elegida:
        if letra in letras_adivinadas:
            lista_palabra_oculta.append(letra)
        else:
            lista_palabra_oculta.append('-')

    print(' '.join(lista_palabra_oculta))


def chequeo(letra_elegida,lista_palabra_oculta,vidas,coincidencias):
    final = False

    if letra_elegida in lista_palabra_oculta and letra_elegida not in letras_adivinadas:
        letras_adivinadas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in lista_palabra_oculta and letra_elegida in letras_adivinadas:
        print('Esta letra ya la has dicho, intenta con otra')
    else:
        vidas -= 1
        letras_falladas.append(letra_elegida)


    if vidas == 0:
        final = perder()
    elif coincidencias == largo_palabra:
        final = ganar(lista_palabra_oculta)

    return vidas, final, coincidencias


def perder():
    print(f'Has perdido, la palabra era: ' + palabra)

    return True
def ganar(palabra_encontrada):
    mostrar_guiones(palabra_encontrada)
    print('Felicidades, has ganado!!')

    return True



print('Bienvenido al ahorcado de paises, en este juego tendrás que adivinar el pais, ¡Comenzemos!')

print('No están en la lista: Taiwan y Kosovo')

palabra, largo_palabra = elegir_palabra(paises)
while not juego_terminado:
    mostrar_guiones(palabra)
    print('Letras incorrectas: ' + '-'.join(letras_falladas))
    letra = pedir_letras()
    vidas, terminado, aciertos = chequeo(letra, palabra, vidas, aciertos)
    print(f'Vidas: {vidas}')
    juego_terminado = terminado