print('\n','*'*5, 'Comprensión de listas', '*'*5,'\n')

#Filtrar pares y genera lista con estos valores
numeros = range(1,10+1)
#Sin usar comprensión de listas
numeros_pares = []
#iterar elementos de la lista
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(f'Numeros pares del 1 al 10: {numeros_pares}')

#Usando comprensión de listas
#sintaxis: nueva_lista = [expresion for elemento in iterable if condicion]
numeros_nones = [numero for numero in numeros if numero % 2 != 0]
print(f'Numeros nones del 1 al 10: {numeros_nones}')
