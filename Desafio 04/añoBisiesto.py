def añoBisiesto(valor):
    for digito in valor:
        if digito in '0123456789':
            continue
        else:
            print('Solo acepto numeros.')
            return True

    if int(valor) % 4 == 0 and (not(int(valor) % 100 == 0) or int(valor) % 400 == 0):
        print('El año si es bisiesto')
    else:
        print('El año no es bisiesto')
    return False


error = True
while error:
    error = añoBisiesto(input('ingresame un valor numerico: '))
