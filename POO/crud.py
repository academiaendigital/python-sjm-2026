from conexion import conectar_bd
import mysql.connector

def crear_registro(conexion, nombre, apellido, fecha_nacimiento, genero,cedula, telefono, direccion):
    cursor = conexion.cursor()
    sql = "INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, genero,cedula, telefono, direccion) VALUES (%s, %s, %s, %s, %s,%s, %s, %s)"
    valores = (nombre, apellido, fecha_nacimiento, genero,cedula, telefono, direccion)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tu datos se han ingresado con éxito")
    cursor.close()

def leer_registros(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM pacientes")
    resultados = cursor.fetchall()
    for pacientes in resultados:
        print(pacientes)
    cursor.close()

def actualizar_registro(conexion, id_paciente, nombre, edad):
    cursor = conexion.cursor()
    try:
        sql = "UPDATE pacientes SET nombre = %s, edad = %s WHERE id_paciente = %s"
        valores = (nombre, edad, id_paciente)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Tus datos se actualizaron con éxito.")
    except mysql.connector.Error as error:
        print(f"Error al actualizar el registro: {error}")
    finally:
        cursor.close()


def eliminar_registro(conexion,id_paciente ):
    cursor = conexion.cursor()
    sql = "DELETE FROM pacientes WHERE id_paciente = %s"
    valores = (id_paciente )
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tu datos se han eliminado con éxito.")
    cursor.close()

conexion = conectar_bd()




if conexion:
    #leer_registros(conexion)
    #actualizar_registro(conexion, 4, "2ASDASDA3",84)
    leer_registros(conexion)
    #eliminar_registro(conexion, 4)
    #leer_registros(conexion)
    conexion.close()
