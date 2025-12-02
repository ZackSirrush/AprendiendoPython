dato = int(input('Proporciona un número entero: '))
en_rango = 1 <= dato <= 10
print(f'Variable está dentro del rango entre 1 y 10: {en_rango}')

#Lógica inversa
fuera_rango = not(1 <= dato <= 10)
print(f'Variable está fuera del rango entre 1 y 10: {fuera_rango}')

#Precedencia, los operadores se priorizan con:
# 1. Parentesis ()
# 2. Exponente **
# 3. Unario (positivo o negativo) + -x
# 4. Operaciones (Mult *, Div /, Div int//, Módulo %)
# 5. Sumas y restas (+ -)
# 6. Comparación == != < <= > >=
# 7. Lógicos Not and or
# 8. Asignación = /= += -=

#1. División, 2. Multiplicación, 3. Suma, 4. Resta
resultado = 12 // (3 + 2) * 3 - 1
print(f'\n\nResultado: {resultado}')