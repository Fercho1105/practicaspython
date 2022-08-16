# #listas
# mix = [0,1.0,"dos",3+4j]

# print(len(mix))  #Cantidad de elemnetos en la lista

# for i in mix:
#     print(f"{i:6} - Tipo:{type(i)}")
    
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

# cuadrados.append(7 ** 3) #Agrega el elemento al final de la lista

# cuadrados.insert(6,6 ** 3)#Agrega un elemento en la posicion que nosotros indiquemos por medio de un indice , syntaxis:  .insert(posicion en la que queremos agregar,elemento a agregar)

# cuadrados.extend([27 ,1000 , -1])   #Agrega múltiples valores al final de la lista mediante un iterable

# cuadrados.extend(range(-1, -4, -1))  

# print(cuadrados)

# del cuadrados[9:]  #funcion para eliminar elementos de la lista, en este caso desde el indice 9 en adelante

# print(cuadrados)

# cuadrados.remove(27)  #remueve el valor con el que encuentre incidencia o igualdad, de la lista, de izq a derecha

# print(cuadrados)

# valor_extraido = cuadrados.pop(2)  #Extrae el elemento del indice que le indiquemos, si no se le indica un indice, extrae el último elemento

# print(valor_extraido) #Guardamos el valor extraido en una variable

# print(cuadrados)

# cuadrados.clear() #Elimina todos los elementos de la lista

# print(cuadrados)
##############################################################



