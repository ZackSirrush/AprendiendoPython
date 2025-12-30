print('\n','*'*5, 'Playlist de canciones', '*'*5,'\n')

lista_calif = [] #Crea lista vacía
numero_calif = int(input('Proporciona el no. de calificaciones a evaluar: '))
for indice in range(numero_calif):
    calificacion = float(input(f'Calificación [{indice+1}]: '))
    lista_calif.append(calificacion)

print(f'\nLista de calificaciones: {lista_calif}')

suma_calificaciones = sum(lista_calif)
promedio = suma_calificaciones / numero_calif

print(f'Promedio de calificaciones: {promedio:.2f}')
