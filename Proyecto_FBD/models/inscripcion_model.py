from database.conexion import obtener_conexion


def obtener_inscripciones():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""

        SELECT
            i.id,
            i.matricula,
            i.codigo_curso,
            i.periodo,
            e.nombre AS estudiante,
            c.nombre AS curso
        FROM inscripcion i
        INNER JOIN estudiante e 
            ON i.matricula = e.matricula
        INNER JOIN curso c 
            ON i.codigo_curso = c.codigo
        ORDER BY i.id ASC

    """)

    inscripciones = cursor.fetchall()

    cursor.close()
    conexion.close()

    return inscripciones


def obtener_inscripcion_por_id(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""

        SELECT * FROM inscripcion 
        WHERE id=%s

    """, (id,))

    inscripcion = cursor.fetchone()

    cursor.close()
    conexion.close()

    return inscripcion


def insertar_inscripcion(
        matricula,
        codigo_curso,
        periodo
):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""

        INSERT INTO inscripcion(
            matricula,
            codigo_curso,
            periodo
        )
        VALUES(%s,%s,%s)

    """, (
        matricula,
        codigo_curso,
        periodo
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


def actualizar_inscripcion(
        id,
        matricula,
        codigo_curso,
        periodo
):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""

        UPDATE inscripcion
        SET
            matricula=%s,
            codigo_curso=%s,
            periodo=%s
        WHERE id=%s

    """, (
        matricula,
        codigo_curso,
        periodo,
        id
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


def eliminar_inscripcion(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM inscripcion WHERE id=%s",
        (id,)
    )

    conexion.commit()

    cursor.close()
    conexion.close()
def contar_inscripciones():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM inscripcion")
    total = cursor.fetchone()[0]

    cursor.close()
    conexion.close()

    return total