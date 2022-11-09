
personas = [] # Creamos una lista para guardar una lista que contenga los datso de las personas

while True:
    print("""
    1. Agregar personas a la agenda
    2.Guardar daros en un archivo
    """)
    opcion = input("Ingrese una opcion: ")  #Le pedimos al usuario que digite una opcion


    if opcion == "1":  #Agregamos una persona

        contacto = []
        while True :
            nombre = input("Introduce tu nombre : ") #Pedimos que inserte los datos correctamente
            apellido = input("Introduce tu apellido : ")
            if nombre == "" :
                print("No has introducido tu nombre")
            elif apellido == "" :
                print("No has introducido tu apellido")  
            else :
                contacto.append(nombre)  #Agregamos los datos a la lista contacto
                contacto.append(apellido)
                break

        while True :
            try :
                edad = int(input("Introduce tu edad : ")) #Pedimos que inserte los datos correctamente
                contacto.append(edad) #Agregamos los datos a la lista contacto
                break
            except ValueError :
                    print('Debes introducir un número')

        correo = input("Introduce tu correo : ")
        contacto.append(correo)#Agregamos los datos a la lista contacto

        while True :
            try :
                telefono = input("Introduce tu teléfono : ") #Pedimos que inserte los datos correctamente
                int(telefono)
                contacto.append(telefono) #Agregamos los datos a la lista contacto
                break
            except ValueError :
                print ('Debes introducir un número')

        personas.append(contacto)  #Ahora la lista "contacto" que contiene los datos de la persona, la agregamos a la lista "personas"

    elif opcion == "2":  #Guardamos los datos
        with open("agenda.txt", "w") as f_agenda:  #Creamos u abrimos el archivo "agenda.txt" en modo escritura
            for persona in personas: #Ahora con un bucle "for", empezamos a escribir dato a dato 
                f_agenda.write(f"{persona[0]} {persona[1]} Edad: {persona[2]} Correo: {persona[3]} Telefono: {persona[4]}\n") #Escribimos los datos en una cadena formateada
            print("Datos guardados exitosamente en agenda.txt")  #Arrojamos un mensaje de exito respecto a la accion de guardar datos
        break  

    else:
        print("Opcion no valida")  #Si no ingrese una opcion correcta, vuelve al menu
        print("Volver a intentar")
