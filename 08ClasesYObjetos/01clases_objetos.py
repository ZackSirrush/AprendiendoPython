print('\n','*'*5, 'Clases y objetos', '*'*5,'\n')
#Esto es una clase
class Persona:

    #Esto es un constructor. ventaja: se llaman de manera automática
    def __init__(self, nombre, apellido):
        #atributos
        self.nombre = nombre
        self.apellido = apellido

    #Esto es un metodo
    def mostrar_persona(self):
        print(f'''Persona
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f'Dirección de memoria self: {id(self)}')
        print(f'Dirección de memoria hex self: {hex(id(self))}')


#Crear objetos
if __name__ == '__main__':
    #Esto es un objeto
    persona1 = Persona('Layla','Acosta') #Crea un objeto vacío en memoria
    persona1.mostrar_persona()
    print(f'Dirección de memoria Persona 1: {id(persona1)}')
    print(f'Dirección de memoria hex Persona 1: {hex(id(persona1))}\n')

    #Segundo objeto
    persona2 = Persona('Ian', 'Sánchez')
    persona2.mostrar_persona()
    print(f'Dirección de memoria Persona 2: {id(persona2)}')
    print(f'Dirección de memoria hex Persona 2: {hex(id(persona2))}\n')