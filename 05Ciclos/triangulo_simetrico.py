print('*'*10,'DIBUJAR UN TRIÁNGULO SIMÉTRICO','*'*10,'\n')

numero_filas = int(input('Introduce el número de filas: '))

#Iterar sobre cada fila
for fila in range(1, numero_filas+1):
    espacios_blanco = ' '*(numero_filas-fila)
    asteriscos = '@'*(2*fila-1)
    print(f'{espacios_blanco}{asteriscos}')