from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import estudiantes, profesores, asignaturas, clases

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(estudiantes.router)
app.include_router(profesores.router)
app.include_router(asignaturas.router)
app.include_router(clases.router)