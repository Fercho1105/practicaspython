import numpy as np


# #Genera numero aleatorio en decimal entre 0 y 1
# numeros = np.random.rand()  

# print(numeros)


#################################################################################

#Creamos un numero aleatorio con una salida constante
#Es decir, no cambia cada vez que se ejecuta el programa
#Se genera un numero pseudoaleatorio, es decir, que se genera a partir de oatro numro, o sea, 
#no es totalmente aleatorio


# np.random.seed(0)

# numeros = np.random.rand()  #Genera numero aleatorio en decimal entre 0 y 1

# print(numeros)


#################################################################################

#Generamos una lista de numeros pseudoaleatorios


np.random.seed(0)

numeros = np.random.rand(10)  #Genera 10 numeros aleatorio en decimal entre 0 y 1

print(numeros)
