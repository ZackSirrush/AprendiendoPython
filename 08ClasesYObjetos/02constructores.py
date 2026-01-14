print('\n','*'*5, 'Clase de aritmética', '*'*5,'\n')

class Aritmetica:
    def __init__(self,operando1=None, operando2=None):
        self._operando1 = operando1
        self._operando2 = operando2

    def sumar(self):
        resultado = self._operando1 + self._operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self._operando1 - self._operando2
        print(f'Resultado resta: {resultado}')

    def multiplicar(self):
        resultado = self._operando1 * self._operando2
        print(f'Resultado multiplicación: {resultado}')

    def dividir(self):
        resultado = self._operando1 / self._operando2
        print(f'Resultado multiplicación: {resultado}')

    @property
    def operando1(self):
        return self._operando1
    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1

    @property
    def operando2(self):
        return self._operando2
    @operando2.setter
    def operando2(self, operando1):
        self._operando2 = operando1

if __name__ == '__main__':
    print('*** EJEMPLO CLASE ARITMÉTICA ***')
    print('Primer objeto')
    aritmetica1 = Aritmetica(5, 7)
    print(f'Valor operando 1: {aritmetica1.operando1}')
    print(f'Valor operando 2: {aritmetica1.operando2}')
    aritmetica1.sumar()
    aritmetica1.restar()
    print('\nSegundo objeto')
    aritmetica2 = Aritmetica(12, 16)
    print(f'Valor operando 1: {aritmetica2.operando1}')
    print(f'Valor operando 2: {aritmetica2.operando2}')
    aritmetica2.multiplicar()
    aritmetica2.dividir()
    print('\nTercer objeto')
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 9
    print(f'Valor operando 1: {aritmetica3.operando1}')
    print(f'Valor operando 2: {aritmetica3.operando2}')
    aritmetica3.sumar()
    print('\nCuarto objeto')
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 2
    aritmetica4.operando2 = 8
    print(f'Valor operando 1: {aritmetica4.operando1}')
    print(f'Valor operando 2: {aritmetica4.operando2}')
    aritmetica4.sumar()
    print('\nQuinto objeto')
    aritmetica5 = Aritmetica(operando1=3, operando2=4)
    print(f'Valor operando 1: {aritmetica5.operando1}')
    print(f'Valor operando 2: {aritmetica5.operando2}')
    aritmetica5.sumar()