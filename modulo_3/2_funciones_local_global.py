# Probando ámbitos
titulo =  "Probando ámbitos"
suma = 10.5
def sumar ( ) :
    suma = 2 + 2
    titulo = titulo + ' mundo '
    print ( titulo )
    print ( " Suma en ambito local ", suma , id ( suma ) )

    
print ( ' Antes de llamar a la función ' )
print ( ' Suma en ambito global ' , suma , id ( suma ) )
sumar()
print ( ' Después de llamar a la función sumar ' )
print ( ' Suma en ambito global ' , suma , id ( suma ) )