#Declara variables
cadena = input('Ingresa una frase: ') #Cadena
contador = 0 #Contador para vocales
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ" #Vocales por contar

# Agregar el ciclo for
for caracter in cadena: #caracteres en cadena
    if caracter in vocales: #Sí cadena tiene alguna letra de las vocales
        contador += 1 #Contador suma uno

# Imprimir la cantidad de vocales encontradas en la cadena
print(f'Las vocales de la cadena "{cadena}" son: {contador}')