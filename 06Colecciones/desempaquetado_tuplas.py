print('\n','*'*5, 'Desempaquetado de Tuplas (Unpacking)', '*'*5,'\n')

producto = ('P001', 'Camisa', 20.00)

#Aplicar desempaquetado
id, descripcion, precio = producto

print(f'Tupla completa: {producto}')
print(f'Producto: ID = {id}, descripcion: {descripcion}, precio: {precio:.2f}')