# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a construir APIs REST modernas em Python usando o framework FastAPI, praticando a criação de endpoints, validação de dados com Pydantic e as operações CRUD (criar, ler, atualizar e excluir) sobre uma coleção de recursos.

## 📝 Tarefas

### 🛠️ Criar seus Primeiros Endpoints GET

#### Descrição
Use o starter code fornecido para colocar sua primeira API no ar! Complete os endpoints GET para listar todos os livros da biblioteca e buscar um livro específico pelo seu `id`.

#### Requisitos
O programa concluído deve:

- Responder em `GET /books` com a lista completa de livros em formato JSON
- Responder em `GET /books/{book_id}` com o livro correspondente ao `id` informado
- Retornar o status HTTP `404` com uma mensagem clara quando o livro não existir
- Exemplo de uso:

  ```text
  GET /books/1
  {"id": 1, "title": "O Pequeno Príncipe", "author": "Antoine de Saint-Exupéry", "year": 1943}
  ```

### 🛠️ Validar Dados com Modelos Pydantic

#### Descrição
Defina um modelo Pydantic chamado `Book` para representar um livro e use-o para criar o endpoint `POST /books`, garantindo que apenas dados válidos sejam aceitos pela API.

#### Requisitos
O programa concluído deve:

- Definir um modelo `Book` com os campos `title` (str), `author` (str) e `year` (int)
- Aceitar requisições `POST /books` com um corpo JSON validado pelo modelo `Book`
- Gerar automaticamente um `id` único para cada novo livro criado
- Retornar o livro criado com o status HTTP `201`
- Rejeitar automaticamente requisições com campos ausentes ou de tipo incorreto (o FastAPI responde com `422`)

### 🛠️ Completar o CRUD com Atualização e Exclusão

#### Descrição
Finalize sua API implementando os endpoints de atualização e exclusão de livros, completando as quatro operações CRUD e tornando sua API pronta para uso real.

#### Requisitos
O programa concluído deve:

- Responder em `PUT /books/{book_id}` atualizando os dados do livro com o corpo JSON recebido
- Responder em `DELETE /books/{book_id}` removendo o livro da coleção e retornando o status HTTP `204`
- Retornar o status HTTP `404` quando o `id` informado não existir, em ambos os endpoints
- Permitir testar todas as operações pela documentação interativa gerada automaticamente em `/docs`
