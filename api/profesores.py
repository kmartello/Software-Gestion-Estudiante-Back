from controller.profesores import *
from fastapi import APIRouter
from model import Profesor

router = APIRouter()

@router.get("/api/v1/profesores", tags=["Profesores"])
async def selectAll():
    return selectProfesores()

@router.get("/api/v1/profesores/{id}", tags=["Profesores"])
async def select(id: int):
    return selectProfesor(id)

@router.post("/api/v1/profesores", tags=["Profesores"])
async def insert(profesor: Profesor):
    return insertProfesor(profesor)

@router.put("/api/v1/profesores/{id}", tags=["Profesores"])
async def update(profesor: Profesor, id: int):
    return updateProfesor(id, profesor)

@router.delete("/api/v1/profesores/{id}", tags=["Profesores"])
async def delete(id: int):
    return deleteProfesor(id)