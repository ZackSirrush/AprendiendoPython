print('\n','*'*5, 'Ordenamiento en Python', '*'*5,'\n')

#Sintaxis: sorted(iterable, key = None, reverse = False)

empleados = ['Juan', 'Pedro', 'Maria']
#Ordenar lista
#empleado_ordenados = sorted(empleados, reverse=True)
empleado_ordenados = sorted(empleados)
print(f'Empleados ordenados: {empleado_ordenados}')

#Ordenar dict con una llave
empleados_dict = [
    {'nombre':'Juan','salario':3000},
    {'nombre':'Maria','salario':2500},
    {'nombre':'Pedro','salario':3500},
]

empleados_ordenados_por_salario = sorted(empleados_dict, key=lambda x: x['salario'])
print(f'\nEmpleados ordenados por salario: {empleados_ordenados_por_salario}')