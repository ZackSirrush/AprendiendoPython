print('\n','*'*10,'CICLOS BREAK Y CONTINUE','*'*10,'\n')

print('Palabra break: \n')
#Ejemplo con break
for numero in range(1,10):
    if numero % 2 == 0: #Solo imprime los número que sean pares (por tener residuo 0 al dividir entre 2)
        print(numero)
        break #Sale del ciclo al encontrar el primer número par en el ciclo For

print('Palabra continue: \n')
#Ejemplo con continue
for numero in range(1,10):
    if numero % 2 == 1: #Busca los números nones (por tener residuo 1 al dividir entre 2)
        continue #Omite el número non al encontrarlo y continua
    print(numero) #Solo imprime pares