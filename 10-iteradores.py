# ITERADORES CORREN UN DETERMINADO NUMERO DE VECES 
# UN PIEZA DE CODIGO

meses= ['octubre','febrero', 'marzo']

#CICLO FOR
for mes in meses:
    print(mes)

print(f'Estoy viajando por el mundo en el mes de {mes}')

#imprimir numeros
#generar secuencias de números enteros. 
# Imagina que quieres crear una lista de números del 0 al 9.
# En lugar de escribir cada número manualmente, 
# puedes usar range() para generar esta secuencia
#  de manera automática.
#range() también acepta dos o tres argumentos:
# range(start, stop, step)
#start: El número inicial de la secuencia (incluido).
#stop: El número final de la secuencia (no incluido).
# step: El incremento entre cada número. 
# Si se omite, el valor por defecto es 1.


for numero in range(5,104,2):
    print(numero)
