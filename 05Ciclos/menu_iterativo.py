print('*'*10,'SISTEMA DE ADMINISTRACION DE CUENTAS','*'*10,'\n')

salir = False


while not salir:
    print(f'''Menú:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir''')
    opcion = int(input('Elige una opción del menú: '))
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('Eliminando tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo...\n')
        salir = True
    else:
        print('Proporciona una opción válida\n')
else:
    print('Cerrando sistema...\n')