from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.encoders import jsonable_encoder
from schemas.alunos import Aluno as AlunoSchema

from models.alunos import Aluno
from sqlalchemy.orm import Session
from models.dataBase import get_db

router = APIRouter()

list_alunos = {
    "1": {
        "nome": "Luis Henrique",
        "idade": 21,
        "email": "luis@gmail.com",
        "curso": "Engenharia dnetstat -tulnp | grep 5432a Computação",
        "periodo": 6,
        "cidade": "Uberlândia",
        "estado": "MG",
        "pais": "Brasil"
    },
    "2": {
        "nome": "Fernando",
        "idade": 20,
        "curso": "Engenharia da Computação"
    }
}

# Read
@router.get("/alunos")
async def root_alunos():
    return list_alunos

@router.post("/alunos")
def create_aluno(aluno: AlunoSchema, db: Session = Depends(get_db)):
    new_aluno = Aluno(**aluno.model_dump())
    db.add(new_aluno)
    db.commit()
    db.refresh(new_aluno)
    return new_aluno

@router.put("/alunos/{id}")
def update(id: int, aluno:AlunoSchema, db:Session = Depends(get_db)):
    aluno_retorno_post = db.query(Aluno).filter(Aluno.id == id)
    aluno_retorno_post.first()

    if aluno_retorno_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Aluno: {id} does not exist')
    else:
        print(aluno.model_dump())
        aluno_retorno_post.update(aluno.model_dump(), synchronize_session=False)
        db.commit()
    return aluno_retorno_post.first()

@router.delete("/alunos/{id}")
def delete(id:int ,db: Session = Depends(get_db)):
    aluno_retorno_delete = db.query(Aluno).filter(Aluno.id == id)
    
    if aluno_retorno_delete.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Aluno não existe")
    else:
        aluno_retorno_delete.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



# Create
# @router.post("/alunos")
# async def create_aluno(aluno: Aluno):
#     aluno_id = str(len(list_alunos) + 1)
#     list_alunos[aluno_id] = jsonable_encoder(aluno)
#     return list_alunos[aluno_id]

# Read Specific
# @router.get("/alunos/{aluno_id}")
# async def read_specific_aluno(aluno_id: str):
#     if aluno_id not in list_alunos:
#         raise HTTPException(status_code=404, detail="Aluno not found")
#     return list_alunos[aluno_id]

# # Update
# @router.put("/alunos/{aluno_id}")
# async def update_aluno(aluno_id: str, aluno: Aluno):
#     if (aluno_id not in list_alunos):
#         raise HTTPException(status_code=404, detail="Aluno not found")
#     infos_update = jsonable_encoder(aluno)
#     list_alunos[aluno_id] = infos_update
#     return infos_update

# # Delete
# @router.delete("/alunos/{aluno_id}")
# async def delete_aluno(aluno_id: str):
#     if aluno_id not in list_alunos:
#         raise HTTPException(status_code=404, detail="Aluno not found")
#     del list_alunos[aluno_id]
#     return {"detail": "Aluno deleted"}