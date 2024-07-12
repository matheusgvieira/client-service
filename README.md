# Clientes App

## Setup

### 1. Clone o repositório

```sh
git clone https://github.com/matheusgvieira/client-service.git
cd client-service
```

## 2. Construa e execute os contêineres Docker

```sh
docker-compose up --build
```

## 3. Acesse os serviços

• Flask: http://localhost:5000
• FastAPI: http://localhost:8000

## Endpoints

### Flask

    •	POST /clientes: Cadastra um cliente
    •	GET /clientes: Lista todos os clientes

### FastAPI

    •	POST /generate_jwt/: Gera um JWT para um cliente

## Estrutura do Projeto

```
clientes-app/
├── clientes/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   ├── database.py
│   └── config.py
├── jwt_service/
│   ├── __init__.py
│   ├── main.py
│   └── jwt_generator.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Descrição dos Arquivos

    •	clientes/config.py: Configuração do Flask.
    •	clientes/database.py: Configuração do SQLAlchemy.
    •	clientes/models.py: Definição do modelo Cliente.
    •	clientes/app.py: Aplicação Flask com as rotas para cadastro e listagem de clientes.
    •	jwt_service/jwt_generator.py: Função para gerar JWT.
    •	jwt_service/main.py: Aplicação FastAPI com o endpoint para gerar JWT.
    •	Dockerfile: Dockerfile para criar a imagem da aplicação.
    •	docker-compose.yml: Arquivo para orquestração dos contêineres.
    •	requirements.txt: Lista de dependências do projeto.
    •	README.md: Instruções para configuração e execução do projeto.

## Inicialização do Banco de Dados

Após iniciar o contêiner do Flask, inicialize o banco de dados executando:

```sh
docker-compose exec flask-app flask shell
```

No shell do Flask, execute:

```sh
from clientes.database import db
db.create_all()
```
