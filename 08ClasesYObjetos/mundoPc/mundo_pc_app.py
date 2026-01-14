from mundoPc.computadora import Computadora
from mundoPc.monitor import Monitor
from mundoPc.orden import Orden
from mundoPc.raton import Raton
from mundoPc.teclado import Teclado

print('\n','*'*5, 'Mundo PC', '*'*5,'\n')

teclado1 = Teclado('Logitech','USB')
raton1 = Raton('HP','USB')
monitor1 = Monitor('HP',27)
computadora1 = Computadora('HP',monitor1,teclado1,raton1)

teclado2 = Teclado('GAMER','Bluethooth')
raton2 = Raton('GAMER','Bluethooth')
monitor2 = Monitor('GAMER',34)
computadora2 = Computadora('GAMER',monitor2,teclado2,raton2)


computadoras1 = [computadora1,computadora2]
orden1 = Orden(computadoras1)
print(orden1)

teclado3 = Teclado('DELL','Bluethooth')
raton3 = Raton('DELL','Bluethooth')
monitor3 = Monitor('DELL',27)
computadora3 = Computadora('DELL',monitor3,teclado3,raton3)

#agrega otra computadora
orden1.agregar_computadora(computadora3)
print(orden1)