# Diccionario global para almacenar los libros
# Estructura: de mi objeto {ISBN: {'titulo': '', 'autor': '', 'prestado': False}}
biblioteca = {}

def agregar_libro(isbn):
    """Solicita los datos y agrega un nuevo libro a la biblioteca."""
    if isbn in biblioteca:
        print(f"❌ Error: Ya existe un libro con el ISBN {isbn}.")
        return

    print(f"\n--- Agregando libro con ISBN: {isbn} ---")
    titulo = input("Ingresa el título del libro: ")
    autor = input("Ingresa el autor del libro: ")

    biblioteca[isbn] = {
        'titulo': titulo,
        'autor': autor,
        'prestado': False  # El libro inicialmente no está prestado
    }
    print(f"✅ Libro '{titulo}' de {autor} agregado exitosamente.")

def prestar_libro(isbn):
    """Marca un libro como prestado si está disponible."""
    if isbn not in biblioteca:
        print(f"❌ Error: El libro con ISBN {isbn} no se encuentra en la biblioteca.")
        return

    libro = biblioteca[isbn]
    if libro['prestado']:
        print(f"⚠️ Aviso: El libro '{libro['titulo']}' ya se encuentra prestado.")
    else:
        libro['prestado'] = True
        print(f"✅ Libro '{libro['titulo']}' prestado exitosamente.")

def devolver_libro(isbn):
    """Marca un libro como disponible si estaba prestado."""
    if isbn not in biblioteca:
        print(f"❌ Error: El libro con ISBN {isbn} no se encuentra en la biblioteca.")
        return

    libro = biblioteca[isbn]
    if not libro['prestado']:
        print(f"⚠️ Aviso: El libro '{libro['titulo']}' no estaba prestado.")
    else:
        libro['prestado'] = False
        print(f"✅ Libro '{libro['titulo']}' devuelto exitosamente.")

def buscar_libro_por_titulo():
    """Busca libros por título (búsqueda parcial insensible a mayúsculas)."""
    termino = input("Ingresa el título o parte del título a buscar: ").lower()
    encontrados = []

    for isbn, detalles in biblioteca.items():
        if termino in detalles['titulo'].lower():
            encontrados.append((isbn, detalles))

    if not encontrados:
        print("🔍 No se encontraron libros con ese título.")
    else:
        print(f"\n--- {len(encontrados)} Libro(s) Encontrado(s) ---")
        for isbn, detalles in encontrados:
            estado = "PRESTADO" if detalles['prestado'] else "DISPONIBLE"
            print(f"ISBN: {isbn} | Título: {detalles['titulo']} | Autor: {detalles['autor']} | Estado: {estado}")

def mostrar_todos_los_libros():
    """Muestra todos los libros en la biblioteca."""
    if not biblioteca:
        print("📖 La biblioteca está vacía.")
        return

    print("\n--- Catálogo Completo de la Biblioteca ---")
    for isbn, detalles in biblioteca.items():
        estado = "PRESTADO" if detalles['prestado'] else "DISPONIBLE"
        print(f"ISBN: {isbn} | Título: {detalles['titulo']} | Autor: {detalles['autor']} | Estado: {estado}")

def menu():
    """Función principal que muestra el menú e interactúa con el usuario."""
    while True:
        print("\n--- Menú de Gestión de Biblioteca ---")
        print("1. Agregar un libro")
        print("2. Prestar un libro (por ISBN)")
        print("3. Devolver un libro (por ISBN)")
        print("4. Buscar libro por título")
        print("5. Mostrar todos los libros")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            isbn = input("Ingresa el ISBN del nuevo libro: ")
            agregar_libro(isbn)
        elif opcion == '2':
            isbn = input("Ingresa el ISBN del libro a prestar: ")
            prestar_libro(isbn)
        elif opcion == '3':
            isbn = input("Ingresa el ISBN del libro a devolver: ")
            devolver_libro(isbn)
        elif opcion == '4':
            buscar_libro_por_titulo()
        elif opcion == '5':
            mostrar_todos_los_libros()
        elif opcion == '6':
            print("👋 Saliendo del sistema de biblioteca. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar la aplicación
menu()