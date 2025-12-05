print('*'*3, 'SISTEMA CON COSTO DE ENVÍOS', '*'*3)

TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

destino = input('Ingrese el tipo de destino para su envío (nacional/internacional): ')
peso = float(input('Ingrese el peso del envío (en kg): '))

costo_envio = None

if destino.upper().strip() == 'NACIONAL':
    costo_envio = peso * TARIFA_NACIONAL
elif destino.upper().strip() == 'INTERNACIONAL':
    costo_envio = peso * TARIFA_INTERNACIONAL
else:
    print(f'El destino {destino.upper()} no es valido')

if costo_envio is not None:
    print(f'El costo de envio del paquete es: ${costo_envio:.2f}')