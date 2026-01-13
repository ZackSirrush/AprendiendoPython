print('\n','*'*5, 'Maquina de snacks', '*'*5,'\n')

#Lista de snaks inicial
inventario = [
    {'id':1,'nombre':'Papas','precio':30},
    {'id':2,'nombre':'Refresco','precio':50},
    {'id':3,'nombre':'Sandwich','precio':120}
]

ticket_compra = [

]

def mostrar_snacks():
    print('--- Snacks disponibles ---')
    for snack in inventario:
        print(f'ID: {snack.get('id')} -> {snack.get('nombre')} - ${snack.get('precio')}')

def buscar_snacks(id_buscar):
    for snack in inventario:
        if snack.get('id') == id_buscar:
            return snack
    return None

def comprar_snaks():
    id_snack = int(input('Indica el ID del snack que deseas comprar: '))
    snack_encontrado = buscar_snacks(id_snack)
    if snack_encontrado is not None:
        ticket_compra.append(snack_encontrado)
        print('¡Snack agregado a ticket!')
    else:
        print(f'Snack NO encontrado con ID: {id_snack}')

def mostrar_ticket():
    ticket = f'\t--- Ticket de venta ---'
    total = 0
    for productos in ticket_compra:
        ticket += f'\n\t- {productos.get('nombre')} - ${productos.get('precio')}'
        total += productos.get('precio')
    ticket += f'\n\tTOTAL -> ${total}'
    print(ticket)

#Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n --- Menú ---
        1. Mostrar Snacks
        2. Comprar Snack
        3. Mostrar Ticket
        4. Salir''')
        opcion = int(input('\nSelecciona una opción: '))
        if opcion == 1: #Muestra inventario
            mostrar_snacks()
        elif opcion == 2: #Agregar nuevo producto
            comprar_snaks()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('¡Vuelva pronto!')
            break
        else:
            print('Proporciona una opción del menú.')