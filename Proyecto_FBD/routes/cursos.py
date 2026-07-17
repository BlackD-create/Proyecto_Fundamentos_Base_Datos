from flask import Blueprint, render_template, request, redirect, flash

import mysql.connector

from models.curso_model import (
    obtener_cursos,
    obtener_curso_por_codigo,
    insertar_curso,
    actualizar_curso,
    eliminar_curso
)

from models.docente_model import obtener_docentes
from models.departamento_model import obtener_departamentos


cursos_bp = Blueprint(
    "cursos",
    __name__
)


@cursos_bp.route("/cursos")
def listar():

    cursos = obtener_cursos()

    return render_template(
        "cursos/listar.html",
        cursos=cursos
    )


@cursos_bp.route("/cursos/nuevo", methods=["GET", "POST"])
def nuevo():

    docentes = obtener_docentes()
    departamentos = obtener_departamentos()

    if request.method == "POST":

        insertar_curso(

            request.form["codigo"],
            request.form["nombre"],
            request.form["creditos"],
            request.form["cedula"],
            request.form["codigo_dep"]

        )

        return redirect("/cursos")

    return render_template(

        "cursos/nuevo.html",

        docentes=docentes,
        departamentos=departamentos

    )


@cursos_bp.route("/cursos/editar/<string:codigo>", methods=["GET", "POST"])
def editar(codigo):

    curso = obtener_curso_por_codigo(codigo)

    docentes = obtener_docentes()
    departamentos = obtener_departamentos()

    if request.method == "POST":

        actualizar_curso(

            codigo,
            request.form["nombre"],
            request.form["creditos"],
            request.form["cedula"],
            request.form["codigo_dep"]

        )

        return redirect("/cursos")

    return render_template(

        "cursos/editar.html",

        curso=curso,
        docentes=docentes,
        departamentos=departamentos

    )


@cursos_bp.route("/cursos/eliminar/<string:codigo>")
def eliminar(codigo):

    try:

        eliminar_curso(codigo)

    except mysql.connector.Error as err:

        if err.errno == 1451:

            flash("No se puede eliminar el curso porque existen estudiantes inscritos en él.", "danger")

        else:

            flash(f"Error inesperado de base de datos: {err.msg}", "danger")

    return redirect("/cursos")