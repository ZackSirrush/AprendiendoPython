print('*'*3, 'SISTEMA PARA CONVERTIR CALIFICACIONES', '*'*3)

calificacion = float(input('Ingrese una calificación entre 0 y 10: '))

if calificacion >= 9 and calificacion <= 10:
    calificacion_txt = 'A'
elif calificacion >= 8 and calificacion < 9:
    calificacion_txt = 'B'
elif calificacion >= 7 and calificacion < 8:
    calificacion_txt = 'C'
elif calificacion >= 6 and calificacion < 7:
    calificacion_txt = 'D'
elif calificacion >= 0 and calificacion < 6:
    calificacion_txt = 'F'
else:
    calificacion_txt = 'VALOR DESCONOCIDO'

print(f'La calificación de {calificacion:.2f} es igual a {calificacion_txt}')