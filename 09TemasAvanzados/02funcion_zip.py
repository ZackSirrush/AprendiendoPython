nombres = ['Juan', 'Maria', 'Pedro', 'Ana'] #Tomará el valor de la lista más pequeña e ignora los demás
edades = [30, 25, 35]
ciudades = ['Madrid', 'Barcelona', 'Sevilla']

#combinar elementos con función zip
personas = zip(nombres, edades, ciudades)

#Iterar sobre el resultado de función zip
for persona in personas:
    print(persona)