import random

print(f'\n', '-'*7, 'GENERADOR DE ID ÚNICOS', '-'*7, '\n')
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
ano_nacimiento = input('Ingrese su año de nacimiento (YYYY): ')
num_aleatorio = random.randint(1000, 9999)
nombre_letras = nombre.strip().upper()[0:2]
apellido_letras = apellido.strip().upper()[0:2]
ano_digitos = ano_nacimiento.strip()[2:]
id_unico = f'{nombre_letras}{apellido_letras}{ano_digitos}{num_aleatorio}'

print(f'\nHola {nombre}, ')
print(f'\t Tu número de identificación (ID) generado por el sistema es:\n\t {id_unico}')
print(f'¡Bienvenido!')