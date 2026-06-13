#OPERACIONES BASICAS EN PYTHON

a = 15
b = 40
print('La suma de a+b es igual a ' + str(a) + ' + ' + str(b) + ' = ' + str(a+b))

#para concatener variables numericas es necesario usar la palabra str para
#convertir el valor en una cadena de texto  o puedes usar la siguiente alternativa

print(f'La suma de a+b es igual a {a} + {b} = {a+b}')

#Python 3.6, se introdujeron las f-strings,

print(f'La multiplicación de a por b es igual a {a} + {b} = {a*b}')
print(f'La division de a entre b es igual a {a} + {b} = {a/b}')
