# To-Do List Microservice

Este projeto é um microserviço de gerenciamento de lista de tarefas (to-do list) desenvolvido com Python e FastAPI. Ele permite a criação, leitura, atualização e exclusão de tarefas, com suporte a persistência de dados em um banco de dados relacional, cache de resultados, testes unitários e de integração, e está configurado para containerização com Docker e orquestração com Kubernetes.

## Requisitos

1. **CRUD de Tarefas**
    - **POST**: Criar uma nova tarefa
    - **PUT**: Editar uma tarefa existente
    - **PATCH**: Editar parcialmente uma tarefa (e.g., marcar como concluída)
    - **GET**: Buscar uma tarefa específica
    - **DELETE**: Deletar uma tarefa

## Como Rodar o Projeto Localmente

### Pré-requisitos

- Python 3.9+
- Docker
- Docker Compose
- Kubernetes (kubectl)

### Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/MeninoNias/ms-tasklist.git
    cd ms-tasklist
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente:
    ```sh
    cp .env.example .env
    ```

### Executando a Aplicação

1. Inicie o banco de dados PostgreSQL e Redis usando Docker Compose:
    ```sh
    docker-compose up -d
    ```

2. Execute a aplicação:
    ```sh
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

### Executando os Testes

Para rodar os testes unitários e de integração, use o pytest:
```sh
pytest

