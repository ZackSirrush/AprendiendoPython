print('\n','*'*5, 'Generadores en Python', '*'*5,'\n')

def generador(maximo):
    contador = 0
    while contador <= maximo:
        yield contador
        contador += 1

#Crea un generador
var_generador = generador(10)

#iterar sobre el generador
for valor in var_generador:
    print(valor)