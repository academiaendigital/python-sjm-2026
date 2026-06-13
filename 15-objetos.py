#OBJETOS 
#un objeto como ya sabemos es similar a un array, te permite agrupar contenido
#diferentes tipos de datos
#AQUI SE CONOCEN COMO DICCIONARIOS

cancion = {
    'artista': 'Ricardo Arjona',
    'nombre': 'El problema'
}
#acceder a los elementos del dicionario
print(cancion['artista'])
artista = cancion['artista']
print(artista)


#agregar un key al diccionario 
cancion['playlist_id'] = 'Romantica'
print(cancion)

#eliminar el valor de un diccionario
del cancion['playlist_id']
print(cancion)
