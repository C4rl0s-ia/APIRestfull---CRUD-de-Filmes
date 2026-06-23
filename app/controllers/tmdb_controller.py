from fastapi import APIRouter, Depends, HTTPException, Query
from app.services.tmdb_service import search_movies
from app.models.usuario_model import Usuario
from app.security import get_current_user

router = APIRouter(prefix="/tmdb", tags=["TMDB"])

@router.get("/search")
async def search_tmdb_movies(query: str = Query(..., min_length=2, description="Termo de busca"), current_user: Usuario = Depends(get_current_user)):
    try:
        results = await search_movies(query)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
