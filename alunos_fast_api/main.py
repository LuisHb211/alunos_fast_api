from fastapi import FastAPI
from typing import Optional
from routers.alunos import router as router_alunos
from routers.cursos import router as router_cursos
from models.dataBase import Base, engine

app = FastAPI()
app.include_router(router_alunos)
app.include_router(router_cursos)
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
  api_overview = {
    'Read':"localhost:8000/alunos",
    'Create':"localhost:8000/alunos",
    'Read_specific':"localhost:8000/alunos/{aluno_id}",
    'Update':"localhost:8000/alunos/{aluno_id}",
    'Delete':"localhost:8000/alunos/{aluno_id}",
  }
  return api_overview

