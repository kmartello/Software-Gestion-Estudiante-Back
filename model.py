from pydantic import BaseModel


class Estudiante(BaseModel):
    nombre: str
    apellido: str
    identificacion: str
    correo: str
    programa: str


class Profesor(BaseModel):
    nombre: str
    apellido: str
    identificacion: str
    correo: str
    especialidad: str


class Asignatura(BaseModel):
    nombre: str
    salon: int
    horario: str
    id_profesor: int


class Clase(BaseModel):
    id_asignatura: int
    id_estudiante: int
