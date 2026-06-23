from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.filme_schema import FilmeCreate
from app.services import filme_service
from app.models.usuario_model import Usuario
from app.security import get_current_user

router = APIRouter()



@router.post("/filmes")
def criar_filme(filme: FilmeCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    filme.usuario = current_user.username
    return filme_service.criar(db, filme)

@router.get("/filmes")
def listar_filmes(db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return filme_service.listar(db, current_user.username)

@router.get("/filmes/{filme_id}")
def obter_filme(filme_id: int, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    filme = filme_service.obter(db, filme_id)
    
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    if filme.usuario != current_user.username:
        raise HTTPException(status_code=403, detail="Acesso não permitido")
    
    return filme

@router.delete("/filmes/{filme_id}")
def deletar_filme(filme_id: int, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    filme = filme_service.deletar(db, filme_id)
    
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    if filme.usuario != current_user.username:
        raise HTTPException(status_code=403, detail="Acesso não permitido")
    
    return filme

@router.put("/filmes/{filme_id}")
def atualizar_filme(filme_id: int, filme_update: FilmeCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    filme_existente = filme_service.obter(db, filme_id)

    if not filme_existente:
        raise HTTPException(status_code=404, detail="Filme não encontrado")

    if filme_existente.usuario != current_user.username:
        raise HTTPException(status_code=403, detail="Acesso não permitido")

    filme_update.usuario = current_user.username
    filme_atualizado = filme_service.atualizar(db, filme_id, filme_update)

    return filme_atualizado