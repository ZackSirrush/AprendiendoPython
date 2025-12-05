print('*'*3, 'SISTEMA DE RESERVAS DE HOTEL', '*'*3)

HABITACION_SIN_VISTA = 150.50
HABITACION_CON_VISTA = 190.50

nombre = input('Ingrese su nombre: ')
dias_estancia = int(input('¿Cuántos días quiere reservar?: '))
vista_mar = input('¿Desea una habitación con vista al mar? (Si/No): ')

print('\n---------------- DETALLES DE RESERVACIÓN ----------------')
print(f'Cliente: {nombre}')
print(f'Días de estancia: {dias_estancia}')
print(f'Habitación con vista al mar: {vista_mar.strip().upper()}')
if vista_mar.strip().upper() == 'SI':
    costo_total = dias_estancia * HABITACION_CON_VISTA
else:
    costo_total = dias_estancia * HABITACION_SIN_VISTA
print(f'Costo total: ${costo_total:.2f}')