año_actual=int(input('Ingresa el año actual:'))
año_cualquiera=int(input('Ingresa un año cualquiera:'))
diferencia_años=año_actual-año_cualquiera
if diferencia_años>0:
   if diferencia_años ==1:
        print(f'Ha pasado un año desde {año_cualquiera}')
   else:
       print(f'Han pasado {diferencia_años} años desde {año_cualquiera}')

elif diferencia_años<0:
    if diferencia_años == -1:
        print(f'Falta un año para {año_cualquiera}')
    else:
        print(f'Faltan {diferencia_años*-1} años para {año_cualquiera}')

else:
    print(f'Son el mismo año: {año_cualquiera}')