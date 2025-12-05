print('*'*3, 'SISTEMA SALUD FITNESS', '*'*3)

META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 #VALOR APROX SIN CALORIAS

nombre = input('Ingrese su nombre: ')
pasos_caminados = int(input('Ingrese cuantos pasos caminó hoy: '))

meta_alcanzada = pasos_caminados >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'

#Calcular calorias quemadas
calorias_quemadas = pasos_caminados * CALORIAS_POR_PASO

print(f'\nUsuario: {nombre}')
print(f'Pasos dados hoy: {pasos_caminados}')
print(f'Calorías quemadas: {calorias_quemadas} kcal')
print(f'Meta de pasos diarios alcanzados: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de: {META_PASOS_DIARIOS} pasos')