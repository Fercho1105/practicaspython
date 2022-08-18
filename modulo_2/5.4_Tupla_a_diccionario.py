""" Casteo de Tupla a diccionario"""

#Usamos dict() y hacemos el diccionario

tiempos = dict(
    Hamilton = "1:49.8",
    Bottas = "1.56.4",
    Perez = "1:53.8",
    Verstappen = "1:52.6"
)

print(tiempos)


""" Errores y duplicados"""
#******
# Esta da error ya que el diccionario no puede tener claves duplicadas 
#******
# tiempos = dict(
#     Hamilton = "1:49.8",
#     Bottas = "1.56.4",
#     Hamilton = "1:53.8",
#     Verstappen = "1:52.6"
# )


#******
# Pero si se puede tener valores duplicados
#*****
# tiempos = dict(
#     Hamilton = "1:49.8",
#     Bottas = "1.56.4",
#     Perez = "1.56.4",
#     Verstappen = "1:52.6"
# )