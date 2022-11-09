def letra_adyacente (letra) : # Función que devuelve la letra adyacente a la que se le pasa como parámetro .
    """Función que devuelve las letra adyacentes a la introducida por el usuario . """ # Comentario de la función .
    alfabeto = " ABCDEFGHIJKLMNOPQRSTUVWXYZ " # Definición del alfabeto .
    for i in alfabeto : # Ciclo que recorre el alfabeto .
        if letra == i : # Condición que comprueba si la letra introducida es igual a la letra del alfabeto .
            print ( " La letra introducida es :" + letra )
            print ( " La letra anterior es : " + alfabeto [ alfabeto.index ( i ) -1 ] ) # Imprime la letra anterior .
            print ( " La letra siguiente es : " + alfabeto [ alfabeto.index ( i ) +1 ] ) # Imprime la letra siguiente .
            break

while True : # Ciclo infinito .
    letra = input ( "Introduce una letra del alfabeto: "
                    "\n ( Para salir escribe 0 )\n" ) # Solicita al usuario una letra y se indica que si se introduce se sale del programa .
    if len ( letra ) > 1 : # Condición que comprueba si la longitud de la letra introducida es mayor que 1 .
        print ( " Debes introducir una sola letra . " ) # Imprime un mensaje de error .
    elif letra.isalpha ( ) : # Condición que comprueba si la letra introducida es alfabética .
        letra = letra.upper ( ) # Convierte la letra introducida a mayúsculas .
        letra_adyacente ( letra ) # Llama a la función que devuelve las letras adyacentes .
    elif letra == " 0 " : # Condición que comprueba si la letra introducida es 0 .
        break # Sale del ciclo .
    else : # Condición que comprueba si la letra introducida no es alfabética ni 0 .
        print ( " La letra introducida no es válida . " ) # Imprime un mensaje de error .