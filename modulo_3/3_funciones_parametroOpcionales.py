# def sumar (parametro1, parametro2 ) :
#     """ Función que suma dos parametros y los imprime en pantalla """
#     print ( ' Suma : ' , parametro1 + parametro2 ) 
# argumento1 = 5
# argumento2 = 7
# # Invocando a la función por medio de parametro variables
# sumar (argumento1,argumento2)
# # Invocando a la función por medio de parametros de valor
# sumar ( ' mundo ! ' , ' Hola ' )
# sumar ( ' Hola ' , ' mundo ! ' )
# sumar ( ' hola ' )




########
# Parámetros opcionales
def muestra_alumno ( nombre , edad = 18 , sexo = ' F ' ) :
    """ Es una función que muestra en pantalla el nombre , la edad y el sexo de un alumno
    Recibe tres parámtros .
    1.- Nombre
    2. Edad - 18 
    3. Sexo = ' F '
    """


print ( f'Nombre : ( nombre ) , Edad : ( edad ) , Sexo : ( sexo ) ' )
# Ejecución de función con parámetro obligatorio
muestra_alumno ( ' María ' )
# Ejecución utilizando el parametro obligatorio y uno opcional
muestra_alumno ( ' María ' , 22 )
# Ejecución de función con el primer y último parámtro
muestra_alumno ( ' Juan ' , sexo = ' M ' )