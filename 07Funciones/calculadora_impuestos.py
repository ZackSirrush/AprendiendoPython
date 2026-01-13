print('\n','*'*5, 'Calculadora de impuestos', '*'*5,'\n')

def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

pago_sin_impuesto = float(input('Ingrese el valor de pago sin IVA: '))
impuesto = float(input('Ingrese el valor del IVA: '))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'El pago con impuesto es: {pago_con_impuesto}')