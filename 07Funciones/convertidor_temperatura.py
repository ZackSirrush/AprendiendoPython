print('\n','*'*5, 'Convertidor de temperatura', '*'*5,'\n')

def celsius_fahrenheit(celcius):
    return celcius * 9 / 5 + 32

def fahrenheit_celsius(farenheit):
    return (farenheit - 32) * 5 / 9

celsius = float(input('Proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius}°C a °F: {resultado:.2f}°F')

fahrenheit = float(input('Proporcione su valor en farenheit: '))
resultado2 = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit}°F a °C: {resultado2:.2f}°C')