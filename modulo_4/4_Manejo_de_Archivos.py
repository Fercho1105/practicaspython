# #MODO ESCRITURA/SOBREESCRITURA
# # f_archivo = open("archivo1.txt", "w")#Creamos o abrimos un archivo "archivo1.txt", que en este caso lo creamos y lo abrimos en modo de escritura o sobreescritura "w"
# # print(f_archivo) #Imprimios la propiedades de la variable, en este caso, del archivo
# # f_archivo.write("Hola mundo!") # Escribimos en el archivo con .write()
# # f_archivo.close() #Cerramos el archivo con .close() , es importante cerrar archivos cuando ya no los vayamos a utilizar


# f_archivo = open("archivo1.txt", "w")  #Abrimos, ya que ya está creado, el archivo en modo escritura/sobreescritura
# f_archivo.write("Este es mi primer archivo") #Sobreescribimos en el archivo
# f_archivo.close() #Cerramos el archivo

# #MODO LECTURA 
# f_lectura = open("archivo1.txt", "r")  #Abrimos el archivo en modo lectura, no se puede modificar
# print(f_lectura.read())  #Vamos a imprimir el contenido del archivo,las cadenas que contiene, con .read()
# f_lectura.close() #Cerramos el archivo


# #Imprimimos las propiedades de los archivos
# print(f_archivo) #Vemos que esta en modo escritura
# print(f_lectura) #Esta en modo lectura


############################################

#Sentencia "with" y  "as"

# f_lectura = open("archivo1.txt", "r") #Abrimos el archivo en modo lectura
# print(f_lectura.closed) #Vemos si el archivo esta cerrado con .closed
# f_lectura.close() #Cerramos el archivo
# print(f_lectura.closed) #Volvemos a confirmar si el archivo esta cerrado

# #Con la sentencia "with", trabajamos dentro ella y le agregamos un alies con "as"
# with open("archivo1.txt", "r") as f_lectura: #Abrimos el archivo "archivo1.txt" con alias "f_lectura" en modo en lectrura ("r")
#     print(f_lectura.closed) #Preguntamos si el archivo esta cerrado y da "False"
# print(f_lectura.closed) #Nuevamente volvemos a preguntar si esta cerrado el archivo y ahora de "True" . Esto es porque el archivo se cierra automaticamente cuando nos salimeos de la sentencia "with"


# #AHORA, AÑADIREMOS INFORMACION AL ARCHIVO SIN SOBREESCRIBIR, NI PERDER INFORMACION 
# # with open("archivo1.txt", "a") as f_archivo: #Abrimos nuevamente el archivo, pero en modo "a"(append) para agregar info. al final del archivo
# #     f_archivo.write("\nEste es mi primer archivo 2") #Agregamos un salto de linea y texto
# #     f_archivo.write("Este es mi primer archivo 3") #Agregamos texto sin salto de linea, por lo que empezará a escribirse esta linea, a lado de la linea anterior
# #     f_archivo.write("\n") #Agregamos un salto de linea
# #     f_archivo.write("\tEste es mi primer archivo 4") #Agregamos una indentacion y texto
# with open("archivo1.txt", "r") as f_lectura: #Abrimos el archivo en modo lectura 
#     # print(f_lectura.read()) #Imprimimos el contenido del archivo
#     contenido = f_lectura.read() #Guardamos la informacion en una variable.
#     print(f"****{contenido}****") #Imprimimos la infromacion
#     contenido = f_lectura.read() #Volvemos a leer el archivo para guardar info.
#     print(f"****{contenido}****") # No se guarda nada , porque cuando un archvo ya fue leido,y se vuelve a leer, empieza a leer desde donde acabo de leer la vez anterior. Entonces ya no hay nada despues de donde se quedo el archivo


############################################

#LECTURA DE ARCHIVOS LÍNEA A LÍNEA

# with open("archivo1.txt","r") as f_lectura: #Abrimos el archivor en modo lectura 
#     numero_de_lineas = 0 #Hacemos un contador desde 0
#     for i in f_lectura: #Entramos a un bucle "for" que leerá las lineas del archivo
#         numero_de_lineas += 1 #Sumamos cada vez que se encuentre una linea
#         print(f"Linea: {numero_de_lineas}: {i}") #En una cadena formateada, imprimimos el numero de linea y su contenido
#     print(f"El archivo tiene {numero_de_lineas} lineas") #Imprimimos el numero total delienas

############################################

#CREANDO UNA LISTA A PARTIR DE UNA ARCHIVO

with open("archivo1.txt","r") as f_lectura: #Abrimos archivo en modo lectura
    lista_archivo = f_lectura.readlines() #Con el metodo .readlines() Devuelve todas las líneas del archivo, como una lista donde cada línea es un elemento en el objeto de la lista
    print(lista_archivo) #Imprimimos la lista

# print(lista_archivo) #Podemos usar la lista creada, a pesar de habernos salido del "with"

#Podemos modificar la lista de ser necesario
lista_archivo[1] = "Este es mi primer archivo 2 \n" 
lista_archivo.insert(2,"Este es mi primer archivo 3 \n")

print(lista_archivo) #CHecamos la lista actualizada

with open("archivo1.txt","w") as f_archivo: #Ahora actualizamos y sobreescribimos los datos del archivo, ya que lo abirmos en "w" (escritura/sobreescritura), si solo queremos agregar, abrimos en "a" (append) 
    f_archivo.writelines(lista_archivo) #Con .wrtitelines(parametro), sobreescribmos los datos del archivo con el parametro 



############################################