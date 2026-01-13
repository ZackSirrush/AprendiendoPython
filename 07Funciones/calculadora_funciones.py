print('\n','*'*5, 'Calculadora con funciones', '*'*5,'\n')

def mostrar_menu():
    print(f''' --- Operaciones ---
            1. Suma
            2. Resta
            3. Multiplicación
            4. Division
            5. Salir''')
    return int(input('\nElige una opcion: '))

def pedir_valores():
    operando1 = float(input('Ingrese el valor 1: '))
    operando2 = float(input('Ingrese el valor 2: '))
    return operando1, operando2

def ejecutar_operacion(opcion, salir):
    #Solicitar operandos
    if 1 <= opcion <= 4:
        operando1, operando2 = pedir_valores()
    resultado = 0
    if opcion == 1: #Sumar
        resultado = operando1 + operando2
        print(f'El resultado de {operando1} + {operando2} es: {resultado}\n')
    elif opcion == 2:
        resultado = operando1 - operando2
        print(f'El resultado de {operando1} - {operando2} = {resultado}\n')
    elif opcion == 3:
        resultado = operando1 * operando2
        print(f'El resultado de {operando1} * {operando2} = {resultado}\n')
    elif opcion == 4:
        resultado = operando1 / operando2
        print(f'El resultado de {operando1} / {operando2} = {resultado}\n')
    elif opcion == 5:
        print('Cerrando sistema...')
        salir = True
    else:
        print('Opcion no valida')
    return salir

#Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)