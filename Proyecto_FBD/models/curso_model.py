from database.conexion import obtener_conexion


def obtener_cursos():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""

        SELECT

            c.codigo,
            c.nombre,
            c.creditos,

            c.cedula,
            c.codigo_dep,

            d.nombre AS docente,

            dep.nombre AS departamento

        FROM curso c

        INNER JOIN docente d
            ON c.cedula = d.cedula

        INNER JOIN departamento dep
            ON c.codigo_dep = dep.codigo

        ORDER BY c.nombre

    """)

    cursos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return cursos


def obtener_curso_por_codigo(codigo):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""

        SELECT *

        FROM curso

        WHERE codigo=%s

    """, (codigo,))

    curso = cursor.fetchone()

    cursor.close()
    conexion.close()

    return curso


def insertar_curso(
        codigo,
        nombre,
        creditos,
        cedula,
        codigo_dep
):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""

        INSERT INTO curso(

            codigo,
            nombre,
            creditos,
            cedula,
            codigo_dep

        )

        VALUES(%s,%s,%s,%s,%s)

    """, (

        codigo,
        nombre,
        creditos,
        cedula,
        codigo_dep

    ))

    conexion.commit()

    cursor.close()
    conexion.close()


def actualizar_curso(
        codigo,
        nombre,
        creditos,
        cedula,
        codigo_dep
):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""

        UPDATE curso

        SET

            nombre=%s,
            creditos=%s,
            cedula=%s,
            codigo_dep=%s

        WHERE codigo=%s

    """, (

        nombre,
        creditos,
        cedula,
        codigo_dep,
        codigo

    ))

    conexion.commit()

    cursor.close()
    conexion.close()


def eliminar_curso(codigo):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(

        "DELETE FROM curso WHERE codigo=%s",

        (codigo,)

    )

    conexion.commit()

    cursor.close()
    conexion.close()
def contar_cursos():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM curso")
    total = cursor.fetchone()[0]

    cursor.close()
    conexion.close()

    return total