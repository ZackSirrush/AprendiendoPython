numero = 10
texto = 'Hola, mundo'

x, y, z = 15,'Saludos',-18.51 #Asignación múltiple

print(f'El valor número es: {numero}')
print(f'El valor de cadena es: {texto}')
print(f'Valor de x= {x}, y = {y}, z = {z}')

a = b = c = 10 #Asignación encadenada
print(f'\nEl valor de a = {a}, b = {b}, c = {c}')

#Intercambio de valores sin variables temporales
x, y = 5, 10
print(f'El valor inicial de x= {x}, y = {y}')
x, y = y, x
print(f'El nuevo valor de x= {x}, y = {y}')

#Recibir multiples valores por entrada de datos
nombre, apellido = input('Ingrese nombre y apellidos separados por coma (,): ').split(',')
print(f'El nombre es: {nombre.strip()}, el apellido es: {apellido.strip()}')