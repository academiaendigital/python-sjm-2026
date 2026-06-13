
class Restaurant(self,nombre):
    def agregar_resturante(self):
        self.nombre = nombre
        print ("Agregando..") 
    def eliminar_restaurante(self):
        print ("Eliminando..")


#instanciar la clase, el nombre de la variable tu lo elijes
restaurnt = Restaurant() #aqui ya estamos creando un objeto  y cremos la instancia
print(restaurnt)

#para ejecutar el metodo
restaurnt.agregar_resturante('el caballo sediento') 
restaurnt.eliminar_restaurante('el caballo sediento') 



