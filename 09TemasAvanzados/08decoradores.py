print('\n','*'*5, 'Decoradores en Python', '*'*5,'\n')

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print('Antes de llamar la función saludar')
        resultado = funcion(*args, **kwargs) #Se llama a la funcipn
        print('Después de llamar función saludar')
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Carlos')