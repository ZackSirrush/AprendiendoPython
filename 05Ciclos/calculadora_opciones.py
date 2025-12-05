print('*'*10,'CALCULADORA CON MENÚ','*'*10,'\n')

salir = False

while not salir:
    print(f'''Operaciónes que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. Dividir
    5. Salir''')

    opcion = int(input('\nElige una opción: '))

    if 1<= opcion <= 4:
        numero1 = float(input('Dame el primer número: '))
        numero2 = float(input('Dame el segundo número: '))
    if opcion == 1:
        suma = numero1 + numero2
        print(f'\nEl resultado de sumar {numero1:.2f} + {numero2:.2f} es: {suma:.2f}\n')
    elif opcion == 2:
        resta = numero1 - numero2
        print(f'\nEl resultado de restar {numero1:.2f} - {numero2:.2f} es: {resta:.2f}\n')
    elif opcion == 3:
        multiplicacion = numero1 * numero2
        print(f'\nEl resultado de multiplicar {numero1:.2f} * {numero2:.2f} = {multiplicacion:.2f}\n')
    elif opcion == 4:
        division = numero1 / numero2
        residuo = numero1 % numero2
        print(f'\nEl resultado de dividir {numero1:.2f} / {numero2:.2f} es: {division:.2f}')
        print(f'El residuo es: {residuo:.2f}\n')
    elif opcion == 5:
        salir = True
        print(f'Saliendo del sistema...\n')
    else:
        print(f'Ingrese una opción válida\n')
else:
    print(f'Sistema cerrado\n')