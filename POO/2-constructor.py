#CONSTRUCTOR ES UNA FUNCION QUE SE EJECUTA AUTOMATICAMENTE CUANDO INSTANCIAMOS UNA CLASE


class Restaurante:

    def __init__(self,nombre, categoria): #constructor
        print('yo me ejecuto automaticamente cuando creas un objeto de la clase')
        self.nombre = nombre
        self.categoria = categoria
    def agregar_restaurante(self,nombre):
        self.nombre = nombre
        print(f"agregar restaurante...{self.nombre}")
        
    def mostrar_informacion(self):
        print(f"El nombre del restaurante es: {self.nombre} y es de la categoria: {self.categoria}")

#Instanciar la clase
restaurante = Restaurante("El pollo loco", "comida casual")
restaurante.mostrar_informacion()

restarurante2 = Restaurante("EL caballo cediento", "comida italiana")
restarurante2.mostrar_informacion()





#abstraccion de la clase
#son los datos necesarios de una clase ejemplo si elaboramos los platos de un restaurante son necesario los platos, descricion, precio