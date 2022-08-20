lista = []
alumnos = 1
limite_alumos = int(input("¿Cuántos alumnos desea registrar: "))

while alumnos <= limite_alumos:
    opcion = input("Agregar alumno(1) o Terminar el programa(2): ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del alumno: ").capitalize()
        calificacion1 =input(f"Ingrese la primera calificación de {nombre}: ")
        tamaño_cal1 = len(calificacion1)
        calificacion2 =input(f"Ingrese la segunda calificación de {nombre}: ")
        tamaño_cal2 = len(calificacion2)
        calificacion3 =input(f"Ingrese la tercer calificación de {nombre}: ")
        tamaño_cal3 = len(calificacion3)

        if len(calificacion1) > 0 and len(calificacion2) > 0 and len(calificacion3) > 0:
            calificacion1 = int(calificacion1)
            calificacion2 = int(calificacion2)
            calificacion3 = int(calificacion3)
            promedio = (calificacion1 + calificacion2 + calificacion3) / 3
            promedio =  float(promedio)

        elif len(calificacion1) > 0 and len(calificacion2) > 0 and len(calificacion3) == 0:
            calificacion1 = int(calificacion1)
            calificacion2 = int(calificacion2)
            promedio = (calificacion1 + calificacion2) / 2
            promedio =  float(promedio)

        elif len(calificacion1) == 0 and len(calificacion2) > 0 and len(calificacion3) > 0:
            calificacion2 = int(calificacion2)
            calificacion3 = int(calificacion3)
            promedio = (calificacion2 + calificacion3) / 2
            promedio =  float(promedio)
        
        elif len(calificacion1) > 0 and len(calificacion2) == 0 and len(calificacion3) > 0:
            calificacion1 = int(calificacion1)
            calificacion3 = int(calificacion3)
            promedio = (calificacion1 + calificacion3) / 2
            promedio =  float(promedio)

        elif len(calificacion1) > 0 and len(calificacion2) == 0 and len(calificacion3) == 0:
            calificacion1 = int(calificacion1)
            promedio = calificacion1
            promedio =  float(promedio)

        elif len(calificacion1) == 0 and len(calificacion2) > 0 and len(calificacion3) == 0:
            calificacion2 = int(calificacion2)
            promedio = calificacion2
            promedio =  float(promedio)

        elif len(calificacion1) == 0 and len(calificacion2) == 0 and len(calificacion3) > 0:
            calificacion3 = int(calificacion3)
            promedio = calificacion3
            promedio =  float(promedio)

        else:
            while True:
                print("Debe de haber por lo menos registrar una calificación.")
                print("Ingrese nuevamente los valores.")
                calificacion1 =input(f"Ingrese la primera calificación de {nombre}: ")
                tamaño_cal1 = len(calificacion1)
                calificacion2 =input(f"Ingrese la segunda calificación de {nombre}: ")
                tamaño_cal2 = len(calificacion2)
                calificacion3 =input(f"Ingrese la tercer calificación de {nombre}: ")
                tamaño_cal3 = len(calificacion3)
                if tamaño_cal1 > 0 or tamaño_cal2 > 0 or tamaño_cal3 > 0:
                    if len(calificacion1) > 0 and len(calificacion2) > 0 and len(calificacion3) > 0:
                        calificacion1 = int(calificacion1)
                        calificacion2 = int(calificacion2)
                        calificacion3 = int(calificacion3)
                        promedio = (calificacion1 + calificacion2 + calificacion3) / 3
                        promedio =  float(promedio)
                        break

                    elif len(calificacion1) > 0 and len(calificacion2) > 0 and len(calificacion3) == 0:
                        calificacion1 = int(calificacion1)
                        calificacion2 = int(calificacion2)
                        promedio = (calificacion1 + calificacion2) / 2
                        promedio =  float(promedio)
                        break

                    elif len(calificacion1) == 0 and len(calificacion2) > 0 and len(calificacion3) > 0:
                        calificacion2 = int(calificacion2)
                        calificacion3 = int(calificacion3)
                        promedio = (calificacion2 + calificacion3) / 2
                        promedio =  float(promedio)
                        break
                    
                    elif len(calificacion1) > 0 and len(calificacion2) == 0 and len(calificacion3) > 0:
                        calificacion1 = int(calificacion1)
                        calificacion3 = int(calificacion3)
                        promedio = (calificacion1 + calificacion3) / 2
                        promedio =  float(promedio)
                        break

                    elif len(calificacion1) > 0 and len(calificacion2) == 0 and len(calificacion3) == 0:
                        calificacion1 = int(calificacion1)
                        promedio = calificacion1
                        promedio =  float(promedio)
                        break

                    elif len(calificacion1) == 0 and len(calificacion2) > 0 and len(calificacion3) == 0:
                        calificacion2 = int(calificacion2)
                        promedio = calificacion2
                        promedio =  float(promedio)
                        break

                    elif len(calificacion1) == 0 and len(calificacion2) == 0 and len(calificacion3) > 0:
                        calificacion3 = int(calificacion3)
                        promedio = calificacion3
                        promedio =  float(promedio)
                        break
                else:
                    continue
        alumno = [nombre,calificacion1,calificacion2,calificacion3,f"promedio ={promedio}"]
        alumnos += 1
        lista.append(alumno)
    elif opcion == "2":
        print(f"El programa ha terminado con la cantidad de {alumnos} alumnos registrados")
        break
    else:
        print("Opcion no valida")
        continue

