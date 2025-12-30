print('\n','*'*5, 'Manejo de Sets/Conjuntos', '*'*5,'\n')
#Los sets eliminan duplicados

mi_set = {1,2,3,4,5,4}
print(f'Mi set: {mi_set}')

#Agregar elementos al set no agrega elementos duplicados
mi_set.add(6)
mi_set.add(7)
print(f'Mi set modificado: {mi_set}')

#Eliminar un elemento
mi_set.remove(4)
print(f'Mi set eliminado: {mi_set}\n')

#Iterar elementos del set
for elem in mi_set:
    print(elem, end=' ')

#Comprobar sí existe un elemento
print(f'\n¿Existe el valor 4 en el set?: {4 in mi_set}')
print(f'\n¿Existe el valor 1 en el set?: {1 in mi_set}')

#Obtener longitud del set
print(f'La longitud del set/conjunto es: {len(mi_set)}')