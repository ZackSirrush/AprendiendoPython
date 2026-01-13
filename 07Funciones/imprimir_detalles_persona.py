print('\n','*'*5, 'Imprimir detalles de una persona usando kwargs', '*'*5,'\n')

def imprimir_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')

#Llamado a la función
imprimir_persona(nombre='Karla', edad=30, ciudad='México')
imprimir_persona(nombre='Carlos', edad=28, ciudad='Guadalajara', puesto='Gerente')