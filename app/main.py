from fastapi import FastAPI

from app import models
from app.routers import users

app = FastAPI()

# Criar tabelas ao iniciar a aplicação
models.create_tables()

# Adiciona o roteador de usuários
app.include_router(users.router)
