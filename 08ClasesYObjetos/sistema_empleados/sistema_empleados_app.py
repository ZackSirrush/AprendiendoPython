from sistema_empleados.empleado import Empleado
from sistema_empleados.empresa import Empresa

print('\n','*'*5, 'Sistema de empleados', '*'*5,'\n')

empresa1 = Empresa('Lagion')

#contrata empleados
empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('María', 'Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Ana', 'Recursos Humanos')

print(f'Total de empleados: {Empleado.obtener_total_empleados()}')

# Empleados por dpto de vtas
print(f'Empleados en ventas: '
      f'{empresa1.obtener_numero_empleados_departamento('Ventas')}')

# MOSTRAR EMPLEADOS DE EMPRESA 1
empresa1.obtener_total_empleados()