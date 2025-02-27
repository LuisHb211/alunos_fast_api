from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from schemas.alunos import Aluno

router = APIRouter()

list_alunos = {}

#Read
@router.get("/alunos")
async def read_alunos():
  return list_alunos

#Create
@router.post("/alunos")
async def create_aluno(aluno: Aluno):
  aluno_id = str(len(list_alunos) + 1)
  list_alunos[aluno_id] = jsonable_encoder(aluno)
  return list_alunos[aluno_id]

#Read Specifc
@router.get("/alunos/{aluno_id}")
async def read_specific_aluno(aluno_id: str):
  if aluno_id not in list_alunos:
    raise HTTPException(status_code=404, detail="Aluno not found")
  return list_alunos[aluno_id]

#Update
@router.put("/alunos/{aluno_id}")
async def update_aluno(aluno_id: str, aluno: Aluno):
  if aluno_id not in list_alunos:
    raise HTTPException(status_code=404, detail="Aluno not found")
  infos_update = jsonable_encoder(aluno)
  list_alunos[aluno_id] = infos_update
  return infos_update

#Delete
@router.delete("/alunos/{aluno_id}")
async def delete_aluno(aluno_id: str):
  if aluno_id not in list_alunos:
    raise HTTPException(status_code=404, detail="Aluno not found")
  del list_alunos[aluno_id]
  return {"detail": "Aluno deleted"}