import m_factorial as mf  #Importamos el modulo "m_factorial" con "import", y le asignamos un alias, con "as"

# para importar un objeto de un modulo usamos "from"
#EJEMPLO
"""
from m_factorial import factorial  

Importamos la funcion "factorial", del modulo "m_factorial"

"""

fact5 = mf.factorial(5)  #Lamamos al modulo importado con el alias, y la funcion a utlizar del modulo importado

print(f"El factorial de 5 es {fact5}")