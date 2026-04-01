from pydantic import BaseModel, Field

class FilmeCreate(BaseModel):
    titulo: str
    genero: str
    ano: int
    nota: int = Field(ge=0, le=10)