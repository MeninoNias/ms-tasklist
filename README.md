# To-Do List Microservice

Este projeto é um microserviço de gerenciamento de lista de tarefas (to-do list) desenvolvido com Python e FastAPI. Ele permite a criação, leitura, atualização e exclusão de tarefas, com suporte a persistência de dados em um banco de dados relacional, cache de resultados, testes unitários e de integração, e está configurado para containerização com Docker e orquestração com Kubernetes.

### Acessando a Aplicação

A aplicação está disponível publicamente na seguinte URL:

[http://18.212.133.34/docs](http://18.212.133.34/docs)

Você pode acessar a documentação interativa da API do To-Do List através deste link.

## Requisitos

1. **CRUD de Tarefas**
    - **POST**: Criar uma nova tarefa
    - **PUT**: Editar uma tarefa existente
    - **PATCH**: Editar parcialmente uma tarefa (e.g., marcar como concluída)
    - **GET**: Buscar uma tarefa específica
    - **DELETE**: Deletar uma tarefa

## Implantação

A aplicação foi implantada na AWS EC2 utilizando Docker Compose, Nginx e um balanceador de carga.

### Tecnologias Utilizadas

- **FastAPI**: Framework web para Python.
- **Redis**: Sistema de cache em memória.
- **Docker**: Containerização da aplicação.
- **Nginx**: Servidor web utilizado como proxy reverso.
- **AWS EC2**: Instância de computação em nuvem para hospedar a aplicação.

### Arquitetura

A arquitetura da implantação inclui:
- Um container para a aplicação FastAPI.
- Um container para o PostgreSQL.
- Um container para o Redis.
- Um container para o Nginx configurado como proxy reverso.
- Um balanceador de carga configurado na AWS para distribuir o tráfego entre as instâncias.

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
```

### Como Foi Feita a Implantação

1. **Criação da Instância EC2**: Uma instância EC2 foi criada no AWS.
2. **Configuração do Docker e Docker Compose**:
   - Instalação do Docker e Docker Compose na instância EC2.
   - Definição dos serviços no arquivo `docker-compose.yml`, incluindo FastAPI, Redis e Nginx.
3. **Configuração do Nginx**:
   - Configuração do Nginx como proxy reverso para encaminhar solicitações HTTP para a aplicação FastAPI.
   - Arquivos de configuração do Nginx foram colocados em um diretório chamado `nginx`.
4. **Configuração do Balanceador de Carga**:
   - Um balanceador de carga foi configurado no AWS para distribuir o tráfego de entrada entre as instâncias da aplicação.
5. **Deploy da Aplicação**:
   - Os serviços foram iniciados usando Docker Compose.
   - A aplicação foi verificada para garantir que todos os componentes estavam funcionando corretamente.
