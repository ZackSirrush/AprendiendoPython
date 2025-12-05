print('*'*10,'SISTEMA CAJERO AUTOMATICO','*'*10,'\n')

saldo = 1000
salir = False

while not salir:
    print(f'''Opciones por realizar:
        1. Consultar saldo
        2. Retirar
        3. Depositar
        4. Salir''')
    opcion = int(input('Elige una opción: '))
    if opcion == 1:
        print(f'Tu saldo disponible es: ${saldo:.2f}\n')
    elif opcion == 2:
        retiro = float(input('¿Cuanto quieres retirar?: '))
        if retiro <= saldo:
            saldo -= retiro #saldo = saldo - retiro
            print(f'Tu nuevo saldo disponible es: ${saldo:.2f}\n')
        else:
            print(f'No cuentas con saldo suficiente. Tu saldo disponible es: ${saldo:.2f}\n')
    elif opcion == 3:
        deposito = float(input('Ingresa el monto por depositar: '))
        saldo += deposito #saldo = saldo + deposito
        print(f'Tu nuevo saldo disponible es: ${saldo:.2f}\n')
    elif opcion == 4:
        print('Saliendo del sistema. Hasta pronto!\n')
        salir = True
    else:
        print('Opcion no valida, selecciona otra opción.\n')
else:
    print('Aplicación cerrada')