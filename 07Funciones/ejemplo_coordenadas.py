print('\n','*'*5, 'Obtener coordenadas x, y, z', '*'*5,'\n')

def obtener_coordenadas():
    x,y,z = 10,20,30
    return x,y,z

#Llamar función
resultado = obtener_coordenadas()
print(f'Las coordenadas son: {resultado}')

#Unpacking
x1, y1, z1 = resultado
print(f'La coordenada X es: {x1}')
print(f'La coordenada Y es: {y1}')
print(f'La coordenada Z es: {z1}')