print('*'*3, 'SISTEMA PARA CÁLCULO DE ÁREA Y PERÍMETRO DE RECTÁNGULO', '*'*3)

base = float(input('Proporciona la base del rectángulo: '))
altura = float(input('Proporciona la altura del rectángulo: '))

area = base * altura
perimetro = 2*(base + altura)

print(f'El área del rectángulo con B = {base} y A = {altura} es: {area}')
print(f'El perímetro del rectángulo es: {perimetro}')