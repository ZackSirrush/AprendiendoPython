print('\n','*'*5, 'Combinación de listas y tuplas', '*'*5,'\n')

#Lista con tuplas de productos
productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Sudadera', 40.00)
]

#Imprimir info de cada producto y precio total
precio_total = 0

print('Información de los productos: ')
for producto in productos:
    id, descripcion, precio = producto
    print(f'\tProducto: ID = {id}, Descripción = {descripcion}, Precio = ${precio:.2f}')
    precio_total += precio

print(f'\nPrecio total de los productos: ${precio_total:.2f}')