from mundoPc.monitor import Monitor
from mundoPc.raton import Raton
from mundoPc.teclado import Teclado


class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''\t{self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}"
        Teclado: {self.teclado}
        Ratón: {self.raton}'''

if __name__ == '__main__':
    teclado1 = Teclado('Logitech','USB')
    raton1 = Raton('HP','USB')
    monitor1 = Monitor('HP',27)
    computadora1 = Computadora('HP',monitor1,teclado1,raton1)
    print(computadora1)
    teclado2 = Teclado('GAMER','Bluethooth')
    raton2 = Raton('GAMER','Bluethooth')
    monitor2 = Monitor('GAMER',34)
    computadora2 = Computadora('Gamer',monitor2,teclado2,raton2)
    print(computadora2)
