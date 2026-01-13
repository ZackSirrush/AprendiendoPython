#*args - arguments - tupla
#**kwargs - keywords arguments (key, value) como un dict
print('\n','*'*5, 'Argumentos variables en forma de dict', '*'*5,'\n')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Más info: {kwargs}')

#Llamado a la función
superheroe_superpoderes('Spider-man', 'Sentido arácnido', edad=17, empresa='Marvel')
superheroe_superpoderes('Iron-Man','Armadura', 'Millonario', edad=45)

#Args variables son opcionales
superheroe_superpoderes('Mi Vecino', personalidad='Buen pedo!')