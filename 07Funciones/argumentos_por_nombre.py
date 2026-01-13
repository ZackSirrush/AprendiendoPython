print('\n','*'*5, 'Función con argumentos por nombre', '*'*5,'\n')

def imprimir_persona(nombre,apellido='',edad=0): #Tienen valores por default menos nombre
    print(f'Persona: Nombre = {nombre}, Apellido = {apellido}, Edad = {edad}')

#Llamar función pasando argumentos
imprimir_persona('Ricardo','Quintana',30)

#Llamar función usando argumentos por nombre
imprimir_persona(nombre='Carlos',apellido='Rojas',edad=28)

#Llamar función intercambiando el órden
imprimir_persona(edad=25, apellido='González', nombre='Manuel')

#Argumentos con valores por default
imprimir_persona(nombre='Jose')
imprimir_persona(nombre='Jose', apellido='López')