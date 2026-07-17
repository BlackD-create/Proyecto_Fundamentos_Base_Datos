from database.conexion import obtener_conexion


def obtener_departamentos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM departamento
        ORDER BY codigo ASC
    """)

    departamentos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return departamentos


def obtener_departamento_por_codigo(codigo):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM departamento WHERE codigo=%s",
        (codigo,)
    )

    departamento = cursor.fetchone()

    cursor.close()
    conexion.close()

    return departamento


def insertar_departamento(codigo, nombre):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO departamento(codigo,nombre)
        VALUES(%s,%s)
    """, (codigo, nombre))

    conexion.commit()

    cursor.close()
    conexion.close()


def actualizar_departamento(codigo, nombre):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE departamento
        SET nombre=%s
        WHERE codigo=%s
    """, (nombre, codigo))

    conexion.commit()

    cursor.close()
    conexion.close()


def eliminar_departamento(codigo):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM departamento WHERE codigo=%s",
        (codigo,)
    )

    conexion.commit()

    cursor.close()
    conexion.close()
def contar_departamentos():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM departamento")
    total = cursor.fetchone()[0]

    cursor.close()
    conexion.close()

    return total