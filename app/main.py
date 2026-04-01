from fastapi import FastAPI
from app.database.connection import engine, Base
from app.controllers import filme_controller

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(filme_controller.router)

@app.get("/")
def home():
    return {"mensagem": "API funcionando!"}