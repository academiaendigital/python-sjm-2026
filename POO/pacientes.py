# app.py
from flask import Flask, render_template
from conexion import conectar_bd # Importa la función de conexión de tu archivo 'conexion.py'
import mysql.connector

app = Flask(__name__)

def leer_registros():
    """Conecta a la BD, lee todos los pacientes y devuelve una lista de tuplas."""
    conexion = conectar_bd() # Llama a tu función de conexión
    resultados = []
    
    if conexion is None:
        print("Error: No se pudo establecer la conexión a la base de datos.")
        return resultados

    cursor = None
    try:
        # Aquí se usa el cursor para ejecutar la consulta
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pacientes")
        resultados = cursor.fetchall()
        
    except mysql.connector.Error as error:
        print(f"Error al leer los datos en Sistema: {error}")
        
    finally:
        if cursor is not None:
            cursor.close()
        if conexion.is_connected():
            conexion.close() # Cierra la conexión después de la operación
            
    return resultados


# --- RUTA PRINCIPAL DE FLASK (Renderizado) ---

@app.route('/')
def listar_pacientes():
    # 1. Obtener datos de la base de datos
    datos_pacientes = leer_registros()
    
    # 2. Renderizar la plantilla HTML, pasándole los datos
    return render_template(
        'pacientes.html', # nombre del archivos dentro de la carpeta de tempplates que se va renderizar
        pacientes=datos_pacientes, 
        titulo="Lista de Pacientes" # Aca se pueden declarar todas las variables fijas que necesiten
    )

# --- INICIO DEL SERVIDOR ---
if __name__ == '__main__':
    # Asegúrate de que tu servidor MySQL (XAMPP/WAMP) esté corriendo.
    app.run(debug=True)