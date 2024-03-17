from sdk import executeQuery, executeOneQuery, executeNonQuery
from model import Estudiante

def selectEstudiantes():
    query = "SELECT * FROM estudiantes where estado = true"
    return executeQuery(query)

def selectEstudiante(id):
    query = "SELECT * FROM estudiantes where id = %s and estado = true"
    return executeOneQuery(query, (id,))

def insertEstudiante(estudiante: Estudiante):
    query = "INSERT INTO estudiantes (nombre, apellido, identificacion, correo, programa) VALUES (%s, %s, %s, %s, %s)"
    return executeNonQuery(query, (estudiante.nombre, estudiante.apellido, estudiante.identificacion, estudiante.correo, estudiante.programa))

def updateEstudiante(id, estudiante: Estudiante):
    query = "UPDATE estudiantes SET nombre = %s, apellido = %s, identificacion = %s, correo = %s, programa = %s WHERE id = %s"
    return executeNonQuery(query, (estudiante.nombre, estudiante.apellido, estudiante.identificacion, estudiante.correo, estudiante.programa, id))

def deleteEstudiante(id):
    query = "UPDATE estudiantes SET estado = false WHERE id = %s"
    return executeNonQuery(query, (id,))