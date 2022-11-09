import m_alumnos as m3

numero_alumnos = input("¿ Cuántos alumnso desea registrar? ")
if numero_alumnos.isdigit() :
    numero_alumnos = int(numero_alumnos)
    m3.captura(numero_alumnos)
else :
    m3.captura()