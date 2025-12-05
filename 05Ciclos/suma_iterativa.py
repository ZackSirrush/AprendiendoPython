print('*'*10,'SUMA ITERATIVA','*'*10,'\n')
MAXIMO = 10
numero = 1
acumulador_suma = 0

MAXIMO = 10
numero = 1
acumulador_suma = 0

while numero <= MAXIMO:
    print(f'(acumulador_suma + numero) -> {acumulador_suma} + {numero}')
    acumulador_suma += numero
    numero += 1
    print(f'Suma parcial acumulada: {acumulador_suma}\n')

print(f'\nResultado: {acumulador_suma}')