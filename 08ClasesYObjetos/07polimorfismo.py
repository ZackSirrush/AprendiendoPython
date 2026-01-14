class Animal:
    def hacer_sonido(self):
        print('Hago un sonido')

class Perro(Animal):
    #Sobreescritura de metodos
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    #Sobreescritura de metodos
    def hacer_sonido(self):
        print('Puedo maullar')

#Función polimorfica
def hacer_sonido_animal1(animal): #duck typing
    animal.hacer_sonido()

#Programa principal
print('\n','*'*5, 'Ejemplo de polimorfismo', '*'*5,'\n')

print('Clase Padre - Animal: ')
animal1 = Animal()
hacer_sonido_animal1(animal1)
animal1.hacer_sonido()
print(f'\nClase Hija - Perro')
perro1 = Perro()
hacer_sonido_animal1(perro1) #Polimorfismo duck_typing
print(f'\nClase Hija - Gato')
gato1 = Gato()
hacer_sonido_animal1(gato1)
gato1.hacer_sonido() #Polimorfismo