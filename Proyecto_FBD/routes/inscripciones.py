from flask import Blueprint, render_template, request, redirect

from models.inscripcion_model import (
    obtener_inscripciones,
    obtener_inscripcion_por_id,
    insertar_inscripcion,
    actualizar_inscripcion,
    eliminar_inscripcion
)

from models.estudiante_model import obtener_estudiantes
from models.curso_model import obtener_cursos


inscripciones_bp = Blueprint(
    "inscripciones",
    __name__
)


@inscripciones_bp.route("/inscripciones")
def listar():

    inscripciones = obtener_inscripciones()

    return render_template(
        "inscripciones/listar.html",
        inscripciones=inscripciones
    )


@inscripciones_bp.route("/inscripciones/nuevo", methods=["GET", "POST"])
def nuevo():

    estudiantes = obtener_estudiantes()
    cursos = obtener_cursos()

    if request.method == "POST":

        insertar_inscripcion(
            request.form["matricula"],
            request.form["codigo_curso"],
            request.form["periodo"]
        )

        return redirect("/inscripciones")

    return render_template(
        "inscripciones/nuevo.html",
        estudiantes=estudiantes,
        cursos=cursos
    )


@inscripciones_bp.route("/inscripciones/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    inscripcion = obtener_inscripcion_por_id(id)

    estudiantes = obtener_estudiantes()
    cursos = obtener_cursos()

    if request.method == "POST":

        actualizar_inscripcion(
            id,
            request.form["matricula"],
            request.form["codigo_curso"],
            request.form["periodo"]
        )

        return redirect("/inscripciones")

    return render_template(
        "inscripciones/editar.html",
        inscripcion=inscripcion,
        estudiantes=estudiantes,
        cursos=cursos
    )


@inscripciones_bp.route("/inscripciones/eliminar/<int:id>")
def eliminar(id):

    eliminar_inscripcion(id)

    return redirect("/inscripciones")