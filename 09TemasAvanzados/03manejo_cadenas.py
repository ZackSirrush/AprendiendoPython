#Manejo de cadenas
#Dividir una cadena
cadena = 'Hola Mundo'
palabras = cadena.split() #Genera una lista separando cadenas por defecto espacio
palabra = cadena.split('M') #Se puede elegir el separador
print(palabras)
print(palabra)

#Buscar y remplazar
posicion = cadena.find('Mundo') #devuelve el valor de 5 (donde empieza)
print(f'Posición de la cadena "Mundo": {posicion}')

#Reemplazar con replace
nueva_cadena = cadena.replace('Mundo', 'Python')
print(f'Nueva cadena reemplazada: {nueva_cadena}')

#Multiplicación de cadenas
cadena2 = 'Hola '
resultado_multiplicacion_cadena = cadena2*3
print(f'Resultado multiplicación de cadena: {resultado_multiplicacion_cadena}')

#Funcion strip limpia espacios en blanco, tabulaciones inicio y fin
cadena3 = '    Hola Mundo   '
cadena4 = '....Hola Mundo.....'
cadena_limpia = cadena3.strip()
cadena_limpia2 = cadena4.strip('.')
print(f'Cadena limpia de caracteres en inicio y fin: {cadena_limpia}')
print(f'Cadena limpia de caracteres "." en inicio y fin: {cadena_limpia2}')
