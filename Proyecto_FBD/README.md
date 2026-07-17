# Sistema de Gestión Universitaria

## Descripción

El Sistema de Gestión Universitaria es una aplicación web desarrollada utilizando
**Python**, **Flask** y **MySQL**, 
cuyo propósito es facilitar la administración de la información académica de una institución educativa.

El sistema permite gestionar estudiantes, docentes, departamentos, cursos, inscripciones 
y evaluaciones mediante una interfaz web intuitiva, ofreciendo las operaciones básicas de registro, 
consulta, actualización y eliminación de información (CRUD).

---

## Tecnologías utilizadas

- Python 3.14
- Flask 3.1.3
- MySQL Server
- MySQL Workbench
- MySQL Connector/Python
- HTML5
- Bootstrap 5
- PyCharm (IDE principal)
- Visual Studio Code (compatible)

---

## Estructura del proyecto

```text
Sistema_Gestion_Universidad/
│
├── Manual_Implementacion.pdf
├── README.md
├── gestion_universidad.sql
│
└── gestion_universidad/
    ├── app.py
    ├── config.py
    ├── requirements.txt
    ├── database/
    ├── models/
    ├── routes/
    ├── static/
    └── templates/
```

---

## Requisitos del sistema

- Windows 10 o superior.
- Python 3.14 o superior.
- MySQL Server.
- MySQL Workbench.
- PyCharm o Visual Studio Code.
- Navegador web moderno (Brave, Google Chrome, Microsoft Edge, Mozilla Firefox, entre otros).

---

## Instalación

Para realizar la instalación y configuración del sistema, consulte el documento:

**Manual_Implementacion.pdf**

En dicho manual se describe el procedimiento para:

- Instalar Python y MySQL.
- Configurar la base de datos.
- Instalar las dependencias del proyecto.
- Ejecutar la aplicación.
- Resolver problemas comunes durante la implementación.

---

## Instalación de dependencias

Las dependencias del proyecto se encuentran especificadas en el archivo **requirements.txt**.

Instalación mediante `pip`:

```bash
pip install -r requirements.txt
```

O utilizando el lanzador de Python en Windows:

```bash
py -m pip install -r requirements.txt
```

En caso de ser necesario, las dependencias principales pueden instalarse manualmente:

```bash
pip install Flask
pip install mysql-connector-python
```

---

## Ejecución del proyecto

Una vez configurada la base de datos e instaladas las dependencias, ejecutar el archivo principal:

```bash
python app.py
```

o

```bash
py app.py
```

Posteriormente, abrir un navegador web e ingresar a:

```
http://127.0.0.1:5000
```

---

## Funcionalidades

El sistema permite administrar la siguiente información:

- Gestión de estudiantes.
- Gestión de docentes.
- Gestión de departamentos.
- Gestión de cursos.
- Gestión de inscripciones.
- Gestión de evaluaciones.

Cada módulo permite realizar operaciones de creación, consulta, actualización y eliminación de registros.

---

## Autor

**Autor:** Ortiz "Z²"

**Institución utilizada como referencia:** Escuela Superior Politécnica de Chimborazo (ESPOCH)

**Carrera:** Ingeniería en Tecnologías de la Información

---

## Licencia

Este proyecto fue desarrollado con fines académicos
como parte de la asignatura de Fundamentos de Bases de Datos.

Se permite su utilización con fines educativos, conservando
el reconocimiento de la autoría correspondiente.