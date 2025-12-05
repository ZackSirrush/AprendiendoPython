from random import randint

print('*'*10,'JUEGO DE ADIVINANZAS','*'*10,'\n')

numero_secreto = randint(1,50)
intento = 0
adivinanza = None
INTENTOS_MAXIMOS = 5

while adivinanza != numero_secreto and intento < INTENTOS_MAXIMOS:
    adivinanza = int(input('Adivina el número secreto (1 - 50): '))
    if adivinanza < numero_secreto:
        print('El número secreto es mayor\n')
    elif adivinanza > numero_secreto:
        print('El número secreto es menor\n')
    intento += 1

if adivinanza == numero_secreto:
    print(f'¡Felicidades!, adivinaste el número secreto en {intento} intentos')
else:
    print(f'Lo siento, se agotaron tus {INTENTOS_MAXIMOS} intentos.')
    print(f'El número secreto era: {numero_secreto}.')