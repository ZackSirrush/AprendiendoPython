print('\n','*'*5, 'Suma con argumentos variables', '*'*5,'\n')

def suma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

#Llamar función sumar
resultado = suma(1,2,3,4,5)
print(f'Resultado de la suma: {resultado}')

resultado = suma(1,2,3,4,5,6,7,8,9)
print(f'Resultado de la suma: {resultado}')