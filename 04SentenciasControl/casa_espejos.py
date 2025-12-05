print('*'*3, 'CASA DE LOS ESPEJOS', '*'*3)
#Condiciones
EDAD_MINIMA = 10

edad = int(input('¿Cual es tu edad?: '))
miedo_oscuridad = input('¿Tienes miedo a la oscuridad?: ')
miedo_oscuridad = miedo_oscuridad.strip().lower() == 'si'

if not miedo_oscuridad and edad >= EDAD_MINIMA:
    print('Puedes entrar a la casa de los espejos')
else:
    print('Lo siento, no puedes ingresar a la casa de los espejos')