from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Filme(Base):
    __tablename__ = "filmes"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    genero = Column(String)
    ano = Column(Integer)
    nota = Column(Integer)