#CREANDO CLASES Y OBJETOS

class Restaurante:
    def agregar_restaurante(self,nombre): #el self es lo que se requiere para guardar la informacion
        self.nombre = nombre #atributo de la clase aqui es donde se almacena los datos del restaurante
        print(f"agregar restaurante...{self.nombre}")
    def mostrar_informacion(self):
        print(f"El nombre del restaurante es: {self.nombre}")




class Carro:
    def agregar_carro(self,marca,modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        print(f"agregar carro...{self.marca,self.modelo, self.color}")
        
        
carro = Carro()        
carro.agregar_carro("fiat", "palio","azul")
print(f"La marca de mi carro es: {carro.marca}") #imprimir objetos 
carro2 = Carro()
carro2.agregar_carro("ford", "fortuna", "negro")
print(f'La marca de mi carro es: {carro.marca} el modelo: {carro2.modelo} el color: {carro2.color}')

       
#Instanciar la clase
restaurante = Restaurante()
restaurante.agregar_restaurante("El pollo loco")
restaurante.mostrar_informacion()


#PUEDO CREAR DIFERENTES OBJETOS USANDO UNA MISMA CLASE 

restaurante2 = Restaurante()
restaurante2.agregar_restaurante("El cochino andante")
restaurante2.mostrar_informacion()

#IMPRIMIR LOS OBJETOS
print(f"El nombre del restaurante es: {restaurante.nombre}")
print(f"El nombre del restaurante es: {restaurante2.nombre}")