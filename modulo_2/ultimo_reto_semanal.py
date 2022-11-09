# Deinimos los diccionarios de traducción a emplear , en éste caso , español y inglés .

colores_en = {'rojo' : 'red' , 'naranja' : 'orange' , 'amarillo' : 'yellow' , 'verde' : 'green' , 'azul' : 'blue' , 'violeta' : 'purple'}
colores_it = {'rojo' : 'rosso' , 'naranja' : 'arancione' , 'amarillo' : 'giallo' , 'verde' : 'verde' , 'azul' : 'blu' , 'violeta' : 'viola' }

# Damos la bienvenida al usuario y le decimos cuáles son los idiomas disponibles .
print('Bienvenido al traductor de colores')
print('Este programa traduce colores de español a italiano o inglés)')

# Pedimos al usuario que escriba una frase con un color y lo guardamos en la variable frase .
frase = input('Escribe una frase con un color: ')

# Separamos las palabras de la frase en minúsculas y las guardamos en una lista .
palabras = frase.lower().split()

# Creamos un bucle infinito para que el programa siga ejecutándose hasta que el usuario decida salir .
while True :

    # Pedimos al usuario que escriba el idioma que quiere traducir .
    idioma = input('¿Qué idioma quieres traducir? inglés ( 1 ) o italiano ( 2 ) : ' )
    if idioma == '1' : # Si el usuario escribe 1 , entonces traduciremos a inglés .
        for i in palabras :
            # Si la palabra está en el diccionario de colores en inglés , entonces la traduciremos .
            if i in colores_en :
                print(frase) # Imprimimos la frase original .
                print (f'El color {i} en inglés es {colores_en[i]} ' ) # Imprimimos el color en inglés .
                exit() # Salimos del bucle infinito .

    elif idioma == '2' : # Si el usuario escribe 2 , entonces traduciremos a italiano .
        for i in palabras :
            # Si la palabra está en el diccionario de colores en italiano , entonces la traduciremos .
            if i in colores_it :
                print(frase) # Imprimimos la frase original .
                print( f'El color {i} en italiano es {colores_it[i]}') # Imprimimos el color en italiano .
                exit() # Salimos del bucle infinito .

        else : # si no está en el diccionario de colores en italiano , entonces le decimos que no se encuentra .
            print ( ' No se encontró el color ' )
            break # salimos del bucle infinito .
    else : # Si el usuario escribe otra cosa que no sea 1 o 2 , entonces le decimos que no es una opción válida .
        print ( ' No se ha ingresado una opción válida ' )

