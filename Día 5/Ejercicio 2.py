def letras_ordenadas(palabra):

    set1 = set()

    for letra in palabra:
        set1.add(letra)

    lista = list(set1)
    lista.sort()

    return lista


print(letras_ordenadas('entretenido'))