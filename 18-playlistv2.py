playlists = {} #se crea el diccionario vacio 

def crear_playlist():
    nombre_playlist = input('Cómo deseas nombrar tu playlist:\n')
    playlists[nombre_playlist] = []
    return nombre_playlist #función que retornan un valor en este caso el  nombre de la playlist
                            

def agregar_canciones(playlist_nombre):
    print('Agregando canciones a la playlist:', playlist_nombre)
    while True:
        cancion = input('Ingresa el nombre de la canción (o "X" para salir): ')
        if cancion.lower() == 'x':
            break
        playlists[playlist_nombre].append(cancion) #metodo que agrega una cancion a la playlist
        print('Canción agregada:', cancion)

def eliminar_canciones(playlist_nombre):
    print('Eliminando canciones de la playlist:', playlist_nombre)
    while True:
        cancion_eliminar = input('Ingresa el nombre de la canción a eliminar (o "X" para salir): ')
        if cancion_eliminar.lower() == 'x':
            break
        if cancion_eliminar in playlists[playlist_nombre]:
            playlists[playlist_nombre].remove(cancion_eliminar)
            print('Canción eliminada:', cancion_eliminar)
        else:
            print('La canción no se encuentra en la playlist.')

def mostrar_playlists():
    if not playlists:
        print("No hay playlists creadas.")
    else:
        for nombre_playlist, canciones in playlists.items():
            print(f"Playlist: {nombre_playlist}")
            for cancion in canciones:
                print(f"- {cancion}")

def app():
    while True:
        print("\nMenú:")
        print("1. Crear una nueva playlist")
        print("2. Agregar canciones a una playlist")
        print("3. Eliminar canciones de una playlist")
        print("4. Mostrar todas las playlists")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre_playlist = crear_playlist()
            agregar_canciones(nombre_playlist)
        elif opcion == '2':
            nombre_playlist = input("¿A qué playlist deseas agregar canciones? ")
            if nombre_playlist in playlists:
                agregar_canciones(nombre_playlist)
            else:
                print("La playlist no existe.")
        elif opcion == '3':
            nombre_playlist = input("¿De qué playlist deseas eliminar canciones? ")
            if nombre_playlist in playlists:
                eliminar_canciones(nombre_playlist)
            else:
                print("La playlist no existe.")
        elif opcion == '4':
            mostrar_playlists()
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")

app()