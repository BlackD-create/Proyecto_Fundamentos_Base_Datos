from flask import Blueprint, render_template, request, redirect, flash

import mysql.connector

from models.departamento_model import (
    obtener_departamentos,
    obtener_departamento_por_codigo,
    insertar_departamento,
    actualizar_departamento,
    eliminar_departamento
)

departamentos_bp = Blueprint(
    "departamentos",
    __name__
)


@departamentos_bp.route("/departamentos")
def listar():

    departamentos = obtener_departamentos()

    return render_template(
        "departamentos/listar.html",
        departamentos=departamentos
    )


@departamentos_bp.route("/departamentos/nuevo", methods=["GET","POST"])
def nuevo():

    if request.method == "POST":

        insertar_departamento(

            request.form["codigo"],
            request.form["nombre"]

        )

        return redirect("/departamentos")

    return render_template("departamentos/nuevo.html")


@departamentos_bp.route("/departamentos/editar/<int:codigo>", methods=["GET","POST"])
def editar(codigo):

    departamento = obtener_departamento_por_codigo(codigo)

    if request.method == "POST":

        actualizar_departamento(

            codigo,
            request.form["nombre"]

        )

        return redirect("/departamentos")

    return render_template(

        "departamentos/editar.html",

        departamento=departamento

    )


@departamentos_bp.route("/departamentos/eliminar/<int:codigo>")
def eliminar(codigo):

    try:

        eliminar_departamento(codigo)

    except mysql.connector.Error as err:

        if err.errno == 1451:

            flash("No se puede eliminar el departamento porque tiene docentes o cursos asociados.", "danger")

        else:

            flash(f"Error inesperado de base de datos: {err.msg}", "danger")

    return redirect("/departamentos")