from database.conexion import obtener_conexion


def obtener_evaluaciones():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""

        SELECT
            ev.id_eval,
            ev.id,
            ev.nota,
            ev.tipo,
            e.nombre AS estudiante,
            c.nombre AS curso,
            i.periodo
        FROM evaluacion ev
        INNER JOIN inscripcion i 
            ON ev.id = i.id
        INNER JOIN estudiante e 
            ON i.matricula = e.matricula
        INNER JOIN curso c 
            ON i.codigo_curso = c.codigo
        ORDER BY ev.id_eval ASC

    """)

    evaluaciones = cursor.fetchall()

    cursor.close()
    conexion.close()

    return evaluaciones


def obtener_evaluacion_por_id(id_eval):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""

        SELECT * FROM evaluacion 
        WHERE id_eval=%s

    """, (id_eval,))

    evaluacion = cursor.fetchone()

    cursor.close()
    conexion.close()

    return evaluacion


def insertar_evaluacion(
        id,
        nota,
        tipo
):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""

        INSERT INTO evaluacion(
            id,
            nota,
            tipo
        )
        VALUES(%s,%s,%s)

    """, (
        id,
        nota,
        tipo
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


def actualizar_evaluacion(
        id_eval,
        id,
        nota,
        tipo
):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""

        UPDATE evaluacion
        SET
            id=%s,
            nota=%s,
            tipo=%s
        WHERE id_eval=%s

    """, (
        id,
        nota,
        tipo,
        id_eval
    ))

    conexion.commit()

    cursor.close()
    conexion.close()


def eliminar_evaluacion(id_eval):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM evaluacion WHERE id_eval=%s",
        (id_eval,)
    )

    conexion.commit()

    cursor.close()
    conexion.close()
def contar_evaluaciones():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM evaluacion")
    total = cursor.fetchone()[0]

    cursor.close()
    conexion.close()

    return total