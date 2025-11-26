#Programa: generador de correos
print("*"*10+"\tGenerador de correos\t"+"*"*10+"\n")

nombre = " Juan Manuel Perez Martinez "
empresa = " Lagion Mexico"
dominio = ".com.mx"

usr_normalizado = nombre.strip() #Quita espacios al inicio y final de cadena
usr_normalizado = usr_normalizado.replace(" ",".")
usr_normalizado = usr_normalizado.lower()
empresa_normalizado = empresa.strip()
empresa_normalizado = empresa_normalizado.replace(" ","")
empresa_normalizado = empresa_normalizado.lower()


dominio_correo= f"@{empresa_normalizado}{dominio}"
correo_generado = f"{usr_normalizado}{dominio_correo}"

print(f"Nombre usuario: {nombre}")
print(f"Nombre normalizado: {usr_normalizado}\n")

print(f"Nombre de empresa: {empresa}")
print(f"Extensión del dominio: {dominio}")
print(f"Dominio del correo normalizado: {dominio_correo}\n")
print(f"Correo generado: {correo_generado}")