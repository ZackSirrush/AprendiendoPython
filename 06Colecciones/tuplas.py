print('\n','*'*5, 'Manejo de Tuplas/Tuple', '*'*5,'\n')

#Similar a listas pero inmutables (no cambiarán)
mi_tupla = (1,2,3,4,5)
print(mi_tupla)

#Iterar elementos en la tupla
for elemento in mi_tupla:
    print(elemento, end=' ')

#Crear tupla para coordenada X, Y
coordenadas = (3, 5)
print(f'\nCoordenada en el eje X: {coordenadas[0]}')
print(f'Coordenada en el eje Y: {coordenadas[1]}')

#Crear tupla unitaria
tupla_un_elemento = 10,
print(f'Tupla de un elemento: {tupla_un_elemento}')

#Tupla anidada
tupla_anidada = (1, (2,3), (4,5))
print(f'Tupla anidada: {tupla_anidada}')
print(f'Segundo elemento: {tupla_anidada[1]}')