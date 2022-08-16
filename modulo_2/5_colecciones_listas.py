# #   //******LISTAS *****//
"""  "FOR" en listas  """
# mix = [0,1.0,"dos",3+4j]

# print(len(mix))  #Cantidad de elemnetos en la lista

# for i in mix:
#     print(f"{i:6} - Tipo:{type(i)}") #Imprimimos i y su tipo de dato
    
# sin_dos = mix[:2] + mix[3:]  #Sacamos los 2 primeros valores que estan antes de "dos" y de igualmanera sacamos el ultimo valor de la lista y las sumamos

# print(mix,sin_dos)

# duplicado = mix * 2 #Obtenemos la msima lista 2 veces en una misma 

# print(duplicado)

##############################################################

# #Sacamos el cuadrado de acuerdo al numero de elementos que hay en la lista.
# cuadrados=[0,1,4,9,16,25]

# for i in range(len(cuadrados)):
#     print(f"{i} ** 2 = {cuadrados[i]}")

# #Ahora sacamos el cubo
# cuadrados=[0,1,4,9,16,25]
# for i in range(len(cuadrados)):
#     cuadrados[i] = cuadrados[i] * i
#     print(f"Ahora están al cubo {cuadrados[i]}")

""" .append """

# cuadrados.append(7 ** 3) #Agrega el elemento al final de la lista

""" .insert """

# cuadrados.insert(6,6 ** 3)#Agrega un elemento en la posicion que nosotros indiquemos por medio de un indice , syntaxis:  .insert(posicion en la que queremos agregar,elemento a agregar)

""" .extend """

# cuadrados.extend([27 ,1000 , -1])   #Agrega múltiples valores al final de la lista mediante un iterable

# cuadrados.extend(range(-1, -4, -1))  

# print(cuadrados)

""" del lista"""

# del cuadrados[9:]  #funcion para eliminar elementos de la lista, en este caso desde el indice 9 en adelante

# print(cuadrados)

""" .remove """

# cuadrados.remove(27)  #remueve el valor con el que encuentre incidencia o igualdad, de la lista, de izq a derecha

# print(cuadrados)

""" .pop """

# valor_extraido = cuadrados.pop(2)  #Extrae el elemento del indice que le indiquemos, si no se le indica un indice, extrae el último elemento

# print(valor_extraido) #Guardamos el valor extraido en una variable

# print(cuadrados)

""" .clear """

# cuadrados.clear() #Elimina todos los elementos de la lista

# print(cuadrados)
##############################################################

""" ejemplos con las funciones"""

# vocales = ["a" , "e", "i", "o", "u"]

# vocales[1:4] = ["E", "I", "O"] #Reemplazamos del indice 1 al 3(porque el 4 no se cuenta) lo que pusimos entre corchetes, respectivamente

# print(vocales, len(vocales))

# vocales[1:4] = [] #Vaciamos de la posicion 1 a la 3

# print(vocales, len(vocales))

# vocales[1:2] = ["e", "i", "o" ,"u"] #Cambiamos los elementos de la posicion 1 a la 2, pero como solo hay dos valores, mete todos los valores dentro del rango del índice


# print(vocales, len(vocales))

# vocales.extend(["i", "i"]) #Agregamos una lista al final de la que ya teniamos

# print(vocales, len(vocales))

# print(vocales.index("i")) #Buscamos la primera "i" de la lista, es decir, su indice

# print(vocales.count("i")) # Vemos cuantas veces está repetido un elemento de la lista

# print(vocales.index("i",4)) #Buscaremos el indice de la primera "i" a partir de la posicion 4  | syntaxis .index(objeto a buscar, indice desde el cual buscaremos en adelante)

""" .reverse """

# vocales.reverse() #Revertimos la lista

# print(vocales, len(vocales))

""" .sort """

# vocales.sort() #Ordenamos la lista de manera ascendente, alfabéticamnete o numéricamente

# print(vocales, len(vocales))


##########################################################################

# carros = ["Audi", "Ford", "BMW", "VW"]

# carros.sort(key = len) #Ordenamos la lista con "key" que tiene como parametro la longitud de cada elemento, ordenandolo así de menor a mayor y alfabeticamente

# print(carros)


#################################################################################

""" listas dentro de listas """

# listas = [[0, 1], [2, 3, 4], [5, 6]]  #Podemos guardar listas en una lista

# print(listas[0], listas[1:3]) #Imrimimos las listas, en este caso, cada lista ocupa un indice

# #Ahora imprimiremos valores de las listas dentro de la lista 

# print(listas[2][1]) # syntaxis:  lista[numero de lista a usar][elemento de la lista a convocar]

#################################################################################


""" ID """

vocales1 = ["a" , "e", "i", "o", "u"]

vocales2 = vocales1 #Hacemos copia idéntica de nuetra lista

print(vocales1, vocales2)

print(id(vocales1),id(vocales2)) #Obtenemos el ID  de la lista, son iguales porque igualamos el objeto, duplicamos el mismo objeto

vocales3 = vocales1.copy() #Hacemos una copia de la vocales1 y la guardamos

print(id(vocales1),id(vocales3)) # Es diferente ID porque es diferente objeto, diferentes identificadores, ya que usamos la funcion copy

print(id(vocales1[2]), id(vocales2[2])) # Mismo ID porque es mismo objeto

print(id(vocales1[2]), id(vocales3[2])) # Mismo ID porque es mismo objeto

del vocales1[2]

print(vocales2, vocales3)

print(id(vocales1[2]), id(vocales3[3])) # El ID de la "o" es el mismo







