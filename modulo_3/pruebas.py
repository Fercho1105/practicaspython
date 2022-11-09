# while True:
#     caracter = input("Ingrese in letra: ")
#     esLetra = caracter.isalpha()
#     if esLetra == False:
#         print("Escriba una letra porfavor.")
#         continue
#     else:
#         abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#         for letra in abecedario:
#             if letra == caracter:
#                 indice = abecedario.index(letra)
#                 indice_a_imprimir1 = indice - 1
#                 indice_a_imprimir2 = indice + 1
#                 print(abecedario[indice_a_imprimir1])
#                 print(abecedario[indice_a_imprimir2])
#                 break
#             else:
#                 continue

#Funcion

def funcionimprimirletra():
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letra in abecedario:
        if letra == caracter:
            indice = abecedario.index(letra)
            indice_a_imprimir1 = indice - 1
            indice_a_imprimir2 = indice + 1
            print(abecedario[indice_a_imprimir1])
            print(abecedario[indice_a_imprimir2])
            exit()
        else:
            continue

caracter = "a"

funcionimprimirletra(caracter)