# # ****CONJUNTOS****
"""A diferencia de los demas, no posee un orden ni un indice, nunca se repiten datos"""

"""EJEMPLO DE UN CONJUNTO"""

# canasta = {'manzana', 'naranja', 'manzana', 'pera', 'naranja', 'platano'}

# print(canasta) #Vemos que no imprime en pantalla los elementos repetidos, y no hay orden

# print('manzana' in  canasta) # Vemos si esta el valor de manzana, ya que se repite 2 veces


# print('melon' in  canasta) # Vemos si esta el valor de melon, pero en este caso es falso


#######################################################################################

"""FUNCIONES EN CONJUNTOS"""

# vocales = ["a", "e", "i", "o", "u", "a"]

# print(vocales)


""" set() """
# vocales = list(set(vocales)) #Convertimos la lista en conjunto para eliminar elementos repetidos, y ese conjunto lo guardamos 


# print(vocales)

#######################################################################################

# vocales = {"a", "e", "i", "o", "u", "a"}

# vocales2 = { "e", "i", "o"}

""" .issubset() """
# print(vocales2.issubset(vocales))  #Con esta funcion sabemos si si un conjunto, es un subconjunto de un conjunto  | syntaxis posibleSubconjunto.issubset(conjunto principal )

#######################################################################################

"""OPERADORES EN CONJUNTOS"""


vocales = {"a", "e", "i", "o", "u", "a"}

vocales2 = { "A", "E", "I", "O", "U", "u"}


print(vocales - vocales2) # Imprimimos la diferencia entre ambos conjuntos, pero dado que son valores son diferentes en ambos conjuntos, no hay diferencia (no se efectua la resta)


print(vocales | vocales2) #Ahora unimos ambos conjuntos con " | "


print(vocales & vocales2) # Sacamos la interseccion de los conjuntos con " & "


print(vocales ^ vocales2) # Sacamos los valores que no se repiten en los conjuntos










