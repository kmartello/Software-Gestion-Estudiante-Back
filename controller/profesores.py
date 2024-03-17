from sdk import executeQuery, executeOneQuery, executeNonQuery
from model import Profesor

def selectProfesores():
    query = "SELECT * FROM profesores where estado = true"
    return executeQuery(query)

def selectProfesor(id):
    query = "SELECT * FROM profesores where id = %s and estado = true"
    return executeOneQuery(query, (id,))

def insertProfesor(profesor: Profesor):
    query = "INSERT INTO profesores (nombre, apellido, identificacion, correo, especialidad) VALUES (%s, %s, %s, %s, %s)"
    return executeNonQuery(query, (profesor))

def updateProfesor(id, profesor: Profesor):
    query = "UPDATE profesores SET nombre = %s, apellido = %s, identificacion = %s, correo = %s, especialidad = %s WHERE id = %s"
    return executeNonQuery(query, (profesor.nombre, profesor.apellido, profesor.identificacion, profesor.correo, profesor.especialidad, id))

def deleteProfesor(id):
    query = "UPDATE profesores SET estado = false WHERE id = %s"
    return executeNonQuery(query, (id,))