import sqlite3

DATABASE_URL = "database.db"


def get_db():
    """Retorna uma conexão com o banco SQLite"""
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn
