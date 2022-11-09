import numpy as np
import matplotlib.pyplot as plt


## HACEMOS USO DE LA DISTRIBUCION NORMAL

#SINTAXIS
#np.random.normal(media_districucion, desviacion_estandar, tamaño_muestras)

datos = np.random.normal(0, 1.0, 1000)

plt.hist(datos)
plt.show()


