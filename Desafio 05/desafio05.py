# 1) Realiza una función llamada area_rectangulo()
# que devuelva el área del rectángulo a partir de una base y una altura.
# Calcula el área de un rectángulo de 15 de base y 10 de altura

# def area_rectangulo(base, altura):
#    return base * altura

#print(area_rectangulo(15, 10))

# 2)Realiza una función llamada area_circulo() que devuelva
# el área de un círculo a partir de un radio.
# Calcula el área de un círculo de 5 de radio

# 🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y
# multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159
# como pi o importarlo del módulo math.

#from math import pi

# def area_circulo(radio):
#    return pi * radio**2

# print(area_circulo(5))

# 3) Realiza una función llamada relacion()
# que a partir de dos números cumpla lo siguiente:
# 1.-Si el primer número es mayor que el segundo, debe devolver 1.
# 2.-Si el primer número es menor que el segundo, debe devolver -1.
# 3.-Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

# def relacion(num1, num2):
#    if num1 > num2:
#        return 1
#    elif num1 < num2:
#        return -1
#    return 0


#print(relacion(5, 10), relacion(10, 5), relacion(5, 5))

# 4) Realiza una función llamada intermedio() que a partir de dos números,
# devuelva su punto intermedio:

# 🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números
# dividida entre 2

# Comprueba el punto intermedio entre -12 y 24

# def intermedio(num1, num2):
#    return (num1 + num2) / 2

#print(intermedio(-12, 24))

# 5) Realizá una función llamada recortar() que reciba tres parámetros.
# El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior.
# La función tendrá que cumplir lo siguiente:

# 1.-Devolver el límite inferior si el número es menor que éste
# 2.-Devolver el límite superior si el número es mayor que éste.
# 3.-Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10

# def recortar(num, lim_inf, lim_sup):
#    return max(min(num, lim_sup), lim_inf)

#print(recortar(-2, 0, 10))

# 6) Realiza una función separar() que tome una lista de números enteros y
# devuelva dos listas ordenadas. La primera con los números pares,
# y la segunda con los números impares:

# 🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()

# Por ejemplo:

#numeros = [-12, 84, 13, 20, -33, 101, 9]


# def separar(*args):
#    lista = sorted(args)
#    pares = []
#    impares = []
#    for arg in lista:
#        if arg % 2 == 0:
#            pares.append(arg)
#        else:
#            impares.append(arg)

#    return pares, impares


#pares, impares = separar(*numeros)
#print(pares)
#print(impares)
