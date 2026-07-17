from flask import Flask, render_template
from routes.estudiantes import estudiantes_bp
from routes.departamentos import departamentos_bp
from routes.docentes import docentes_bp
from routes.cursos import cursos_bp
from routes.inscripciones import inscripciones_bp
from routes.evaluaciones import evaluaciones_bp

# Importamos las funciones de conteo de cada modelo
from models.estudiante_model import contar_estudiantes
from models.docente_model import contar_docentes
from models.curso_model import contar_cursos
from models.departamento_model import contar_departamentos
from models.inscripcion_model import contar_inscripciones
from models.evaluacion_model import contar_evaluaciones

app = Flask(__name__)

app.secret_key = "espoch_gestion_universitaria_secret_key_2026"

app.register_blueprint(estudiantes_bp)
app.register_blueprint(departamentos_bp)
app.register_blueprint(docentes_bp)
app.register_blueprint(cursos_bp)
app.register_blueprint(inscripciones_bp)
app.register_blueprint(evaluaciones_bp)

@app.route("/")
def inicio():

    # Obtenemos los totales reales desde la base de datos
    totales = {
        "estudiantes": contar_estudiantes(),
        "docentes": contar_docentes(),
        "cursos": contar_cursos(),
        "departamentos": contar_departamentos(),
        "inscripciones": contar_inscripciones(),
        "evaluaciones": contar_evaluaciones()
    }

    return render_template("index.html", totales=totales)

if __name__ == "__main__":
    app.run(debug=True)