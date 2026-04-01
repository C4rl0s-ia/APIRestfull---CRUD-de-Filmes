from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.filme_schema import FilmeCreate
from app.services import filme_service
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/filmes")
def criar_filme(filme: FilmeCreate, db: Session = Depends(get_db)):
    return filme_service.criar(db, filme)

@router.get("/filmes")
def listar_filmes(db: Session = Depends(get_db)):
    return filme_service.listar(db)

@router.delete("/filmes/{filme_id}")
def deletar_filme(filme_id: int, db: Session = Depends(get_db)):
    filme = filme_service.deletar(db, filme_id)
    
    if not filme:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    return filme

"""Tratativa de erro adicionada - valida se o filme existe antes de seguir com o update"""
@router.put("/filmes/{filme_id}")
def atualizar_filme(filme_id: int, filme: FilmeCreate, db: Session = Depends(get_db)):
    filme = filme_service.atualizar(db, filme_id, filme)
    
    if not filme: 
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    
    return filme