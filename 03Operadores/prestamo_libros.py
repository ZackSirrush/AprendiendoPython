print('*** SISTEMA PRESTAMO DE LIBROS')

DISTANCIA_PERMITIDA = 3
credencial = input('¿Tienes credencial de estudiante? (Si/No)')
distancia = int(input('¿A cuantos KM vives de la biblioteca?'))

es_elegible = (credencial.strip().lower() == 'si'
               or distancia <= DISTANCIA_PERMITIDA)

print(f'¿El usuario es elegible para préstamo?: {es_elegible}')