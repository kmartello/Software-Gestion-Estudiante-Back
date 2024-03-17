from sdk import executeQuery, executeOneQuery, executeNonQuery
from model import Clase

def selectClases():
    query = "select c.*, e.id || ' - ' || e.nombre || ' ' || e.apellido as  estudiante, a.id || ' - ' || a.nombre as asignatura from clases c inner join estudiantes e on c.id_estudiante = e.id inner join asignaturas a on c.id_asignatura = a.id where c.estado = true"
    return executeQuery(query)

def selectClase(id):
    query = "select c.*, e.id || ' - ' || e.nombre || ' ' || e.apellido as  estudiante, a.id || ' - ' || a.nombre as asignatura from clases c inner join estudiantes e on c.id_estudiante = e.id inner join asignaturas a on c.id_asignatura = a.id where c.id = %s and c.estado = true"
    return executeOneQuery(query, (id,))

def insertClase(clase: Clase):
    query = "INSERT INTO clases (id_estudiante, id_asignatura) VALUES (%s, %s)"
    return executeNonQuery(query, (clase.id_estudiante, clase.id_asignatura))

def updateClase(id, clase: Clase):
    query = "UPDATE clases SET id_estudiante = %s, id_asignatura = %s WHERE id = %s"
    return executeNonQuery(query, (clase.id_estudiante, clase.id_asignatura, id))

def deleteClase(id):
    query = "UPDATE clases SET estado = false WHERE id = %s"
    return executeNonQuery(query, (id,))