### m_alumno.py


"""
Este modulo contiene la funcion captura que solicita la informacion de los 
alumnos y la funcion promedio que calcula el promedio de cada alumno 
"""

def promedio(nombre,calificación1,calificación2) : # Función para calcul

    promedio = ( calificación1 + calificación2 ) / 2 # Se calcula el promedio
    print ( f'El promedio de { nombre } es { promedio } ' ) # Se imprime el nombre del
    
def captura ( numero = 3 ) : 
    lista = [ ] # Se crea una lista vacía
    for i in range ( numero ) : # Se recorre el número de veces que se le indique
        nombre = (input('Ingrese el nombre del alumno: ')).capitalize() 
        calif1 = int(input(f'Ingrese la primera calificación de {nombre}: ')) 
        calif2 = int(input(f'Ingrese la segunda calificación de {nombre}: '))
        lista.append([nombre , calif1 , calif2]) 
        promedio(nombre,calif1,calif2)
    print(lista) 