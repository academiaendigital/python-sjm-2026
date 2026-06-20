nombre = input('Cuál es tu nombre?\r\n') #retorno del carrete \n salto de linea
print(f'tu nombre es {nombre}')



edad = input('Cual es tu edad?\r\n')
#convertir edad en un entero
edad = int(edad)   #float #str

if edad >=18:
    print(f'eres mayor de edad y puedes votar')
else:
    print(f'lo sentimos aun eres un bebe')
   
#caso que un usuario ingrese otro valor que no sea numero
edad = input('¿Cuál es tu edad?\r\n')
try:
    edad = int(edad)
    if edad >= 18:
        print(f'Eres mayor de edad y puedes votar.')
    else:
        print(f'Aún no tienes la edad para votar.')
except ValueError:
    print("Por favor, ingresa un número válido para la edad.")    