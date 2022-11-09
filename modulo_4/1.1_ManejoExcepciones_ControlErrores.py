#Manejo de errores con excepciones y ciclos

while True:  #Creamos un ciclo para que el usuario ingrese los valores correctos
    try:
        dividendo = int(input("Ingrese el dividendo: "))
        divisor = int(input("Ingrese el divisor: "))
        print("El resultado es: ", dividendo / divisor)
        break #Si los valores son correctos, se acaba el programa
    except ValueError:  
        print("Debe ingresarse un numero")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

print("Fin del programa")
