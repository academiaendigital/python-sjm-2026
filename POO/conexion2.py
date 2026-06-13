import pymysql

# --- Parámetros de Conexión ---
# ¡IMPORTANTE! Reemplaza los valores con tus credenciales reales de la base de datos
DB_HOST = "localhost"  # O la IP de tu servidor MySQL
DB_USER = "root"
DB_PASS = ""
DB_NAME = "clinica" 

conn = None # La variable de conexión
cur = None  # La variable del cursor

try:
    # 1. Establecer la conexión
    print("Intentando conectar a MySQL con PyMySQL...")
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME)
    
    # 2. Crear un cursor (el objeto que ejecuta las sentencias SQL)
    cur = conn.cursor()
    print("¡Conexión exitosa!")
    
    # --- EJEMPLO: Ejecutar una consulta simple ---
    sql_query = "SELECT @@version;"
    cur.execute(sql_query)
    
    # Obtener el resultado
    db_version = cur.fetchone()
    print(f"Versión de MySQL: {db_version[0]}")
    
    # --- Aquí puedes añadir tu código para INSERT, UPDATE, SELECT, etc. ---
    
    # Si haces un INSERT, UPDATE o DELETE, debes confirmar los cambios:
    # conn.commit()
    
except pymysql.Error as e:
    # Capturar errores específicos de PyMySQL
    print(f"Error de PyMySQL: {e}")
    
except Exception as e:
    # Capturar otros errores inesperados
    print(f"Ocurrió un error inesperado: {e}")
    
finally:
    # 3. Cerrar la conexión y el cursor (¡Fundamental para liberar recursos!)
    if cur is not None:
        cur.close()
        # print("Cursor cerrado.")
    if conn is not None:
        conn.close()
        print("Conexión con MySQL cerrada.")