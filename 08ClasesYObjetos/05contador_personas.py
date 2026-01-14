class Persona:
    # Atributo clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # Incremento el valor atributo de clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

    @staticmethod #Este metodo no recibe parámetro
    def get_contador_personas_estatico():
        print(f'Método estático')
        return Persona.contador_personas

    @classmethod #No requiere usar nombre de clase, solo "cls"; esta práctica es más recomendada
    def get_contador_personas_clase(cls):
        print('Método de clase')
        return cls.contador_personas

if __name__ == '__main__':
    print('\n', '*' * 5, 'Ejemplo contador de objetos de tipo persona', '*' * 5, '\n')
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostrar_persona()
    persona2 = Persona('Juan', 'Gonzalez')
    persona2.mostrar_persona()

    print(f'\nContador objetos Persona: {Persona.contador_personas}')
    print(f'Contador objetos Persona (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador objetos Persona (clase): {Persona.get_contador_personas_clase()}')