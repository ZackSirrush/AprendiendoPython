#Operadores de comparación
from enum import nonmember

a, b = 7, 5
print(f'Valor inicial a: {a}, b: {b}')

resultado = a == b #Operador de igualdad bool
print(f'Resultado de a = b: {resultado}')

resultado = a != b #Operador diferente !=
print(f'Resultado de a != b: {resultado}')

resultado = a > b #Operador mayor que
print(f'Resultado de a > b: {resultado}')

resultado = a <= b #Operador menor o igual que
print(f'Resultado de a <= b: {resultado}')

#Operadores lógicos
dato1 = False
dato2 = True
print(f'¿Son dato 1 y dato 2 iguales?: {dato1 and dato2}') #False
print(f'¿Son dato 1 y dato 2 diferentes?: {dato1 or dato2}') #OR regresa True si cualquier valor es verdadero

dato1 = not dato1 #Not invierte los valores del bool
dato2 = not dato2
print(f'Las variables se invierten con NOT: {dato1} {dato2}')
#ejemplo de not
nombre = ''
es_cadena_vacia = not nombre
print(f'¿La variable es cadena vacía ? {es_cadena_vacia}')

variable = None
es_variable_sin_valor = not variable
print(f'\n¿La variable es sin valor? {es_variable_sin_valor}')

