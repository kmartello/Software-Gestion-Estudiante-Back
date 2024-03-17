from cmath import log
from sdk import executeQuery, executeOneQuery, executeNonQuery
from model import Asignatura

def selectAsignaturas():
    query = """
        select
            a.*,
            p.id || ' - ' || p.nombre || ' ' || p.apellido as profesor
        from
            asignaturas a
        inner join profesores p on
            a.id_profesor = p.id
        where
            a.estado = true
    """
    return executeQuery(query)


def selectAsignatura(id):
    query = """
        select
            a.*,
            p.id || ' - ' || p.nombre || ' ' || p.apellido as profesor
        from
            asignaturas a
        inner join profesores p on
            a.id_profesor = p.id
        where
            a.id = %s and a.estado = true
    """
    return executeOneQuery(query, (id,))

def insertAsignatura(asignatura: Asignatura):
    print(asignatura)
    query = """
        insert into asignaturas (nombre, salon, horario, id_profesor)
        values (%s, %s, %s, %s)
    """
    return executeNonQuery(query, (asignatura.nombre, asignatura.salon, asignatura.horario, asignatura.id_profesor))

def updateAsignatura(id: int, asignatura: Asignatura):
    query = """
        update asignaturas
        set
            nombre = %s,
            salon = %s,
            horario = %s,
            id_profesor = %s
        where
            id = %s
    """
    return executeNonQuery(query, (asignatura.nombre, asignatura.salon, asignatura.horario, asignatura.id_profesor, id))

def deleteAsignatura(id):
    query = """
        update asignaturas
        set
            estado = false
        where
            id = %s
    """
    return executeNonQuery(query, (id,))