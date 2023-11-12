def chequear_3_cifras(num):
    return num in range(100,1000)


resultado = chequear_3_cifras(78)
print(resultado)


def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass#esta mal poner return false porque sino no se fija en todos los resultados y solo en el primero

    return False
res = chequear_3_cifras([55,99,66])
print(res)

def chequear_2_cifras(lista):

    lista3 = []
    for n in lista:
        if n in range(10,100):
            lista3.append(n)
        else:
            pass#esta mal poner return false porque sino no se fija en todos los resultados y solo en el primero

    return lista3
resu = chequear_2_cifras([55,99,6])
print(resu)