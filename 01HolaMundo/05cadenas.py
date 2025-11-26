# Caracteres especiales en Python

#Salto de línea
mensaje1 = "Hola\nmundo"
print(mensaje1)

#Tabulación
mensaje2 = "Nombre:\tJuan"
print(mensaje2)

# Comillas en cadena
mensaje3 = "Ella dijo: \"Hola a todos\""
print(mensaje3)

#Barra invertida
mensaje4 = "C:\\Usuarios\\Programas\\Documentos"
print(mensaje4)

#Cadena cruda
mensaje5 = r"C:\Usuarios\Programas\Documentos"
print(mensaje5)

#Concatenar String
nombre="Isaac"
saludo = "Hola " + nombre + ", Bienvenido"
print(saludo)

#Concatenar string + int
edad = 29
saludo = "Hola "+nombre+ " Tienes "+str(edad) +" años"
print(saludo)

print(f"Nombre: {nombre}, ¡Bienvenido!, tienes {edad} años")

#EJEMPLO CONCATENACIÓN DE CADENAS

#1. Con operador +
apellido = "Nabor"
nombre_completo=nombre+" "+apellido
print("Usuario + : "+nombre_completo)

#2. Usando print
print("Usando comas:", "Nombre:", nombre_completo,", Edad:", edad)

#3. Usando fstring
ciudad = "Querétaro"
pais = "México"
profesion="Ingeniero"
presentacion = f"Hola, soy {nombre_completo}, tengo {edad + 1} años y soy {profesion} en {ciudad}, {pais}"
print(presentacion)

#Longitud de cadenas
longitud = len(presentacion)
frase_longitud=f"La longitud de la frase es: {longitud} caracteres"
print(frase_longitud)

#Convertir a mayúsculas
mayus_frase = frase_longitud.upper() + " <- Esto es en mayúsculas"
print(mayus_frase)

#Convertir a minúsculas
minus_frase = frase_longitud.lower() + " <- Esto es en minúsculas"
print(minus_frase)

#Inmutabilidad de cadenas
usuario = "Isaac"
nuevo_usuario = usuario.upper()
print(usuario)
print(nuevo_usuario)

#Ejemplo de subcadenas (slicing), inicia el índice desde 0 y no incluye en final
nueva_cadena = "Hola mundo"
subcadena_1 = nueva_cadena[0:4] #Se especifica inicio y fin
subcadena_hola = nueva_cadena[:4] #no se especifica inicio, asume inicio en 0
subcadena_mundo = nueva_cadena[5:] #no se especifica fin, se asume es el final de la cadena
print("Cadena:", nueva_cadena)
print(f"Subcadena con indices especificados: {subcadena_1}")
print(f"Subcadena sin indice inicial: {subcadena_hola}")
print(f"Subcadena sin indice final: {subcadena_mundo}")

correo = "juan.perez@mail.com"
indice_arroba = correo.index("@")
print(f"Valor del índice del caracter arroba: {indice_arroba}")
usuario = correo[:indice_arroba]
print(f"Nombre de usuario: {usuario}")

#Metodo find para encontrar subcadena
frase = "Hola mundo"
posicion = frase.find("mundo")
print(f"Frase original: {frase}")
print(f"Indice subcadena mundo: {posicion}")

#Remplazar subcadena con remplace
nueva_frase = frase.replace("mundo", "Python")
print(f"Frase original: {frase}")
print(f"Frase modificada: {nueva_frase}")

#Multiplicar cadenas
caracter = "*"
repetir_veces = 10
nuevo_caracter = caracter * repetir_veces
print(f"Caracter multiplicado: {nuevo_caracter}")
print("+"*5)

#Encontrar índice de una cadena
texto = "Aprender Python es divertido"
print(f"Texto: {texto.find("Python")}")