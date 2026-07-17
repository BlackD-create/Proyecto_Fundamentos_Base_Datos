from flask import Blueprint, render_template, request, redirect

from models.evaluacion_model import (
    obtener_evaluaciones,
    obtener_evaluacion_por_id,
    insertar_evaluacion,
    actualizar_evaluacion,
    eliminar_evaluacion
)

from models.inscripcion_model import obtener_inscripciones


evaluaciones_bp = Blueprint(
    "evaluaciones",
    __name__
)


@evaluaciones_bp.route("/evaluaciones")
def listar():

    evaluaciones = obtener_evaluaciones()

    return render_template(
        "evaluaciones/listar.html",
        evaluaciones=evaluaciones
    )


@evaluaciones_bp.route("/evaluaciones/nuevo", methods=["GET", "POST"])
def nuevo():

    inscripciones = obtener_inscripciones()

    if request.method == "POST":

        insertar_evaluacion(
            request.form["id"],
            request.form["nota"],
            request.form["tipo"]
        )

        return redirect("/evaluaciones")

    return render_template(
        "evaluaciones/nuevo.html",
        inscripciones=inscripciones
    )


@evaluaciones_bp.route("/evaluaciones/editar/<int:id_eval>", methods=["GET", "POST"])
def editar(id_eval):

    evaluacion = obtener_evaluacion_por_id(id_eval)

    inscripciones = obtener_inscripciones()

    if request.method == "POST":

        actualizar_evaluacion(
            id_eval,
            request.form["id"],
            request.form["nota"],
            request.form["tipo"]
        )

        return redirect("/evaluaciones")

    return render_template(
        "evaluaciones/editar.html",
        evaluacion=evaluacion,
        inscripciones=inscripciones
    )


@evaluaciones_bp.route("/evaluaciones/eliminar/<int:id_eval>")
def eliminar(id_eval):

    eliminar_evaluacion(id_eval)

    return redirect("/evaluaciones")