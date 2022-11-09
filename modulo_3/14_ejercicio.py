import random
import matplotlib.pyplot as plt
import numpy as np


def diagrama_barras_calificaciones(notas,color,alumno):
    """
    Dibujar la grafica de barras con las calificaciones
    """
    plt.bar(notas.keys(),notas.values(),color = color)
    plt.title("Calificaciones de " + alumno)


calificaciones = {
    "Programacion": 3,
    "Español": 6.5,
    "Calculo": 4,
    "Historia": 8,
    "Biologia": 10,
    "Ingles": 3
}

alumno = input("Nombre del alumno: ")
diagrama_barras_calificaciones(calificaciones, "red", alumno)

plt.show()
