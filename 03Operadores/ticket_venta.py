print('*'*3, 'SISTEMA GENERACION TICKET DE VENTA', '*'*3)

precio_leche = float(input('Precio leche: $'))
precio_pan = float(input('Precio pan: $'))
precio_lechuga = float(input('Precio lechuga: $'))
precio_platanos = float(input('Precio platanos: $'))
descuento_porcentaje = int(input('¿Aplicar descuento (%)?: '))

#Cálculo de subtotal sin impuestos
subtotal = precio_platanos + precio_lechuga + precio_pan + precio_leche
descuento = subtotal * (descuento_porcentaje/100)
subtotal_con_descuento = subtotal - descuento
iva = subtotal_con_descuento * 0.16
total = subtotal_con_descuento + iva #TOTAL DE COMPRA

print(f'''
Subtotal: ${subtotal:.2f}
Descuento: ${descuento:.2f} (-{descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento:.2f}
IVA (16%): ${iva:.2f}
Total: ${total:.2f}
''')