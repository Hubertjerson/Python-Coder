
# 1) Identifica el tipo de dato (int, float, string, list o touple) de los
#   siguientes valores literales:

#valor1="Hola Mundo"
# type(valor1)

#valor2=[1, 10, 100]
# type(valor2)

# valor3=-25
# type(valor3)

#valor4=(8, 100, -12)
# type(valor4)

# valor5=1.167
# type(valor5)

#valor6=["Hola", "Mundo"]
# type(valor6)

#valor7=' '
# type(valor7)

#valor8=(1, -5, "Hola!")
# type(valor8)

# 2) Determina mentalmente (sin programar) el resultado que aparecerá
#   por pantalla a partir de las siguientes variables:

#a = 10
#b = -5
#c = "Hola"
#d = [1, 2, 3]
#e= (4,5,6)

#print(a * 5)
#print(a - b)
#print(c + "Mundo")
#print(c * 2)
# print(c[-1])
# print(c[1:])
#print(d + d)
# print(e[1])
# print(e+(7,8,9))

# 3) El siguiente código pretende realizar una media entre 3 números,
# pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?

# In [1]:

#numero_1 = 9

#numero_2 = 3

#numero_3 = 6

# ​media = numero_1 + numero_2 + numero_3 / 3

#print("La nota media es", media)

# La nota media es 14.0

# El problema es que estaba dividiendo el tercer número y luego sumaba ,
# al ponerle el paréntesis ahora sumará primero y luego pasará a dividir.

#numero_1 = 9
#numero_2 = 3
#numero_3 = 6

#media = (numero_1 + numero_2 + numero_3) / 3
#print("La nota media es : ", media)
# Codigo Corregido puede intentar Correrlo.


# 4) A partir del ejercicio anterior, desarrolla un programa para calcular la nota final.
#   Para ello vamos a suponer que cada número es una nota y que queremos obtener la nota media.
#   Cada nota tiene un valor porcentual:

# La primera nota vale un 15% del total

# La segunda nota vale un 35% del total

# La tercera nota vale un 50% del total

# Ejemplos:

#nota_1 = 10

#nota_2 = 7

#nota_3 = 4

# USANDO EL EJEMPLO
#nota_1 = 10
#nota_2 = 7
#nota_3 = 4

#total_nota1 = nota_1 * 0.15
#total_nota2 = nota_2 * 0.35
#total_nota3 = nota_3 * 0.5

#nota_final = total_nota1 + total_nota2 + total_nota3

#print('la nota final es : ', nota_final)

# DANDO LAS NOTAS EL USUARIO

#nota_1 = float(input('ingrese Primera Nota : '))
#nota_2 = float(input('ingrese Segunda Nota : '))
#nota_3 = float(input('ingrese Tercera Nota : '))

#total_nota1 = nota_1 * 0.15
#total_nota2 = nota_2 * 0.35
#total_nota3 = nota_3 * 0.5

#nota_final = total_nota1 + total_nota2 + total_nota3

#print('la nota final es : ', nota_final)


# 5) La siguiente matriz (o lista con listas anidadas) debe cumplir una condición:
# en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros.
# ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

# 🖐 Ayuda: La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

# Partirás de:

# matriz = [

#[1, 5, 1],
#[2, 1, 2],
#[3, 0, 1],
#[1, 4, 4]
# ]

# Debes llegar a:

# matriz = [

#[1, 5, 1, 7],
#[2, 1, 2, 5],
#[3, 0, 1, 4],
#[1, 4, 4, 9]
# ]


# RESPUESTA
#matriz = [
#    [1, 5, 1],
#    [2, 1, 2],
#    [3, 0, 1],
#    [1, 4, 4]
#]
#matriz[0].append(sum(matriz[0]))
#matriz[1].append(sum(matriz[1]))
#matriz[2].append(sum(matriz[2]))
#matriz[3].append(sum(matriz[3]))

#print(matriz)
