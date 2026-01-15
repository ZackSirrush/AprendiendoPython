print('\n','*'*5, 'Función SUM y NEXT en Python', '*'*5,'\n')

lista = [1,2,3,4,5]

#suma de los elementos
resultado = sum(lista)
print(f'Resultado de la suma: {resultado}')

#Proporcionar valor inicial
resultado = sum(lista,20)
print(f'Resultado de la suma con valor inicial 20: {resultado}')

#Función NEXT
iterador = iter(lista)
#Obtiene prximo elemento del iterador
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')
print(f'Siguiente elemento del iterable: {next(iterador)}')