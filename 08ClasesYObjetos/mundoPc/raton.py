from mundoPc.dispositivo_entrada import DispositivoEntrada

class Raton (DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        # self.marca = marca
        # self.tipo_entrada = tipo_entrada
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'ID: {self.id_raton}, Marca: {self.marca}, '
                f'Tipo de entrada: {self.tipo_entrada}')

#CODIGO PRINCIPAL
if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    raton2 = Raton('ACER', 'BLUETHOOTH')
    print(raton1)
    print(raton2)