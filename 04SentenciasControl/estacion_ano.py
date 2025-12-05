print('*'*3, 'ESTACIÓN DEL AÑO', '*'*3)

mes = int(input('Introduce el mes del año: '))
estacion = None

if mes==1 or mes==2 or mes==12:
    print(f'La estación del mes {mes} es invierno')
elif mes==3 or mes==4 or mes==5:
    print(f'La estación del mes {mes} es primavera')
elif mes==6 or mes==7 or mes==8:
    print(f'La estación del mes {mes} es verano')
elif mes==9 or mes==10 or mes==11:
    print(f'La estación del mes {mes} es otoño')
else:
    print(f'Mes inválido')