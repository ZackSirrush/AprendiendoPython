print('*'*3, 'SISTEMA BANCARIO, BANCO XXX', '*'*3)

salir_sistema_txt = input('¿Deseas salir del sistema? (Si/No) ')
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print('Continua con tus operaciones')
else:
    print('Saliendo del sistema')