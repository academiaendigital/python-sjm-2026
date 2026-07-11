# Sistema de Gestión de Biblioteca 📚
# Objetivo: Crear un sistema para rastrear libros en una biblioteca.
# Conceptos: Usar un diccionario donde la clave sea el ID (ISBN) del libro 
# y el valor sea otro diccionario con detalles como {'titulo': '...', 'autor': '...', 'prestado': False}.
# Funciones a Implementar:
# agregar_libro(isbn, titulo, autor): Añade un nuevo libro.
# prestar_libro(isbn): Cambia el estado prestado a True.
# devolver_libro(isbn): Cambia el estado prestado a False.
# buscar_libro_por_titulo(titulo): Busca e imprime los detalles del libro.
































# Rastreador de Inventario Simple 📦
# Objetivo: Administrar los niveles de stock de diferentes productos en una tienda.
# Conceptos: Usar un diccionario donde la clave sea el nombre del producto (cadena) y el valor sea un número entero que representa la cantidad en stock.
# Funciones a Implementar:
# agregar_producto(nombre, cantidad): Agrega stock a un producto existente o crea uno nuevo.
# vender_producto(nombre, cantidad_vendida): Disminuye el stock, asegurándose de que no sea negativo (manejo de errores).
# mostrar_inventario(): Imprime todos los productos y su stock actual. 