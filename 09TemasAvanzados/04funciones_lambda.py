from functools import reduce

print('\n','*'*5, 'Funciones Lambda', '*'*5,'\n')

#Funcion cuadrado sin lambda
def cuadrado(x):
    return x**2

print(f'El cuadrado de 5 es: {cuadrado(5)}')

#Función lambda
cuadrado_lambda = lambda x: x**2
print(f'El cuadrado de 2 es: {cuadrado_lambda(2)}')

#Map y lambda para lista de numeros

numeros = [1,2,3,4,5]

#Aplicar funcion para obtener el cuadrado de cad numero
cuadrados = list(map(lambda x:x**2, numeros))

print(f'\nResultado de map + lambda: {cuadrados}')

#Filter + lambda
nones = list(filter(lambda x: x % 2 != 0, numeros))
print(f'\nResultado de filter para nones + lambda: {nones}')

#Reduce + map
suma_acumulativa = reduce(lambda x, y: x + y, numeros)
print(f'\nSuma acumulativa con reduce: {suma_acumulativa}')