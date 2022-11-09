## GRAFICOS DE DISPERCION

import random
import matplotlib.pyplot as plt


eje_x = [random.randint(1,100) for n in range(100)] #Generamos 100 valores en el eje de las x y los guardamos en una lista

eje_y = [random.randint(1,100) for n in range(100)] #Generamos 100 valores en el eje de las y y los guardamos en una lista



plt.scatter(eje_x,eje_y) # Construye la grafica de dispercion de los datos de eje_x y eje_y


#Le ponemos nombre a la grafica
plt.title("Grafica de dispercion")
plt.show()











