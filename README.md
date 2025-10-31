# UserManagerAPI

> Projeto de aprendizado de FastAPI e Python 3.12+, focado em construção de API para gerenciamento de usuários.

Este projeto foi desenvolvido com objetivo **educacional**, para consolidar conhecimentos de **Python moderno**, **FastAPI**, **Pydantic** e arquitetura básica de APIs REST. Ele implementa funcionalidades básicas de CRUD (Create, Read) e está organizado seguindo boas práticas de modularização em camadas (routers, schemas, models).

---

## 🚀 Tecnologias Utilizadas

- **Python 3.12+** – Linguagem de programação principal.
- **FastAPI** – Framework web moderno e de alta performance para APIs.
- **Uvicorn** – Servidor ASGI para rodar o FastAPI.
- **Pydantic** – Validação e modelagem de dados com BaseModel.
- **SQLAlchemy (planejado)** – ORM para integração com banco de dados relacional (PostgreSQL).
- **PostgreSQL (planejado)** – Banco de dados relacional.

> ⚠️ Observação: Atualmente, o projeto simula a persistência de dados sem banco real, usando dicionários mock.

---

## 📁 Estrutura do Projeto

user-manager-api/
├── .venv/ # Ambiente virtual
├── main.py # Ponto de entrada da API
├── app/
│ ├── routers/
│ │ └── user_router.py # Endpoints relacionados a usuários
│ └── schemas/
│ └── user.py # Modelos de validação (Pydantic)


---

## ⚡ Funcionalidades Implementadas

- **Rota Raiz:**
  ```http
  GET /

Retorna uma mensagem de boas-vindas.

    Criação de Usuário (simulada):

POST /users/

    Request Body:

{
  "name": "Nome do Usuário",
  "email": "usuario@email.com",
  "password": "senha1234"
}

Response Body:

    {
      "id": 1,
      "name": "Nome do Usuário",
      "email": "usuario@email.com"
    }

Consulta de Usuário (simulada):

    GET /users/{user_id}

        Retorna o ID do usuário solicitado e uma mensagem.

🏗️ Como Rodar o Projeto

    Clone o repositório:

git clone <URL_DO_REPOSITORIO>
cd user-manager-api

Crie e ative o ambiente virtual:

python3.12 -m venv .venv
source .venv/bin/activate

Instale as dependências:

pip install "fastapi[standard]"

Execute a aplicação:

fastapi dev main.py

Acesse a documentação interativa:

    Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc
📝 Observações

    Este projeto é educacional, e simula a persistência de dados sem banco real.

    A próxima etapa planejada é integrar SQLAlchemy com PostgreSQL, para CRUD completo com banco real.

    Código estruturado em routers, schemas e futuramente models, seguindo boas práticas de desenvolvimento moderno.

📖 Referências e Aprendizado

    Documentação oficial FastAPI

Pydantic

SQLAlchemy ORM
