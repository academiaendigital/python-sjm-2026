#FUNCIONES QUE RETONAR VALORES
# son funciones para devolver el valor almacenado en una variable pasada como un argumento
def info(nombre):
    return nombre
empleado =info('jenny')
print(empleado)

empleado2 =info('jennysss')

print(empleado2)

def sumar(a, b):
   return a + b
resultado = sumar(15, 13)
print(resultado)  

def pizza(a,b,c):
    return a,b,c
pizzaCocinada = pizza('salsa','maiz','tocineta')
print (pizzaCocinada)
print(f'Los ingredientes de la pizza son {pizzaCocinada} ')