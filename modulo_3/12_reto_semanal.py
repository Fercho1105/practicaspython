import m_retosemanal as m3 # Se importa el módulo m_reto3

Numero_de_listas = int(input("¿Cuántas listas desea crear?: ")) # se pide el número de listas a crear
listas = [] # Se crea una lista vacía

for i in range(Numero_de_listas) : # Se recorre el número de veces que se le indique
    listas.append([]) # se agrega una lista vacía a la lista
    longitud = int(input(f"¿ Cuántos elementos desea crear en la lista { i + 1 }? ")) # Se pide la longitud de la lista
    listas[i] = m3.crear_lista(listas[i] ,longitud) # se llama a la función crear lista pasando como parámetros la lista y la longitud

for i in listas : # Recorre la lista
    print(f'La lista {listas.index(i) + 1} original es : {i}') # Imprime la lista

for i in listas : # Recorre la lista
    for j in listas : # Recorre la lista
        if i != j : # Si la lista i no es igual a la lista j
            i = m3.eliminar_lista(i,j) # se llama a la función eliminar lista pasando como parámetros la lista i y la lista j

print ( ' Después de eliminar las listas repetidas : ' ) # Imprime el mensaje
for i in listas : # Recorre la lista
    print ( i ) # Imprime la lista