# #Valores de retorno, sentencia: "return"


# def promedio (*numeros) :

#     return sum(numeros) / len(numeros)   # Hacemos que la funcion devuelva un valor , y así este valor pueda ser almacenado.

# x = promedio(4,5,6)
# print(x)

#-----------------------------------------------


# def area(**dato) : # ** dato es una variable que recibe un diccionario
#     """ Calcula el área de una figura geométrica y la imprime en pantalla .""" # Docstring

#     # Si el diccionario tiene una clave llamada ' figura ' evalúa el valor de la clave
#     if dato["figura"] == "Rectángulo" :
#         return (dato["base"] * dato["altura"]) # Si el valor de la clave es ' Rectángulo ' imprime el valor de la clave ' base ' multiplicado por la 'altura'
#     elif dato["figura"] == "Triángulo" :
#         return (dato["base"] * dato["altura"] / 2 ) # Si el valor de la clave es ' Triángulo ' imprime el valor de la clave ' base ' multiplicado por la ´altura´ sobre 2
#     elif dato["figura"] == "Círculo" :
#         return (3.141593 * dato[ "radio"] ** 2 ) # Si el valor de la clave es ' Círculo ' imprime el valor de la clave ' radio ' al cuadrado multiplicado por pi(3.141593)
#     else :
#         print("Figura desconocida") # Si el valor de la clave no es ninguna de las anteriores , imprime " Figura desconocida "

# triangulo = area( figura = 'Triángulo' , base = 10 , altura = 5 )
# print(f"El area del triangulo es {triangulo}")

# circulo = area( figura = 'Círculo' , radio = 10 , color = 'Rojo' )
# print(f"El area del circulo es {circulo}")

# dodecagono = area( figura = 'Dodecágono' , lado = 10 ) # Se regresa el valor "None"
# print(f"El area del dodecagono es: {dodecagono}")



################################################


# #Recursividad de funciones en python


# def factorial (numero) :
#     if numero == 0 :
#         return 1
#     else :
#         return factorial(numero - 1 )

# print (" El factorial de 0 es ( 0! ) : " , factorial(0))
# print (" El factorial de 1 es ( 1! ) : " , factorial(1))
# print (" El factorial de 3 es ( 3! ) : " , factorial(3))
# print (" El factorial de -1 es ( -1! ) : ", factorial(-1))  #Esto da un error, sobrepasa el limite de recursividad que python establece.



################################################

# Funciones lambda o funciones anónimas .

# suma = lambda x , y : x + y
# print(suma( 'Hola' , ' mundo!' ) )
# print(suma(2,5))

#--------------------------------------------------

# lista_numeros = [1,0,-2]
# lista_numeros = sorted (lista_numeros, key = lambda n : abs ( n ) )
# print ( lista_numeros )


################################################


# Función zip
paises = [ 'Kenia' , 'Francia' , 'México' , 'Japón' ]
capitales = [ 'Nairobi' , 'Paris' , 'Ciudad de México' , 'Tokio' ]
poblacion = [ 54, 66, 130]
for i in zip(paises,capitales,poblacion):
    print(i)


