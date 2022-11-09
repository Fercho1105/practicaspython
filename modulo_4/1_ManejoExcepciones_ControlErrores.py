# numerador = 10
# denominador = 0
# cadena = '3'
# numerico = 5

# print(numerador/denominador)  #Aqui nos sale un error de "ZeroDivisionError", no se puede dividir entre 0
# print(cadena + numerico) #"Aqui nos sale un error de TypeError" , no se pueden concatenar un string y un int


# try :
# print ( numerador / denominador )
# except ZeroDivisionError :
# print ( ' Ha ocurrido una division entre cero ' )

#####################################################

# try :
# print ( cadena + numerico )
# except TypeError :
# print ( ' Ha ocurrido un error de tipo ' )
#print ( ' Fin del programa ' )


#####################################################

try :
    print ( 10 / 0 )
except TypeError :
    print ( ' Ha ocurrido un error de tipo ' ) # Si no hay uno "TypeError, se va a la sig. excepción"
except :
    print ( " Ha ocurrido un error desconocido " )