print('*'*10,'VALIDACIÓN CAMPO DE UN FORMULARIO','*'*10,'\n')

nombre_usuario = None

while not nombre_usuario:
    nombre_usuario = input('Ingresa tu nombre de usuario: ')

print(f'Nombre de usuario válido: {nombre_usuario}')