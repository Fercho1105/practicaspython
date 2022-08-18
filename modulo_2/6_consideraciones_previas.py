# *** CONTINUE en for

"""Cuando estamos iterando en un ciclo al llegar a la secuencia continue se interrumpe la ejecuccion y se salta a la siguiente iteracion"""

# for numero in range(1,11):
#     if numero % 2 == 1:
#         continue  
#     else:
#         print(f"{numero} es par")


# *** CONTINUE en while    

# numero = 0
# while numero < 11:
#     numero += 1
#     if numero % 2 == 0 :
#         continue
#     print(f"{numero} es impar")

######################################################################

#***** BREAK en while

""" Se sale del ciclo """

# numero = int(input("Ingrese un digito: "))
# limite_inferior = 0
# limite_superior = 10
# buscado = 5
# intentos = 0


# while True:
#     intentos += 1
#     if numero == buscado:
#         print(f"El numero {numero} fue encontrado en {intentos} intentos")
#         break
#     elif numero < buscado :
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) // 2
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) // 2

# print("Fin del programa")

######################################################################

#*** exit() en while

"""Cierra totalmente el programa"""

# numero = int(input("Ingrese un digito: "))
# limite_inferior = 0
# limite_superior = 10
# buscado = 5
# intentos = 0


# while True:
#     intentos += 1
#     if numero == buscado:
#         print(f"El numero {numero} fue encontrado en {intentos} intentos")
#         exit()
#     elif numero < buscado :
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) // 2
#     else:
#         limite_inferior = buscado
#         buscado = (buscado + limite_superior) // 2

# print("Fin del programa")  # No se imprime porque " exit() " cierra todo el programa

# otro programa de ejemplo

# intentos = 0
# while True:
#     intentos += 1
#     print(f"Intento {intentos}")
#     if intentos == 20:
#         print("Fin del programa")
#         exit()









