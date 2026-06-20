# OPERADORES DE COMPARACION 
# == Igual a
# != Diferente de
# <  Menor que
# >  Mayor que
# <= Menor o igual que
# >= Mayor o igual que
a = 5
b = 3
igual = a == b  # igual es False
diferente = a !=  b  # diferente es True
mayor = a >= b  # mayor es True

#CONDICIONAL 
ahorro = 60
if ahorro >=50:
    print("Nos vamos de viaje")
else:
    print("no tenemos ahorros")


#REVISAMOS SI UN VALOR ES DIFERENTE EN PYTHON STRING
lenguaje = 'javascript'
if not lenguaje == 'python':
    print(f'super eres un crack de {lenguaje}')
else:
    print(f"no eres un crack de {lenguaje}")


#EVALUACION BOOLEAN
usuario_autenticado = True
if usuario_autenticado:
    print('el usuario se autentico con exito')
else:
    print('el usuario no se autentico vuelva a intentarlo')
    
    
  
    
    
    


#CONDICONALES CON LIST 
superheroes = ['superman','spiderman','mujer maravilla','hercules']
if  'superman' in superheroes:
    print('amas a superman')
else:
    print('tu superheroe no es batman')


tiposUsuarios= ['admin','superadmin','invitado']
if 'admin' in tiposUsuarios:
    print('tienes acceso a todo menos a borrar la bitacora')
else:
    print('no eres admin')








#condicionales anidados
acceso_usuario = True
acceso_admin = True

if acceso_usuario:
    if acceso_admin:
        print('ACCESO TOTAL')
    else:
        print('El usuaro no es admin')
else:
    print('El usuario no esta autenticado')


