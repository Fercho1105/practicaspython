import numpy as np
import matplotlib.pyplot as plt




np.random.seed(0)

numeros = np.random.rand(10)  #Genera 10 numeros aleatorio en decimal entre 0 y 1



print(numeros)



plt.plot(numeros) #Hacemos una grafica con los numeros generados
plt.show()#Mostramos esa grafica

#En el eje de las "x", se establace como parametro, los elementos que se 
#generaron aleatoriamente menos uno, en este caso, (10-1)


