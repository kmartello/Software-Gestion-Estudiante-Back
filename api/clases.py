from controller.clases import *
from fastapi import APIRouter
from model import Clase

router = APIRouter()

@router.get("/api/v1/clases", tags=["Clases"])
async def selectAll():
    return selectClases()

@router.get("/api/v1/clases/{id}", tags=["Clases"])
async def select(id: int):
    return selectClase(id)

@router.post("/api/v1/clases", tags=["Clases"])
async def insert(clase: Clase):
    return insertClase(clase)

@router.put("/api/v1/clases/{id}", tags=["Clases"])
async def update(clase: Clase, id: int):
    return updateClase(id, clase)

@router.delete("/api/v1/clases/{id}", tags=["Clases"])
async def delete(id: int):
    return deleteClase(id)