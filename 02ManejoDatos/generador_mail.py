nombre = input('Ingresa tu nombre(s): ')
apellidos = input('Ingresa tus apellidos: ')
nombre_empresa = input('Ingresa el nombre de la empresa: ')
extension_dominio = input('Ingresa la extension de dominio: ')

nombre = nombre.strip().lower().replace(' ', '.')
apellido = apellidos.strip().lower().replace(' ', '.')
nombre_empresa = nombre_empresa.strip().lower().replace(' ', '')
dominio_correo = f'@{nombre_empresa}{extension_dominio}'

correo = f'{nombre}.{apellido}{dominio_correo}'

print(f'Tu correo generado por el sistema es: {correo}')

