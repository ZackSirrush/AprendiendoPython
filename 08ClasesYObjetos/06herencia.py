class Animal:
    def comer(self):
        print('Como muchas veces al día')
    def dormir(self):
        print('Duermo muchas horas')
    def hacer_sonido(self):
        print('Puedo hacer un sonido')

class Perro(Animal):
    #Sobreescritura de metodos
    def comer(self):
        print('Como 3 veces al día')
    def dormir(self):
        print('Duermo 15 horas al día')
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    #Sobreescritura de metodos
    def comer(self):
        print('Como 3 veces al día')
    def dormir(self):
        print('Duermo 18 horas al día')
    def hacer_sonido(self):
        print('Puedo maullar')

#Programa principal
print('\n','*'*5, 'Ejemplo de herencia y sobreescritura en Python', '*'*5,'\n')
print('Clase Padre - soy un animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()
print(f'\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()
print(f'\nClase Hija, soy un Gato')
gato1 = Gato()
gato1.comer()
gato1.dormir()
gato1.hacer_sonido()