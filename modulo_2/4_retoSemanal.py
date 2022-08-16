contraseña = input("Ingrese una contraseña: ")
inicioContraseña = contraseña[0]
tipo_inicio_contraseña = inicioContraseña.isdigit()

while tipo_inicio_contraseña == False :
    print("Error!!! Empiece con un número porfavor.")
    contraseña = input("Ingrese una contraseña: ")
    inicioContraseña = contraseña[0]
    tipo_inicio_contraseña = inicioContraseña.isdigit()
    if tipo_inicio_contraseña == True:
        break

comprobacion_contraseña = input("Ingrese nuevamente la contraseña: ")
contador = 1
while comprobacion_contraseña != contraseña :
    print("Las contraseñas no coinciden.")
    if contador < 3:
        input("Ingrese nuevamente la contraseña: ")
        if comprobacion_contraseña == contraseña :
            print("Contraseña correcta")
            break
        else:
            contador += 1
            continue
    else:
        print("Fin del programa.")
        break



