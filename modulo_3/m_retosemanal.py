def crear_lista(lista,longitud) : # Crea una lista de palabras de una longitud determinada
    """Crea una lista de una longitud determinada """ # Recibe una lista y una longitud
    for i in range(longitud) : # Crea una lista de palabras de una longitud determinada
        elemento = input (f" Ingrese el elemento { i + 1 } : " ) # Recibe una elemento
        lista.append(elemento) # Agrega el elemento a la lista
    return lista # Devuelve la lista


def eliminar_lista(lista1,lista2) : # Elimina de la listal los elementos de la lista2
    """Elimina de la primera lista los elementos que están en la segunda lista """ # Recibe dos listas
    for i in lista1 : #Recorre la listal
        if i in lista2 : # Si la palabra está en la lista2
            lista1.remove(i) # Elimina la palabra de la listal
    return lista1 # Devuelve la listal