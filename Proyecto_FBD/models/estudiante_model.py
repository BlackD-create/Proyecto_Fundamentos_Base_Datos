from database.conexion import obtener_conexion


def obtener_estudiantes():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM estudiante
        ORDER BY matricula ASC
    """)

    estudiantes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return estudiantes


def obtener_estudiante_por_matricula(matricula):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    sql = "SELECT * FROM estudiante WHERE matricula = %s"

    cursor.execute(sql, (matricula,))

    estudiante = cursor.fetchone()

    cursor.close()
    conexion.close()

    return estudiante


def insertar_estudiante(matricula, nombre, correo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO estudiante (matricula, nombre, correo)
        VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (matricula, nombre, correo))

    conexion.commit()

    cursor.close()
    conexion.close()


def actualizar_estudiante(matricula, nombre, correo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = """
        UPDATE estudiante
        SET nombre = %s,
            correo = %s
        WHERE matricula = %s
    """

    cursor.execute(sql, (nombre, correo, matricula))

    conexion.commit()

    cursor.close()
    conexion.close()


def eliminar_estudiante(matricula):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    sql = "DELETE FROM estudiante WHERE matricula = %s"

    cursor.execute(sql, (matricula,))

    conexion.commit()

    cursor.close()
    conexion.close()

def contar_estudiantes():
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT COUNT(*) FROM estudiante")
        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total