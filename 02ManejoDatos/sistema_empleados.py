
nombre_empleado = input('Introduce nombre del empleado: ')
edad_empleado = int(input('Introduce la edad del empleado: '))
salario_empleado = float(input('Introduce el salario del empleado: '))
es_jefe_departamento = input('¿Es jefe de departamento?: (Si/No)')

#Convertir a bool sí es jefe
es_jefe_departamento = es_jefe_departamento.lower()== 'si'

print('\n', '*'*3, 'SISTEMA DE EMPLEADOS', '*'*3)
print('Datos del empleado:')
print(f'Nombre de empleado: {nombre_empleado}')
print(f'Edad de empleado: {edad_empleado}')
print(f'Salario de empleado: {salario_empleado:.2f}')
print(f'Jefe de departamento: {es_jefe_departamento}')

