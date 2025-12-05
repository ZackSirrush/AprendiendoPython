print('*'*3, 'SENTENCIA IF PARA NÚMEROS POSITIVOS', '*'*3)

numero = int(input('Ingresa un número: '))

if numero > 0:
    print(f'Número es positivo: {numero}')
elif numero < 0:
    print(f'Número negativo: {numero}')
else:
    print(f'Número es cero: {numero}')