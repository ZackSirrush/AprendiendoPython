print('\n','*'*5, 'Función par', '*'*5,'\n')

#Saber sí el número es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

#Llamado a la función

if __name__ == '__main__':
   numero = int(input('Ingrese un numero: '))
   print(f'¿El numero {numero} es par?: {es_par(numero)}')