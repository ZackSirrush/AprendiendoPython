print('**** SISTEMA DE DESCUENTOS VIP ****')

NO_PROD_DESCUENTO = 10
cantidad_prod = int(input('¿Cuantos productos compraste hoy? '))
membresia = input('¿Tienes membresía de la tienda? (si/no)')

es_elegible = (cantidad_prod >= NO_PROD_DESCUENTO
               and membresia.strip().lower() == 'si')

print(f'¿Tienes acceso al descuento VIP?: {es_elegible}')