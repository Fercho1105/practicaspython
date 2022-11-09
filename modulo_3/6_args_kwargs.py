# #Parametros de tipo tupla , * args

# def promedio (*numeros) : # con "*"se puede recibir multiples numeros, en forma de tupla
#     """
#     Recibe un sólo parámetro de tipo tupla , de valores numéricos
#     E imprime su promedio

#     """ 
#     promedio = sum(numeros) / len(numeros)
#     print(' El promedio es : ' ,promedio)

# promedio(4 )
# promedio(4,5,6)
# promedio(1, 2, 3, 4, 5, 6, 7, 8, 9)

#-----------------------------------------------------------------------------------------------------

# def es_numero( titulo , *serie):
#     """
#     Imprime un título
#     Verifica el si el caracter en el parámetro de tipo tupla es un numero o no
#     """
#     print(titulo)
#     for i in serie :
#         if  type(i) is int or i.isdigit():
#             print (f' {i} es numero')
#         else:
#             print (f' {i} no es numero')

# es_numero( 'Numeros' , '1' , '2' , '3' )
# es_numero( 'Letras' , 'a' , 'b' , 'c' )

# nombre = 'Mezcla'
# lista_varios = [ 'a' , '2' , 3 , 'f' , 5 ]
# es_numero(nombre ,*lista_varios)

###########################################################################################

# Parámetros tipo diccionario ** kwargs
def area(**dato) : # ** dato es una variable que recibe un diccionario
    """ Calcula el área de una figura geométrica y la imprime en pantalla .""" # Docstring

    # Si el diccionario tiene una clave llamada ' figura ' evalúa el valor de la clave
    if dato["figura"] == "Rectángulo" :
        print(dato["base"] * dato["altura"]) # Si el valor de la clave es ' Rectángulo ' imprime el valor de la clave ' base ' multiplicado por la 'altura'
    elif dato["figura"] == "Triángulo" :
        print(dato["base"] * dato["altura"] / 2 ) # Si el valor de la clave es ' Triángulo ' imprime el valor de la clave ' base ' multiplicado por la ´altura´ sobre 2
    elif dato["figura"] == "Círculo" :
        print(3.141593 * dato[ "radio"] ** 2 ) # Si el valor de la clave es ' Círculo ' imprime el valor de la clave ' radio ' al cuadrado multiplicado por pi(3.141593)
    else :
        print ("Figura desconocida") # Si el valor de la clave no es ninguna de las anteriores , imprime " Figura desconocida "

area( figura = 'Triángulo' , base = 10 , altura = 5 )
area( figura = 'Círculo' , radio = 10 , color = 'Rojo' )
area( figura = 'Dodecágono' , lado = 10 )