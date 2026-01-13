print('\n','*'*5, 'Imprimir del 1 al 5 de forma recursiva', '*'*5,'\n')

#Definir función
def funcion_recursiva(numero):
    #Caso base
    if numero == 1:
        print(numero, end=' ')
    else: #Caso recursivo
        funcion_recursiva(numero-1)
        print(numero, end=' ')

#Programa principal
funcion_recursiva(5)