print('*'*3, 'SISTEMA LOGIN', '*'*3)

USUARIO = 'Admin'
PASSWORD = 'Admin1234'

usuario_inp = input('Ingrese su usuario: ')
contrasena = input('Ingrese su contraseña: ')

if usuario_inp == USUARIO and contrasena == PASSWORD:
    print(f'¡Bienvenido {usuario_inp}!')
else:
    print(f'Usuario o contraseña incorrectos')
