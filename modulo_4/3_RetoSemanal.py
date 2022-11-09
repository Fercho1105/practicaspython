lista_base = []

suma_calif = 0


while True:
    print("""
    Bienvenido a la base de datos de la escuela.
    ¿Que deasea hacer?
    Agregar un nuevo alumno (1)
    Ver los alumnos y sus calificaciones (2)
    Salir (3)
    """)
    while True :
        try:
            eleccion= int(input("Ingrese una opcion: "))
            break
        except ValueError:
            print("Ingrese una opcion valida")


    if eleccion == 1 :
        print("Ha deseado agregar un alumno")
        while True :
            nombre = input("Introduzca el nombre del alumno : ")
            nombre = nombre.capitalize()
            apellidos = input("Ingrese sus apellidos: ")
            apellidos = apellidos.capitalize()
            alumno = nombre + " " + apellidos
            if nombre == "" or apellidos == "":
                print("No has introducido el nombre u apellidos del alumno:")
            else:
                break

        while True:
            try:
                no_calif = int(input("¿Cuantas calificaciones desea agregar?: "))
                break
            except ValueError :
                print("Ingrese un valor correcto")

        while True :
            try :
                for i in range(no_calif):
                    calificacion = float(input("Introduzca una calificacion: "))
                    suma_calif += calificacion
                promedio = suma_calif / no_calif
                suma_calif = 0
                lista_base.append([alumno,promedio])
                break
            except ValueError :
                print ('Debes introducir un valor correcto')        


    elif eleccion == 2 :
        print("Ha deseado ver las calificaciones de los alumnos")
        for x in range(len(lista_base)):
            print(f"El promedio de {lista_base[x][0]} es {lista_base[x][1]} \n")
        break


    elif eleccion == 3 :
        print("Usted ha querido salir del programa")
        while True :
            try:
                eleccion_out = int(input("¿Esta seguro? Si(1) o No(2): "))
                if eleccion_out == 1:
                    print("Fin del programa")
                    exit()
                elif eleccion_out == 2:
                    print("Volveremos al menu de inicio")
                    break
                else:
                    print("Valor desconocido, intente nuevamente")
            except ValueError :
                print("Ingrese una opcion valida")

    else:
        print("Eleccion desconocida, intente nuevamente")
