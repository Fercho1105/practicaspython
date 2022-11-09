#Le pedimos al usuario las coordenadas

x = int(input ('Ingresa el valor de x: ')) # Le pedimos al usuario la coordenada "x" y  lo casteamos a un dato entero
y = int(input ('Ingresa el valor de y: ')) # Le pedimos al usuario la coordenada "y" y  lo casteamos a un dato entero

# x = input ('Ingresa el valor de x: ')
# y = input ('Ingresa el valor de y: ')

# while len(x) == 0 and len(y) == 0:
#     print("Porfavor, no deje campos vacios.")
#     x = input ('Ingresa el valor de x: ')
#     y = input ('Ingresa el valor de y: ')
#     tipo_nombreX=x.isdigit()
#     tipo_nombreY=y.isdigit()
#     while tipo_nombreX == False or tipo_nombreY == False:
#         print("Porfavor, inserte un numero por coordenada.")
#         x = input ('Ingresa el valor de x: ')
#         y = input ('Ingresa el valor de y: ')
#         if tipo_nombreX == True or tipo_nombreY == True:
#             break
#         else:
#             pass

# x = int(x)
# y = int(y)

if x==0 and y==0:  # En dado caso que este en el origen,las coordenadas se lo hacemos saber al usuario
    print ('Origen')
elif x>0 and y>0:
    print ('Cuadrante I') #Si el eje "X" y "Y" son mayores a cero,las coordenadas están en el cuadrante 1.
elif x==0 and y>0:
    print("Entre cuadrante I y II") # Si el eje "X" es igual a cero y el eje "Y" es mayor a cero, la coordenada esta entre el 1er  y 2do cuadrante.
elif x<0 and y>0:
    print ('Cuadrante II') # Si el eje "X" es menor a cero, y el eje "Y" es mayor a cero, las coordenadas están en el cuadrante 2.
elif x<0 and y==0:
    print("Entre cuadrante II y III") # Si el eje "X" es menor a cero y el eje "Y" es igual a cero, la coordenada esta entre el 2do  y 3er cuadrante.
elif x<0 and y<0:
    print ('Cuadrante III') #Si el eje "X" y "Y" son menores a cero,las coordenadas están en el cuadrante 3.
elif x==0 and y<0:
    print("Entre cuadrante III y IV") # Si el eje "X" es igual a cero y el eje "Y" es menor a cero, la coordenada esta entre el 3er  y 4to cuadrante.
elif x>0 and y<0 :
    print ('Cuadrante IV ') # Si el eje "X" es mayor a cero, y el eje "Y" es menor a cero, las coordenadas están en el cuadrante 4.
else :
    print("Entre cuadrante IV y I") # Si el eje "X" es mayor a cero y el eje "Y" es igual a cero, la coordenada esta entre el 4to  y 1er cuadrante.

