from flask import Blueprint, render_template, request, redirect

from models.estudiante_model import (
    obtener_estudiantes,
    insertar_estudiante,
    obtener_estudiante_por_matricula,
    actualizar_estudiante,
    eliminar_estudiante
)

estudiantes_bp = Blueprint("estudiantes", __name__)


# ==========================
# LISTAR
# ==========================
@estudiantes_bp.route("/estudiantes")
def listar():

    estudiantes = obtener_estudiantes()

    return render_template(
        "estudiantes/listar.html",
        estudiantes=estudiantes
    )


# ==========================
# NUEVO
# ==========================
@estudiantes_bp.route("/estudiantes/nuevo", methods=["GET", "POST"])
def nuevo():

    if request.method == "POST":

        insertar_estudiante(
            request.form["matricula"],
            request.form["nombre"],
            request.form["correo"]
        )

        return redirect("/estudiantes")

    return render_template("estudiantes/nuevo.html")


# ==========================
# EDITAR
# ==========================
@estudiantes_bp.route("/estudiantes/editar/<string:matricula>", methods=["GET", "POST"])
def editar(matricula):

    if request.method == "POST":

        actualizar_estudiante(
            matricula,
            request.form["nombre"],
            request.form["correo"]
        )

        return redirect("/estudiantes")

    estudiante = obtener_estudiante_por_matricula(matricula)

    return render_template(
        "estudiantes/editar.html",
        estudiante=estudiante
    )


# ==========================
# ELIMINAR
# ==========================
@estudiantes_bp.route("/estudiantes/eliminar/<string:matricula>")
def eliminar(matricula):

    eliminar_estudiante(matricula)

    return redirect("/estudiantes")