
#EJERCICIO  #2
pregunta =  input('agrega un número y te dire si es impar\r\n')
pregunta += '\r\n escribe "cerrar" para salir de la app\r\n'
preguntar = True



while True:
    numero = input("Ingresa un número (o escribe 'cerrar' para salir): ")
    if numero.lower() == "cerrar":
        break
    try:
        numero = int(numero)
        if numero % 2 == 0:
            print(f"{numero} es par.")
        else:
            print(f"{numero} es impar.")
    except ValueError:
          print("Por favor, ingresa un número válido.")