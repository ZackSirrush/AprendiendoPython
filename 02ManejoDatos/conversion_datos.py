#Convertir tipos de datos

numero_cadena = "100"

numero_entero = int(numero_cadena) #convierte cadena a entero
print("Número entero multiplicado: ", numero_entero*2)

numero_decimal = float(numero_cadena) #convierte a float
print("Número float multiplicado: ", numero_decimal*1.2)

numero_texto = str(numero_cadena) #Convierte a string nuevamente
print("Número decimal a string: ", numero_texto)

#Funcion bool
print(f"Valor 0: {bool(0)}") #False, 0 es falso
print(f"Valor 1: {bool(1)}") #True, un valor diferente a 0 es True
print(f"Valor '': {bool('')}") #Cadena vacía es falso
print(f"Valor 'Hola': {bool('Hola')}") #Cadena con datos es True
print(f"Valor 'none': {bool(None)}") #None se considera sin valor

#Concatenación o suma de valores
numero1_cadena = '10'
print(f'Número 1 en cadena: {numero1_cadena}')
numero2_cadena = '20'
print(f'Número 2 en cadena: {numero2_cadena}')
resultado = numero1_cadena + numero2_cadena
print(f'Concatenación: {resultado}')

#Conversión a int
numero1_entero = int(numero1_cadena)
numero2_entero = int(numero2_cadena)
resultado = numero1_entero + numero2_entero
print(f'Suma: {resultado}')

numero1_float = 38.7
resultado = numero1_float + numero2_entero
print(f'Suma float + int: {resultado}')