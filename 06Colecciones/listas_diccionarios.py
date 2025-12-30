print('\n','*'*5, 'Listas y diccionarios', '*'*5,'\n')

personas= [
    {
        'nombre':'Regina',
        'apellido':'Flores',
        'edad':21,
    },
    {
        'nombre':'Alejandro',
        'apellido':'Reyes',
        'edad':32,
    },
]

print(personas)

#Acceder a un diccionario desde lista
print(f'''Detalle del primer elemento de la lista
    Nombre: {personas[0].get('nombre')}
    Apellido: {personas[0].get('apellido')}
    Edad: {personas[0].get('edad')}
''')

#Recorrer elementos de la lista
for contador, persona in enumerate(personas):
    print(f'{contador+1} - Persona: {persona.get('nombre')}')
    print(f'Detalle:\n   Nombre: {persona.get("nombre")}\n   Apellido: {persona.get("apellido")}\n   Edad: {persona.get("edad")}')