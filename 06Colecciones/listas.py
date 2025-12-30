print('*'*5, 'Manejo de listas', '*'*5,'\n')
lista = [1,2,3,4,5]

print(f'{lista} -> Lista original')

#Largo de lista
print(f'Largo de lista: {len(lista)}')
#Acceder a elemento por indice
print(f'Acceder al valor del índice 3: {lista[3]}')
print(f'Acceder a último índice de la lista: {lista[-1]}')

#Modificar elementos de la lista
lista[1] = 10
print(f'Lista modificada v1: {lista}')

#Agregar elementos en la lista
lista.append(20)
print(f'Lista modificada v2: {lista}')

#Añadir elemento en índice especifico
lista.insert(3, 30)
print(f'Se añadió el valor de 30 en índice 3: {lista}')

#Eliminar elementos de una lista
lista.remove(30) #Elimina el valor deseado
print(f'Se remueve el valor 30: {lista}')

lista.pop(1) #Remueve el elemento del índice 1
print(f'Se remueve el elemento del índice 1: {lista}')

del lista[0] #Remueve el indice con del
print(f'Se elimina el índice 0 de la lista: {lista}')

#Obtener sublistas
sublista = lista[1:3] #Genera sublista del índice 1 al 2 (3 no se incliye)
print(f'Sublista [1:3]: {sublista}')