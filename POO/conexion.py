#pip install mysql-connector-python

# Scikit-learn:
#Proporciona herramientas para el aprendizaje automático.
#Incluye algoritmos para clasificación, regresión, clustering y reducción de dimensionalidad.
#TensorFlow y PyTorch:
#Son bibliotecas para el aprendizaje profundo.
#Permiten construir y entrenar redes neuronales.
#FLASK Y  DJANGO
#OS

import mysql.connector
#import pymysql
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Reemplaza con tu contraseña
            database="endigital",  # Reemplaza con el nombre de tu base de datos
            port=3306
        )
        print("Conexión a la base de datos establecida con éxito.") #Mensaje de exito.
        return conexion
    except mysql.connector.Error as error: #si hay un error de MySQL.
        print(f"Error al conectar a MySQL: {error}")
        return None
    except Exception as error: #si hay un error inesperado.
        print(f"Error inesperado: {error}")
        return None
    #finally:
        #Bloque finally, para futuras implementaciones. como cerrar la conexion.
        #if conexion.is_connected():
            #conexion.close()
        #print("Conexión cerrada")
        
        #pass
        
conexion = conectar_bd()        

