#import modulo_funcion_sumar
from modulo_funcion_sumar import sumar

print('\n','*'*5, 'Función sumar', '*'*5,'\n')

#Llamar función
if __name__ == '__main__':
    resultado_función = sumar(8, 5)
    print(f'Resultado de función sumar: {resultado_función}')
    #resultado_función = modulo_funcion_sumar.sumar(9, 15) con import sería así
    #print(f'Resultado defunción sumar: {resultado_función}')


