print('\n','*'*5, 'Alcance de variables', '*'*5,'\n')

#Variable global accesible por cualquier metodo
contador_global = 0

def incrementar_contador():
    #Variable local accesible solo por función "incremento_contador"
    contador_local = 0
    #Usar variable global
    global contador_global
    contador_global += 1 # Incrementar variable global
    contador_local += 1 #Incrementar variable local
    print(f'Contador local: {contador_local} Se reinicia con cada llamada')
    print(f'Contador global: {contador_global}\n')

#Llama varias veces la función
incrementar_contador()
incrementar_contador()
incrementar_contador()

print(f'Valor final de variable global: {contador_global}')