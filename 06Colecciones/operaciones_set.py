print('\n','*'*5, 'Operaciones con set', '*'*5,'\n')

a= {1,2,3,4}
b={3,4,5,6}

union = a|b #Une 2 sets en uno
print(f'Unión a | b: {union}')

interseccion = a&b #Valores coincidentes en ambos sets
print(f'Intersección a & b: {interseccion}')

diferencia = a-b #Resta sets duplicados del segundo conjunto en el primero
print(f'Diferencia a - b: {diferencia}')