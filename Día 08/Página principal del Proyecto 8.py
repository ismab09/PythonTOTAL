import numeros_del_proyecto_8

def preguntar():


    while True:
        print('[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética')
        try:
            mi_rubro = input('Elija su rubro: ').upper()
            ['P','F','C'].index(mi_rubro)
        except ValueError:
            print('Esa no es una opción válida')
        else:
            break

    numeros_del_proyecto_8.decorador(mi_rubro)


def inicio():
    print('Bienvenido a la Farmacia Python')
    while True:

        preguntar()
        otro_turno = 'SD'

        while (otro_turno != 'NO' or otro_turno != 'SI') :
            try:
                otro_turno = input('¿Quieres sacar otro número? [SI] [NO]').upper()
                ['SI','NO'].index(otro_turno)
            except ValueError:
                print('Esa no es una opción válida')
            else:
                if otro_turno == 'NO':
                    print('Gracias por su visita')
                    print('\n' +'-' * 23 + '\n')
                    print('Bienvenido a la Farmacia Python')
                    break
                else:
                    break


inicio()