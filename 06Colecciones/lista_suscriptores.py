print('\n','*'*5, 'Lista de suscriptores', '*'*5,'\n')

#Set inicial
suscriptores = set()

numero_suscriptores = int(input('Ingrese el número de suscriptores iniciales: '))

for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))


print(f'Lista de suscriptores inicial: {suscriptores}')

nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El suscriptor {nuevo_suscriptor} ya está en la lista')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor {nuevo_suscriptor} se agregó correctamente a la lista de suscriptores')

print(f'Lista de suscriptores: {suscriptores}')

#Eliminar suscriptor
suscriptor_eliminar = input('Proporciona el suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)

print(f'\nEl suscriptor {suscriptor_eliminar} se ha eliminado de la lista')
print(f'Lista de suscriptores: {suscriptores}')

#Verificar total de suscriptores
print(f'Cantidad total de suscriptores: {len(suscriptores)}')

#Mostrar suscriptores
print(f'\n---- Lista de suscriptores ----')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')