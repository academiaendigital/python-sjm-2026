playlist = {}
playlist['canciones'] = [] #CRE UN DICCIONARIO

def app(): #funcion principal  para el ejercicio
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Cómo deseas nombrar tu playlist:\n')

        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False  # YA TENEMOS UN NOMBRE DESACTIVAMOS EL TRUE 
            agregar_canciones() 
            mostrar_resumen()
            eliminar_canciones()
           
           

def agregar_canciones():#definir el nombnre de la función
    print('Agregando canciones a la playlist:', playlist['nombre']) #esto se va imprimir en la terminal
    while True: #mientras se cumpla 
        cancion = input('Ingresa el nombre de la canción (o "X" para salir): ')
        if cancion.lower() == 'x':
            
            break #DEJAR DE AGREGAR CANCIONES
        
        playlist['canciones'].append(cancion) 
        
        print('Canción agregada:', cancion)
        
    print('¡Playlist completa!')
    print(playlist)


def eliminar_canciones():
    print('Eliminando canciones de la playlist:', playlist['nombre'])
    while True:
        cancion_eliminar = input('Ingresa el nombre de la canción a eliminar (o "X" para salir): ')
        if cancion_eliminar.lower() == 'x':
            break
        if cancion_eliminar in playlist['canciones']:
            playlist['canciones'].remove(cancion_eliminar)
            print('Canción eliminada:', cancion_eliminar)
        else:
            print('La canción no se encuentra en la playlist.')

    print('¡Playlist actualizada!')
    print(playlist)


def mostrar_resumen():
    print(f'Playlis', playlist['nombre'] )
    print('Canciones de la playlist:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)
    
app()