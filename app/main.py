from fastapi import FastAPI

from app.database import init_db

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Olá Mundo"}


@app.get("/ping")
def ping():
    return {"message": "pong"}

# Inicializa o banco de dados ao iniciar a aplicação


@app.on_event("startup")
async def startup_event():
    await init_db()
