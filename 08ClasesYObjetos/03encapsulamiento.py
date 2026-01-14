print('\n','*'*5, 'Encapsulamiento', '*'*5,'\n')

#Clase
class Coche:
    def __init__(self, marca, modelo, color):
        # self.marca = marca #Público: Accede sin encapsular
        self._marca = marca
        self._modelo = modelo #Protegido: Accede pero no debes hacerlo
        # self.__color = color #Privado: Requiere encapsulamiento
        self._color = color

    def conducir(self):
        print(f'''\nConduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')


    @property #Define get con el estandar de python
    def marca(self):
        return self._marca
    # def get_marca(self):
    #     return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    # def set_marca(self, marca):
    #     self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color


#Programa principal
if __name__ == '__main__':
    #Crear primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()

    #No se debe acceder a atributos que no sean públicos
    coche1.marca = 'Toyota 2'
    coche1.modelo = 'Yaris 2'
    coche1.color = 'Negro'
    coche1.conducir()

    #Atributo de marca del coche 1
    coche1.marca = 'Toyota 3'
    coche1.modelo = 'Yaris 3'
    coche1.color = 'Negro'
    print(f'\nAtributo de marca: {coche1.marca}')
    print(f'Atributo de modelo: {coche1.modelo}')
    print(f'Atributo de color: {coche1.color}')

    #Intentar agregar un nuevo atributo
    setattr(coche1, 'nuevo_atributo', 'Valor nuevo atributo')
    coche1.nuevo_atributo2 = 'Valor nuevo atributo 2' #OTRA FORMA DE AGREGAR ATRIBUTOS A ESTE OBJETO
    coche1.conducir()
    print(f'Atributos de coche1: {coche1.__dict__}')
    #Segundo objeto
    coche2 = Coche('Chevrolet', 'Trax', 'Blanco')
    coche2.conducir()
    print(f'Atributos de coche2: {coche2.__dict__}')