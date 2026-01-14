class Persona:
    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia


#Programa principal
if __name__ == '__main__':
    print('\n','*'*5, 'Atributos de clase', '*'*5,'\n')
    print(f'Atributo de clase: {Persona.atributo_clase}')

    #mod atributo clase
    Persona.atributo_clase = 10
    print(f'Atributo de clase modificado: {Persona.atributo_clase}')

    #CREAR OBJ PERSONA
    persona1 = Persona(15)
    print(f'\nAtributo de clase: {persona1.atributo_clase}')
    print(f'Atributo de instancia: {persona1.atributo_instancia}')

    #CREAR 2 OBJETO
    persona2 = Persona(30)
    print(f'\nAtributo de clase: {persona2.atributo_clase}')
    print(f'Atributo de instancia: {persona2.atributo_instancia}')