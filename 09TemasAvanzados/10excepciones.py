print('\n','*'*5, 'Manejo de excepciones en Python', '*'*5,'\n')

def dividir(numerador, denominador):
    try:
        #Revisa si el denominado es = 0
        if denominador == 0:
            raise Exception('El denominador es igual 0') #Genera excepciones personalizadas
        resultado = numerador / denominador
        print(f'Resultado de la división {resultado}')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
    else:
        print(f'No ocurrió ningún error.')
    finally: #siempre se ejecuta este bloque al final
        print('Resultado procesado\n')
    # except ZeroDivisionError:
    #     print('Error: No se puede dividir entre 0')
    # except TypeError:
    #     print('Error: Los operandos deben ser numéricos')

#Ejemplo de uso
dividir(10,2)
dividir(10,0)
dividir(10,'0')