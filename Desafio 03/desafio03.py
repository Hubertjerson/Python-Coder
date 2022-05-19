# 1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:

# 1-Mostrar una suma de los dos números
# 2-Mostrar una resta de los dos números (el primero menos el segundo)
# 3-Mostrar una multiplicación de los dos números
# 4-Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
# 5-En caso de no introducir una opción válida, el programa informará de que no es correcta.

# OPCION 01
#n1 = float(input("Introduce un número: "))
#n2 = float(input("Introduce otro número: "))
#opcion = 0

#print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos númerosn\n4)finalizar programa")
#opcion = int(input("Introduce un número: "))

# if opcion == 1:
#    print("La suma de", n1, "+", n2, "es", n1+n2)
# elif opcion == 2:
#    print("La resta de", n1, "-", n2, "es", n1-n2)
# elif opcion == 3:
#    print("El producto de", n1, "*", n2, "es", n1*n2)
# elif opcion == 4:
#    print("Hasta la proxima")
# else:
#    print("Opción incorrecta")

# OPCION 02

#n1 = float(input("Introduce un número: ") )
#n2 = float(input("Introduce otro número: ") )
#opcion = 0

#print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números\n4)finalizar programa")
#opcion = int(input("Introduce un número: ") )

# while True:
#     if opcion == 1:
#        print("La suma de",n1,"+",n2,"es",n1+n2)
#        break
#     elif opcion == 2:
#        print("La resta de",n1,"-",n2,"es",n1-n2)
#        break
#     elif opcion == 3:
#        print("El producto de",n1,"*",n2,"es",n1*n2)
#        break
#     elif opcion == 4:
#        print("Hasta la próxima")
#        break
#     else:
#        print("Opción incorrecta")
#        break

# 2) Escribí un programa que lea un número impar por teclado.
#    Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

#numero = 0
# while numero % 2 == 0:
#    numero = int(input("Introduce un número impar: ") )


# 3) Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

# 🖐 Ayuda: Podes utilizar la funciones sum() y range() para hacerlo más fácil.
# El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

#suma = sum( range(1, 100, 2) )
# print(suma)

# 4) Escribí un programa que pida al usuario cuantos números quiere introducir.
#   Luego lee todos los números y realiza una media aritmética:

#suma = 0
#numeros = int(input("¿Cuántos números quieres introducir? ") )
# for x in range(numeros):
#    suma += float(input("Introduce un número: ") )
#print("Se han introducido",numeros,"números que en total han sumado",suma,"y la media es",suma/numeros)

# 5) Escribí un programa que pida al usuario un número entero del 0 al 9,
#   y que mientras el número no sea correcto se repita el proceso.
#   Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

# 🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente
#   si un valor se encuentra en una lista (devuelve True o False)

#numeros = [1, 3, 6, 9]

# while True:
#    numero = int(input("Escribe un número del 0 al 9: "))
#    if numero >= 0 and numero <= 9:
#        break
# if numero in numeros:
#    print("El número",numero,"se encuentra en la lista",numeros)
# else:
#    print("El número",numero,"no se encuentra en la lista",numeros)

# 6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

#print( list( range( 0, 11 ) ) )
#print( list( range( -10, 1 ) ) )
#print( list( range( 0, 21, 2 ) ) )
#print( list( range( -19, 0, 2 ) ) )
#print( list( range( 0, 51, 5 ) ) )

# 7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas,
#   pero no debe repetirse ningún elemento en la nueva lista:

#lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
#lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

#lista_3 = []
#
# for letra in lista_1:
#    if letra in lista_2 and letra not in lista_3:
#        lista_3.append(letra)

# print(lista_3)
