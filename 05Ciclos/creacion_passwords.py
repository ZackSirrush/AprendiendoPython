print('*'*10,'SISTEMA PARA VALIDAR CONTRASEÑAS','*'*10,'\n')

password = input('Ingresa una contraseña (debe tener más de 6 caracteres): ')

while len(password) < 6:
    print('La contraseña debe tener al menos 6 caracteres')
    password = input('Ingrese nuevamente su contraseña: \n')
else:
    print(f'Contraseña correcta: {password}')