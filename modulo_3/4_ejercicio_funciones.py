# Utilizar al menos 2 funciones
# Preguntar cuántos alumnos se registrarán , en caso de no ingresar una cantidad , se asume que se registrarán 3 alumnos
# Preguntará el nombre y 2 calificaciones
# Mostrar el nombre en pantalla con inicial mayúscula y promedio
# Al finalizar el programa se mostrará una lista con el nombre de cada alumno y sus calificaciones


def captura_alumnos(numero = 3):
        
    """
    Registra alumnos y dos calificaciones.
    Recibe como parametro la cantidad de alumnos a registrar.
    Si no especifica el numero de alumnos, se registrarán 3 alumnos 
    """

    lista_alumnos = []
    for i in range (numero) :
        nombre = input (f'{i + 1}.- Ingrese el nombre del alumno : ') .capitalize()
        calficacion1 = int(input( f'Ingrese la primera calificación de  {nombre} : '))
        calficacion2 = int(input( f'Ingrese la segunda calificación de  {nombre} : '))
        lista_alumnos.append([nombre ,calficacion1 ,calficacion2])
        promedio(nombre ,calficacion1 ,calficacion2)
    print ("Las calificaciones de los alumnos son: " ,lista_alumnos)

def promedio(nombre ,calificacion1 ,calificacion2):
    """
    Calcula el promedio de un alumno y lo despliega en pantalla por medio de un mensaje
    Recibe como parametros el nombre y dos calificaciones del alumno
    """
    promedio = (calificacion1 + calificacion2) / 2
    print (f'El promedio de {nombre}  es : { promedio } ')


numero_alumnos = input(' ¿ Cuántos alumnos desea registrar ? ')
if numero_alumnos.isdigit() :
    numero_alumnos = int(numero_alumnos)
    captura_alumnos (numero_alumnos)
else :
    captura_alumnos()
