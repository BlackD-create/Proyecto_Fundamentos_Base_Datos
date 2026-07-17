import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE

def obtener_conexion():
    conexion = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    return conexion

