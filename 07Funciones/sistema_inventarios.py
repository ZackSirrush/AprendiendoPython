print('\n','*'*5, 'Sistema de inventarios con recursividad', '*'*5,'\n')

#Inventario del almacen
inventario = [
    {'id':1,'nombre':'Camisa','precio':25.99, 'cantidad': 50},
    {'id':2,'nombre':'Pantalones','precio':39.99, 'cantidad': 30},
    {'id':3,'nombre':'Camisa','precio':49.99, 'cantidad': 20}
]

#Función para mostrar inventario
def mostrar_inventario():
    print('--- Inventario en Almacén ---')
    for producto in inventario:
        print(f'ID: {producto.get('id')}, Nombre: {producto.get('nombre')},'
              f' Precio: {producto.get('precio')}, Cantidad: {producto.get('cantidad')}')

#Función para agregar producto
def agregar_producto():
    print('--- Agregar nuevo producto ---')
    id_producto = int(input('ID: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {
        'id': id_producto,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    inventario.append(nuevo_producto)
    print('Producto agregado con éxito.')

#Función para buscar producto
def buscar_producto():
    #pass palabra reservada para agregar funciones sin implementarse
    print('--- Buscar producto por ID ---')
    id_buscado = int(input('Ingresa un ID para buscar: '))
    for producto in inventario:
        if producto.get('id') == id_buscado:
            print('\nInformación del producto encontrado: ')
            print(f'ID: {producto.get("id")}, Nombre: {producto.get("nombre")}, '
                  f'Precio: ${producto.get("precio")}, Cantidad: {producto.get("cantidad")}')
            return
    print('Producto no encontrado')

#Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n --- Menú ---
        1. Mostrar inventario
        2. Agregar nuevo producto
        3. Buscar producto por ID
        4. Salir''')
        opcion = int(input('\nSeleccione una opción (1-4): '))
        if opcion == 1: #Muestra inventario
            mostrar_inventario()
        elif opcion == 2: #Agregar nuevo producto
            agregar_producto()
        elif opcion == 3:
            buscar_producto()
        elif opcion == 4:
            print('Cerrando sistema; hasta pronto.')
            break
        else:
            print('Proporciona una opción del menú.')