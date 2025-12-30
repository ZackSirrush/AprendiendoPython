print('\n','*'*5, 'Agenda de contactos', '*'*5,'\n')
agenda={
    'Carlos':{
        'telefono': '0123456789',
        'email': 'carlos@mail.com',
        'direccion':'Calle x 123'
    },
    'María':{
        'telefono': '1234567890',
        'email': 'maria@mail.com',
        'direccion':'Calle x 456'
    },
    'Pedro':{
        'telefono': '9876543210',
        'email': 'pedro@mail.com',
        'direccion':'Calle x 789'
    }
}

print(f'{agenda}')

#Acceder a la información de un contacto específico
print (f'''\nInformación del contacto de María: 
    Teléfono: {agenda['María']['telefono']} 
    Correo: {agenda.get('María').get('email')}
    Dirección: {agenda['María']['direccion']}  
''')

#Agregar nuevo contacto
agenda['Ana'] ={
    'telefono': '8532469712',
    'email': 'ana@mail.com',
    'direccion': 'Calle x 951'
}

print(f'{agenda}')

#Eliminar contacto existente
agenda.pop('Pedro')
#del agenda['Pedro']

print(f'{agenda}')

#Mostrar contactos de agenda
print(f'\nContactos en la agenda')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Teléfono: {detalles.get('telefono')}
    Correo: {detalles.get('email')}
    Dirección: {detalles.get('direccion')} 
''')