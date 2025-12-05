print('*'*3, 'SISTEMA PARA IDENTIFICAR EL MAYOR DE 2 NÚMEROS', '*'*3)

numero1 = int(input('Ingrese el número 1: '))
numero2 = int(input('Ingrese el número 2: '))

if numero1 > numero2:
    print(f'El número 1 es mayor que el número 2 => {numero1} > {numero2}')
else:
    print(f'El número 2 es mayor que el número 1 => {numero2} > {numero1}')