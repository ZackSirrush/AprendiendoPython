print('*'*3, 'SENTENCIA IF', '*'*3)

edad = 7

if edad >= 18:
    print(f'Eres adulto. Tienes {edad} años')
elif 13 <= edad < 18:
    print(f'Eres adolescente. Tienes {edad} años')
else:
    print(f'Eres Infante. Tienes {edad}')