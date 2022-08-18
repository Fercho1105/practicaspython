#  ****TUPLAS******

# NO se pueden modificar a diferencia de las listas

#Ejemplo tupla siemore va en parentesis
vocales = ("a", "e", "i", "o", "u")


"""Esto de abajo, da error porque no se pueden modificar los valores o elementos de las tuplas"""
# vocales[2] = "I"

""" Concatenacion de los datos de tuplas"""
print(vocales[:3] + vocales[2:])  #Concatenamos los primeros 3 valores con ultimos 3 valores

print(vocales)

""" .index() en tuplas"""
print(vocales.index("o")) # Podemos seguir buscando indices en tuplas


""" Generar una lista a partir de una tupla con list()"""
lista_vocales = list(vocales)  # En una variable generamos una lista a partir de la tupla con list()

"""Modificacion de elementos ya generada la lista"""
lista_vocales[2] = "I"  #Ahora que generamos una lista, podemos modificar valores de ésta, pero la tupla sigue igual

print(lista_vocales)

"""Generar una tupla a partir de una lista con tuple()"""

tupla_vocales = tuple(lista_vocales)

print(tupla_vocales)















