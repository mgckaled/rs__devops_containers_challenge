# Container Challenge

Este projeto consiste em uma API FastAPI encapsulada em um container Docker, utilizando SQLite como banco de dados e gerenciando dependências com Pipenv.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11.9**
- **FastAPI**
- **SQLite**
- **Uvicorn**
- **Docker & Docker Compose**
- **Pipenv** (Gerenciamento de dependências)
- **Pytest** (Testes automatizados)

---

## 📦 Estrutura do Projeto

```plaintext
/meu_projeto
│── Pipfile
│── Pipfile.lock
│── Dockerfile
│── docker-compose.yml
│── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│   ├── schemas.py
│   ├── routers/
│   │   ├── users.py
│   │   ├── __init__.py
│   ├── __init__.py
│── .env
│── README.md
│── tests/
│   ├── test_main.py
│   ├── __init__.py
│── database.db 
```

---

## 🛠️ Configuração e Execução

### 1️⃣ Clonar o repositório

```sh
git clone https://github.com/seu-usuario/container_challenge.git
cd container_challenge
```

### 2️⃣ Configurar o ambiente

Instale as dependências usando Pipenv:

```sh
pipenv install
```

### 3️⃣ Rodar os testes

```sh
pipenv run pytest
```

### 4️⃣ Construir e subir os containers

```sh
docker-compose up --build
```

A API estará disponível em `http://localhost:8000`.

---

## 🧪 Testando a API

Acesse a documentação interativa do FastAPI:

```powershell
http://localhost:8000/docs
```

Ou utilize a interface alternativa:

```powersell
http://localhost:8000/redoc
```
