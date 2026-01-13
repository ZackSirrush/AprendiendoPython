print('\n','*'*5, 'Potencia de un número con recursividad', '*'*5,'\n')

#Función factorial recursiva
def potencia(base, exponente):
    #Caso base, factorial 0! = 1, 1! = 1
    if exponente == 0:
        return 1
    else: #caso recursivo
        return base * potencia(base, exponente - 1)

print(f'2 elevado a la 3: {potencia(2,3)}')
print(f'5 elevado a la 0: {potencia(5,0)}')
print(f'4 elevado a la 5: {potencia(4,5)}')