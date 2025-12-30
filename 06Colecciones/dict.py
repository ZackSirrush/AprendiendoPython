print('\n','*'*5, 'Diccionarios/Dict', '*'*5,'\n')

#Creacion de dict
persona = {'nombre':'Isaac',
           'edad':30,
           'ciudad':'México',
           'profesion': 'Ingeniero'
           }

print(f'Diccionario de persona: {persona}')

#Acceder a los elementos del diccionario
print(f'Nombre: {persona['nombre']}')
print(f'Edad: {persona.get('edad')}')
print(f'Ciudad: {persona['ciudad']}')
print(f'Profesión: {persona['profesion']}')

#Modificar valores en dict
persona['edad'] = 35
print(f'Diccionario de persona: {persona}')

#Agregar elemento al diccionario
persona['estatura'] = '1.70 mts'
print(f'Diccionario de persona: {persona}')

#Eliminar elementos en dict
del persona['ciudad']
print(f'Diccionario de persona: {persona}')
persona.pop('profesion')
print(f'Diccionario de persona: {persona}')

#Iterar elementos de un dict (llave, valor)
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

#Obtener los valores
print(f'\nValores del diccionario:')
for valor in persona.values():
    print(f'- Valor: {valor}')

#Obtener llaves
print(f'\nImpresión de llaves del diccionario: ')
for llave in persona.keys():
    print(f'- Llave: {llave}')