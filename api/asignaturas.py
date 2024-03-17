from controller.asignaturas import *
from fastapi import APIRouter
from model import Asignatura

router = APIRouter()

# ASIGNATURAS

@router.get("/api/v1/asignaturas", tags=["Asignaturas"])
async def selectAll():
    return selectAsignaturas()


@router.get("/api/v1/asignaturas/{id}", tags=["Asignaturas"])
async def select(id: int):
    return selectAsignatura(id)

@router.post("/api/v1/asignaturas", tags=["Asignaturas"])
async def insert(asignatura: Asignatura):
    return insertAsignatura(asignatura)

@router.put("/api/v1/asignaturas/{id}", tags=["Asignaturas"])
async def update(asignatura: Asignatura, id: int):
    return updateAsignatura(id, asignatura)

@router.delete("/api/v1/asignaturas/{id}", tags=["Asignaturas"])
async def delete(id: int):
    return deleteAsignatura(id)