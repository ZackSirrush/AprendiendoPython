print('\n','*'*5, 'Regresar una tupla de valores desde una función', '*'*5,'\n')

def persona_mayusculas(nombre,apellido,edad):
    print(f'Esta función regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad

#Programa principal
nombre, apellido, edad = persona_mayusculas('Elizabeth','Salazar',42)
print(f'Resultado Persona: Nombre = {nombre}, Apellido = {apellido}, Edad = {edad}')