print("La lista de alumnos es: ")
# print(lista)

for element in lista: 
    print(f"\n {element}") 

# nombre = input("Ingrese el nombre del alumno: ").capitalize()
# calificacion1 =input(f"Ingrese la primera calificación de {nombre}: ")
# tamaño_cal1 = len(calificacion1)
# calificacion2 =input(f"Ingrese la segunda calificación de {nombre}: ")
# tamaño_cal2 = len(calificacion2)
# calificacion3 =input(f"Ingrese la tercer calificación de {nombre}: ")
# tamaño_cal3 = len(calificacion3)

# if len(calificacion1) > 0 and len(calificacion2) > 0 and len(calificacion3) > 0:
#     calificacion1 = int(calificacion1)
#     calificacion2 = int(calificacion2)
#     calificacion3 = int(calificacion3)

#     print(type(calificacion1))
#     print(type(calificacion2))
#     print(type(calificacion3))
# else:
#     while True:
#         print("Debe de haber por lo menos registrar una calificación.")
#         print("Ingrese nuevamente los valores.")
#         calificacion1 =input(f"Ingrese la primera calificación de {nombre}: ")
#         tamaño_cal1 = len(calificacion1)
#         calificacion2 =input(f"Ingrese la segunda calificación de {nombre}: ")
#         tamaño_cal2 = len(calificacion2)
#         calificacion3 =input(f"Ingrese la tercer calificación de {nombre}: ")
#         tamaño_cal3 = len(calificacion3)
#         if tamaño_cal1 > 0 or tamaño_cal2 > 0 or tamaño_cal3 > 0:
#             break
#         else:
#             continue











# # if tamaño_cal1 > 0:
# #     calificacion1 = int(calificacion1)
# #     print(tamaño_cal1)
# #     print("Casilla llena")
# # else:
# #     print("Casilla vacia")





# # calificacion2 = int(input(f"Ingrese la segunda calificación de {nombre}: "))
# # calificacion3 = int(input(f"Ingrese la tercer calificación de {nombre}: "))
# # while len(calificacion1) == 0 and len(calificacion1) == 0 and len(calificacion1) ==0:
# #     input("Debe de haber por lo menos registrar una calificación")
# #     calificacion1 = int(input(f"Ingrese la primera calificación de {nombre}: "))
# #     calificacion2 = int(input(f"Ingrese la segunda calificación de {nombre}: "))
# #     calificacion3 = int(input(f"Ingrese la tercer calificación de {nombre}: "))
# #     if len(calificacion1) > 0 or len(calificacion1) > 0 or len(calificacion1) >0:
# #         break
# #     else:
# #         continue
