print('*'*10,'REPETICIÓN DE UN MENSAJE','*'*10,'\n')

mensaje = input('Introduce un mensaje a repetir: ')
numero_repeticiones = int(input('Introduce el número de repeticiones: '))

#Iterar repeticiones
for i in range(numero_repeticiones):
    print(f'Repetición {i+1}: {mensaje}')

for _ in range(numero_repeticiones): #Guión bajo se usa para indicar que el valor no se utiliza
    print(f'{mensaje}')