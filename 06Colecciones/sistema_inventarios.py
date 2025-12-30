print('\n','*'*5, 'Sistema de inventarios', '*'*5,'\n')

inventario = []

numero_productos = int(input('¿Cuántos productos deseas agregar al diccionario?'))

for indice in range(numero_productos):
    print(f'Proporciona los valores del producto: {indice+1}')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    #Crear diccionario con detalles
    producto = {'id':indice+1, 'nombre':nombre, 'precio':precio, 'cantidad':cantidad}
    #Agrega el nuevo producto al inventario
    inventario.append(producto)

#Mostrar inventario inicial
print(f'\nInventario inicial: {inventario}')

#Buscar por ID
id_buscar = int(input('\nIngresa el ID del producto a buscar: '))

producto_encontadro=None
for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontadro = producto
        break

if producto_encontadro is not None:
    print('Información del producto: ')
    print(f'''ID: {producto_encontadro.get('id')}
    Nombre: {producto_encontadro.get('nombre')}
    Precio: {producto_encontadro.get('precio')}
    Cantidad: {producto_encontadro.get('cantidad')}
    ''')
else:
    print(f'Producto con ID {id_buscar} no encontrado')

#Mostrar inventario detallado
print(f'\n----- Inventario Detallado -----')
for producto in inventario:
    print(f'''ID: {producto.get('id')}
        Nombre: {producto.get('nombre')}
        Precio: {producto.get('precio')}
        Cantidad: {producto.get('cantidad')}
        ''')