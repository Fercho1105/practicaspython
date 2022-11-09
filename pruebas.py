# ala = "a"
# lista1 = ["Fernando","Diaz","56","No tiene","45645644",ala]

# print(lista1)

# with open("prueba.txt","w") as prueba:
#     prueba.write(f"{lista1[0]} {lista1[1]} | Edad: {lista1[2]} |Correo: {lista1[3]} | Telefono: {lista1[4]}\n") 
#     print("Datos guardados exitosamente en agenda2.txt")  

# print("""
# ¿Que archivo desea cambiar?
# 1. Nombre
# 2. Apellido
# 3. Edad
# 4. Correo
# 5.Telefono
# """)

# respuesta = (input("¿Que archivo desea cambiar?"))

# if respuesta == "1":
#     lista1[0] = input("Ingrese el nuevo Nombre:")
# elif respuesta =="2":
#     lista1[1] = input("Ingrese el nuevo Apellido: ")
# elif respuesta =="3":
#     lista1[2] = input("Ingrese la nueva Edad: ")
# elif respuesta =="4":
#     lista1[3] = input("Ingrese el nuevo Correo: ")
# elif respuesta =="5":
#     lista1[4] = input("Ingrese el nuevo Telefono: ")

# print(lista1)

# with open("prueba.txt","w") as prueba:
#     prueba.write(f"{lista1[0]} {lista1[1]} | Edad: {lista1[2]} |Correo: {lista1[3]} | Telefono: {lista1[4]}\n") 
#     print("Datos guardados exitosamente en agenda2.txt")  

import fileinput

new_id = input("Inserte nuevo ID: ")

for line in fileinput.FileInput("prueba.txt", inplace = 1):
    if line.startswith("id="):
        new_line = line.replace(line,"id=" + new_id)
        print(new_line)
    else:
        print(line, end='')


