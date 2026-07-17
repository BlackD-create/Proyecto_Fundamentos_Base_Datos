from database.conexion import obtener_conexion


def obtener_docentes():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""

        SELECT

            d.cedula,
            d.nombre,
            d.especialidad,
            d.codigo_dep,

            dep.nombre AS departamento

        FROM docente d

        INNER JOIN departamento dep
            ON d.codigo_dep = dep.codigo

        ORDER BY d.cedula ASC

    """)

    docentes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return docentes


def obtener_docente_por_cedula(cedula):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""

        SELECT *

        FROM docente

        WHERE cedula=%s

    """, (cedula,))

    docente = cursor.fetchone()

    cursor.close()
    conexion.close()

    return docente


def insertar_docente(
        cedula,
        nombre,
        especialidad,
        codigo_dep
):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""

        INSERT INTO docente(

            cedula,
            nombre,
            especialidad,
            codigo_dep

        )

        VALUES(%s,%s,%s,%s)

    """,(

        cedula,
        nombre,
        especialidad,
        codigo_dep

    ))

    conexion.commit()

    cursor.close()
    conexion.close()


def actualizar_docente(

        cedula,
        nombre,
        especialidad,
        codigo_dep

):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""

        UPDATE docente

        SET

            nombre=%s,
            especialidad=%s,
            codigo_dep=%s

        WHERE cedula=%s

    """,(

        nombre,
        especialidad,
        codigo_dep,
        cedula

    ))

    conexion.commit()

    cursor.close()
    conexion.close()


def eliminar_docente(cedula):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(

        "DELETE FROM docente WHERE cedula=%s",

        (cedula,)

    )

    conexion.commit()

    cursor.close()
    conexion.close()

def contar_docentes():
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT COUNT(*) FROM docente")
        total = cursor.fetchone()[0]

        cursor.close()
        conexion.close()

        return total