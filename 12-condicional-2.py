#CONDICIONAL EL IF elif else 
tipo = 'estudiante'
if tipo=='estudiante':
    print('Tienes un descuento del 50%')
elif tipo=='profesor':
    print('Tienes un descuento del 80%')
elif tipo=='invitado':
    print('Tienes un descuento del 10%')
else:
    print('NO HAY DESCUENTO')


usuario = 'romanlg' 
tipoUsuario = 'admin'
tiposUsuarios = ['admin','superadmin','invitado']

if tipoUsuario in tiposUsuarios and usuario == 'romanlg':
    if tipoUsuario=='superadmin':
        print('ACCESO TOTAL')
    elif tipoUsuario=='admin':
        print('El usuaro es admin')
    else:
        print('el usuario es invitado')    
else:
    print('el usuario no puede entrar al sistema')
    

