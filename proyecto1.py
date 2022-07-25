nombre=input("Ingrese su nombre: ")
numeDeCaracteres_Nombre=len(nombre)
tipo_nombre=nombre.isalpha()

while numeDeCaracteres_Nombre ==0 or tipo_nombre == False:
    print("Error, no deje ninguna casilla vacia o ponga algun valor que no sea letras")
    nombre=input("Ingrese su nombre: ")
    numeDeCaracteres_Nombre=len(nombre)
    tipo_nombre=nombre.isalpha()
    if numeDeCaracteres_Nombre > 0 and tipo_nombre == True:
        break

#######
apellido_paterno=input("Ingrese su apellido paterno: ")
Caracteres_apellidoPaterno=len(apellido_paterno)
tipo_apellidoPaterno=apellido_paterno.isalpha()


while Caracteres_apellidoPaterno ==0 or tipo_apellidoPaterno == False:
    print("Error, no deje ninguna casilla vacia o ponga algun valor que no sea letras")
    apellido_paterno=input("Ingrese su apellido paterno: ")
    Caracteres_apellidoPaterno=len(apellido_paterno)
    tipo_apellidoPaterno=apellido_paterno.isalpha()
    if Caracteres_apellidoPaterno > 0 and tipo_apellidoPaterno == True:
        break

###########

apellido_materno=input("Ingrese su apellido materno: ")
Caracteres_apellidoMaterno=len(apellido_materno)
tipo_apellidoMaterno=apellido_materno.isalpha()

while Caracteres_apellidoMaterno ==0 or tipo_apellidoMaterno == False:
    print("Error, no deje ninguna casilla vacia o ponga algun valor que no sea letras")
    apellido_materno=input("Ingrese su apellido materno: ")
    Caracteres_apellidoMaterno=len(apellido_materno)
    tipo_apellidoMaterno=apellido_materno.isalpha()
    if Caracteres_apellidoMaterno > 0 and tipo_apellidoMaterno == True:
        break

########

edad=(input("¿Cuál es du edad? "))
Caracteres_edad=len(edad)
tipo_edad=edad.isdigit()



while Caracteres_edad ==0 or tipo_edad == False:
    print("Error, no deje ninguna casilla vacia o ponga un numero")
    edad=(input("¿Cuál es du edad? "))
    Caracteres_edad=len(edad)
    tipo_edad=edad.isdecimal()
    if Caracteres_edad > 0 and tipo_edad == True :
        break

#######
peso=input("Ingrese su peso en kilogramos : ")
Caracteres_peso=len(peso)
tipo_peso=peso.isdigit()

while Caracteres_peso ==0 or tipo_peso == False:
    print("Error, no deje ninguna casilla vacia o ponga un numero")
    peso=input("Ingrese su peso en kilogramos : ")
    Caracteres_peso=len(peso)
    tipo_peso=peso.isdecimal()
    if Caracteres_peso > 0 and tipo_peso == True :
        break

peso=float(peso)

#####

estatura=(input("Ingrese su estatura en metros: "))
Caracteres_estatura=len(estatura)


while Caracteres_estatura ==0:
    print("Error, no deje ninguna casilla vacia o ponga un numero")
    estatura=input("Ingrese su estatura en metros: ")
    Caracteres_estatura=len(estatura)

    if Caracteres_estatura > 0:
        break

estatura=float(estatura)

######
imc=peso/(estatura**2)
imc=float(imc)

#####

print("____________________________________________\n")
print("Nombre completo: " + nombre + " " + apellido_paterno + " " + apellido_materno)
print("Edad: " + str(edad) + " años.") 
print("Peso: "+ str(peso) + " kg.")
print("Estatura: " + str(estatura) + " mts.")
print("Su IMC es: " + str(imc))
if imc<=18.5:
    print("Peso inferior al normal")
elif imc>=18.5 and imc<=24.9:
    print("Peso normal")
elif imc>=25 and imc<=29.9:
    print("Peso superior al normal")
elif imc>=30:
    print("Obesidad")
else:
    print("Rango desconocido. Vuelva a insertar los datos correctamente")
print("_____________________________________________\n")




# print(f"""

#     Nombre completo: {nombre} {apellido_paterno} {apellido_materno}
#     Edad: {edad} años. 
#     Peso: {peso} kg
#     Estatura: {estatura} mts.
#     Su IMC es: {imc}

#     """)
