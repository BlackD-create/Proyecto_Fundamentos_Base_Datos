from flask import Blueprint, render_template, request, redirect, flash

import mysql.connector

from models.docente_model import (
    obtener_docentes,
    obtener_docente_por_cedula,
    insertar_docente,
    actualizar_docente,
    eliminar_docente
)

from models.departamento_model import obtener_departamentos

docentes_bp = Blueprint(
    "docentes",
    __name__
)


@docentes_bp.route("/docentes")
def listar():

    docentes = obtener_docentes()

    return render_template(
        "docentes/listar.html",
        docentes=docentes
    )


@docentes_bp.route("/docentes/nuevo", methods=["GET", "POST"])
def nuevo():

    departamentos = obtener_departamentos()

    if request.method == "POST":

        insertar_docente(

            request.form["cedula"],
            request.form["nombre"],
            request.form["especialidad"],
            request.form["codigo_dep"]

        )

        return redirect("/docentes")

    return render_template(

        "docentes/nuevo.html",

        departamentos=departamentos

    )


@docentes_bp.route("/docentes/editar/<string:cedula>", methods=["GET", "POST"])
def editar(cedula):

    docente = obtener_docente_por_cedula(cedula)

    departamentos = obtener_departamentos()

    if request.method == "POST":

        actualizar_docente(

            cedula,

            request.form["nombre"],
            request.form["especialidad"],
            request.form["codigo_dep"]

        )

        return redirect("/docentes")

    return render_template(

        "docentes/editar.html",

        docente=docente,

        departamentos=departamentos

    )


@docentes_bp.route("/docentes/eliminar/<string:cedula>")
def eliminar(cedula):

    try:

        eliminar_docente(cedula)

    except mysql.connector.Error as err:

        if err.errno == 1451:

            flash("No se puede eliminar al docente porque tiene cursos asignados a su cargo.", "danger")

        else:

            flash(f"Error inesperado de base de datos: {err.msg}", "danger")

    return redirect("/docentes")