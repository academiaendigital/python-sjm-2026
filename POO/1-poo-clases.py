class Carro:
    def __init__(self, marca, modelo, color): #Este es el constructor de la clase.
        #Es un método especial que se ejecuta automáticamente cuando se crea un nuevo objeto (instancia) de la clase 
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
        
 #Es una convención en Python. self representa la instancia del objeto que se está creando. Se utiliza para acceder a los atributos y métodos del objeto dentro de la clase.
    def encender(self):
        self.encendido = True
        print("El carro ha encendido.")

    def apagar(self):
     
        self.encendido = False
        print("El carro ha apagado.")


    def acelerar(self):
        if self.encendido:
            print("El carro está acelerando.")
        else:
            print("El carro debe estar encendido para acelerar.")

# Creamos un objeto (instancia) de la clase Carro
mi_carro = Carro("Toyota", "Corolla", "Blanco")

mi_carro2 = Carro("Chevrolet", "Optra", "Negro")
# Acceder a los atributos del objeto
print(mi_carro2.marca)  # Imprime: Toyota
print(mi_carro2)
print(mi_carro2.marca)
# Llamar a un método del objeto
mi_carro.encender()
mi_carro.acelerar()
mi_carro.apagar()




class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños, ahora tienes {self.edad} años.")
mi_persona= Persona("Jenny", 42)
mi_persona.saludar()

mi_persona.cumplir_anios()