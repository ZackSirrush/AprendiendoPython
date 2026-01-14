class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #Sobreescribir metodo __str__; sí no se sobreescribe
    # imprime __main__.Person object at [direeción de memoria donde se almacena]
    def __str__(self):
        return f'''Persona:
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. mem. {super.__str__(self)}''' #ESTO SERÍA LA RESPUESTA POR DEFAULT

#Programa principal
print('\n','*'*5, 'Ejemplo de polimorfismo en clases object', '*'*5,'\n')

persona1 = Persona('Ana', 'Martínez')
print(persona1) #llama metodo STR sobreescrito que sirve para imprimir resultados