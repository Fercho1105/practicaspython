import random


# #Dado aleatorio entre 1 y 6
# print("El dado dio: " + str(random.randint(1,6)))

#################################################################################


#Dado aleatorio pero en "n" numero de tiros

def tiro_dado(numero_tiros):
    for dado in range(numero_tiros):
        print("El dado " + str(dado +1) + " dió " + str(random.randint(1,6)))


tiro_dado(5)