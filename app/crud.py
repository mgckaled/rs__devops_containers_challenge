from app.database import get_db


def add_user(name: str, email: str):
    """Adiciona um usuário ao banco de dados"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    db.commit()
    db.close()


def get_users():
    """Retorna todos os usuários do banco"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    db.close()
    return users
