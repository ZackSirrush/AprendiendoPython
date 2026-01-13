print('\n','*'*5, 'Argumentos variables', '*'*5,'\n')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'\nSuperhéroe: {superheroe} - {nombre}')
    #Iterar superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

#Llamar función
superheroe_superpoderes('Spider-man', 'Peter Parker', 'Instinto arácnido', 'Telaraña', 'Super-fuerza')
superheroe_superpoderes('Iron-man', 'Tony Stark', 'Armadura', 'Millonario')
superheroe_superpoderes('Mi-Vecino', 'Juan Pérez') #Es opcional agregar args
