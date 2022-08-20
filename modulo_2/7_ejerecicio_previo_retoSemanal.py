lista = []
alumnos = 0
limite_alumos = int(input("¿Cuántos alumnos desea registrar: "))

while alumnos <= limite_alumos:
    opcion = input("Agregar alumno(1) o Terminar el programa(2): ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del alumno: ").capitalize()
        calificacion1 = int(input(f"Ingrese la primera calificación de {nombre}: "))
        calificacion2 = int(input(f"Ingrese la segunda calificación de {nombre}: "))
        calificacion3 = int(input(f"Ingrese la tercer calificación de {nombre}: "))
        alumno = [nombre,calificacion1,calificacion2,calificacion3]
        alumnos += 1
        lista.append(alumno)
    elif opcion == "2":
        print(f"El programa ha terminado con la cantidad de {alumnos} alumnos registrados")
        break
    else:
        print("Opcion no valida")
        continue

print("La lista de alumnos es: ")
print(lista)



