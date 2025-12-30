print('\n','*'*5, 'Playlist de canciones', '*'*5,'\n')

lista_reproduccion = [] #Crea lista vacía

numero_canciones = int(input('¿Cuántas canciones deseas agregar?: '))
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la cancion {indice+1}: ')
    lista_reproduccion.append(cancion)

#Ordena lista de reproducción por orden alfabético
lista_reproduccion.sort() #Orden normal

print(f'\nLista de reproducción en orden alfabético:')
for cancion in lista_reproduccion:
    print(f'- {cancion}')

# lista_reproduccion.sort(reverse=True) #Orden desendente
# print(f'\nLista de reproducción en orden inverso:')
#for cancion in lista_reproduccion:
    # print(f'- {cancion}')