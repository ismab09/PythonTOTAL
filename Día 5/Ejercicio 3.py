def funcion (*args):

    cuenta = 0

    for num in args:

        if cuenta + 1 == len(args):
            return False
        elif args[cuenta] ==0 and args[cuenta + 1] == 0:
            return True
        else:
            cuenta += 1

    return False


print(funcion(0,5,6,7,8,9,1,0))