from controller.estudiantes import *
from fastapi import APIRouter
from model import Estudiante

router = APIRouter()

@router.get("/api/v1/estudiantes", tags=["Estudiantes"])
async def selectAll():
    return selectEstudiantes()

@router.get("/api/v1/estudiantes/{id}", tags=["Estudiantes"])
async def select(id: int):
    return selectEstudiante(id)

@router.post("/api/v1/estudiantes", tags=["Estudiantes"])
async def insert(estudiante: Estudiante):
    return insertEstudiante(estudiante)

@router.put("/api/v1/estudiantes/{id}", tags=["Estudiantes"])
async def update(estudiante: Estudiante, id: int):
    return updateEstudiante(id, estudiante)

@router.delete("/api/v1/estudiantes/{id}", tags=["Estudiantes"])
async def delete(id: int):
    return deleteEstudiante(id)