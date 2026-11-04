"""
Building REST APIs com FastAPI — Starter Code

Para executar a API:
    1. Instale as dependências:  pip install fastapi uvicorn
    2. Inicie o servidor:        uvicorn starter-code:app --reload
    3. Acesse a documentação interativa em http://127.0.0.1:8000/docs

Complete os TODOs abaixo seguindo as tarefas do README.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Biblioteca API", description="API REST para gerenciar livros")

# "Banco de dados" em memória para os livros
books = [
    {"id": 1, "title": "O Pequeno Príncipe", "author": "Antoine de Saint-Exupéry", "year": 1943},
    {"id": 2, "title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899},
]


# --- Tarefa 2: Validar Dados com Modelos Pydantic ---
# TODO: Defina o modelo Book com os campos title (str), author (str) e year (int)
# class Book(BaseModel):
#     ...


# --- Tarefa 1: Criar seus Primeiros Endpoints GET ---

@app.get("/books")
def list_books():
    """Retorna a lista completa de livros."""
    # TODO: Retorne a lista de livros
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Retorna um livro pelo seu id."""
    # TODO: Encontre e retorne o livro com o id informado
    # Dica: use raise HTTPException(status_code=404, detail="...") se não existir
    pass


# --- Tarefa 2: Validar Dados com Modelos Pydantic ---

# TODO: Implemente POST /books recebendo um Book no corpo da requisição
# Dica: use @app.post("/books", status_code=201) e gere um id único


# --- Tarefa 3: Completar o CRUD com Atualização e Exclusão ---

# TODO: Implemente PUT /books/{book_id} para atualizar um livro existente

# TODO: Implemente DELETE /books/{book_id} retornando status 204
# Dica: use @app.delete("/books/{book_id}", status_code=204)
