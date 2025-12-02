print('*'*3, 'SISTEMA PARA DETERMINAR SI SE ENCUENTRA EN RANGO UN VALOR', '*'*3)
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

dato = int(input('Proporciona un número entero: '))
en_rango = dato >= VALOR_MINIMO and dato <= VALOR_MAXIMO

print(f'¿El número {dato} está dentro del rango entre 1 y 5?: {en_rango}')