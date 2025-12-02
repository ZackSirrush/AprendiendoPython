print('*'*3, 'SISTEMA DE AUTENTICACION', '*'*3)

USUARIO_VALIDO = 'Admin'
CONTRASENA_VALIDA = 'Admin1234'

usuario = input('Introduce tu usuario: ')
contrasena = input('Ingresa tu contraseña: ')

user_correcto = (usuario == USUARIO_VALIDO
                 and contrasena == CONTRASENA_VALIDA)

print(f'¿Datos correctos?: {user_correcto}')