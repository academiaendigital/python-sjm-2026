#COMO SABER SI UN NUMERO ES PAR
numero = input('agrega un número y te dire si es impar\r\n')
numero = int(numero)

if numero %2 == 0: #modulo divide para ver si es un entero y genera un residuo
    print(f'tu numero {numero} es par')
else:
    print(f'tu numero {numero} es impar')


