print('\n','*'*5, 'Expresiones generadoras en Python', '*'*5,'\n')

generador = (x**2 for x in range(11) if x % 2 != 0)

for cuadrado_nones in generador:
    print(cuadrado_nones)