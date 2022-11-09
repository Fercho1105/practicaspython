def agregar_datos(lista,valor = 'No especificado'):
    """
    Función que agrega un dato a una lista especificada
    """   
    if valor == "" :
        valor = "No especificado."

    lista.append(valor)
    return lista

def quitarRepetidos(lista1,lista2):
    for i in range (len(lista2)):
        while lista2[i] in lista1 :
            lista1.remove (lista2[i])
    return lista1

#Creador de listas

paises1= []

num_paises = int(input('¿Cuantas paises desea registrar?: '))

for i in range(num_paises):
    pais = input(f'Ingrese el pais numero {i + 1}: ' ).title()
    paises1 = agregar_datos(paises1,pais)


######

paises2= []

num_paises2 = int(input('¿Cuantas paises desea registrar en la 2da lista?: '))

for i in range(num_paises2):
    pais2 = input(f'Ingrese el pais numero {i + 1}: ' ).title()
    paises2 = agregar_datos(paises2,pais2)



######

print("Despues de eliminar los repetidos")
print(quitarRepetidos(paises1 ,paises2))








