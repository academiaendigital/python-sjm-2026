import random

def juego_adivinar_numero():
 
    # 1. Generar un número aleatorio entre 1 y 100 #funcion principal
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("\n--- ¡Bienvenido al Juego de Adivinar el Número! 🎯 ---")
    print("Estoy pensando en un número entre 1 y 100.")
    print("¡Tienes que adivinarlo!")

    # LO QUE HACE QUE EL JUEGO FUNCIONE
    while not adivinado:
        try:
            # SOLICITAR AL USUARIO EL INGRESO 
            intento_usuario = int(input("Ingresa tu intento: "))
            intentos += 1

            # 3. Comprobar si el intento es correcto y dar retroalimentación
            if intento_usuario < 1 or intento_usuario > 100:
                print("⚠️ Recuerda, el número debe estar entre 1 y 100.")
            elif intento_usuario < numero_secreto:
                print("⬇️ ¡Demasiado bajo! Intenta con un número mayor.")
            elif intento_usuario > numero_secreto:
                print("⬆️ ¡Demasiado alto! Intenta con un número menor.")
            else:
                # El número es correcto
                adivinado = True
                print(f"\n🎉 ¡Felicidades! ¡Adivinaste el número secreto ({numero_secreto})!")
                print(f"Lo lograste en {intentos} intento(s). ¡Eres un crack! 💪")

        # Manejo de errores para entradas no numéricas
        except ValueError:
            print("❌ Entrada no válida. Por favor, ingresa un número entero.")

# Ejecutar el juego
juego_adivinar_numero()