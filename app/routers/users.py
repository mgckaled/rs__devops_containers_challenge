from fastapi import APIRouter, HTTPException, Request

from app import crud

router = APIRouter()


@router.post("/users/")
async def create_user(request: Request):
    """Cria um usuário no banco de dados sem usar Pydantic"""
    user_data = await request.json()
    name = user_data.get("name")
    email = user_data.get("email")

    if not name or not email:
        raise HTTPException(
            status_code=400, detail="Nome e e-mail são obrigatórios")

    try:
        crud.add_user(name, email)
        return {"message": "Usuário criado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/")
def read_users():
    """Retorna todos os usuários"""
    users = crud.get_users()
    return {"users": [dict(user) for user in users]}
