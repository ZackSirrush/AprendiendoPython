class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.id_monitor = Monitor.contador_monitores
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return (f'ID: {self.id_monitor}, Marca: {self.marca}, '
                f'Tamaño: {self.tamanio}')

#CODIGO PRINCIPAL
if __name__ == '__main__':
    monitor1 = Monitor('HP', 15)
    monitor2 = Monitor('ACER', 20)
    print(monitor1)
    print(monitor2)