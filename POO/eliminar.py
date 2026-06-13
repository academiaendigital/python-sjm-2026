id_a_eliminar = 4  # Reemplaza con el ID del registro que quieres eliminar

    # Verificar si el registro existe
    cursor.execute("SELECT 1 FROM pacientes WHERE paciente_id = %s", (id_a_eliminar,))
    if cursor.fetchone() is None:
        print(f"Registro con ID {id_a_eliminar} no encontrado.")
    else:
        sql = "DELETE FROM pacientes WHERE paciente_id = %s"
        valores = (id_a_eliminar,)
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"Registro con ID {id_a_eliminar} eliminado correctamente.")
        if cursor.rowcount == 0:
            print("No se eliminó ningún registro.")
            
    datos_variados = [
    ("Producto1", 10.99, 50),
    ("Producto2", 25.50, 100),
    ("Producto3", 5.75, 200)
]

sql_variado = "INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s)"
cursor.executemany(sql_variado, datos_variados)