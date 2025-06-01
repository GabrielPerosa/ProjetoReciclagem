## 1. Visão Geral do Backend

Este serviço backend é responsável por:

- Receber dados do CLP via **OPC-UA**  
- Persistir esses dados em um banco PostgreSQL hospedado na AWS  
- Fornecer dados para o chatbot, frontend web e aplicativo mobile  

O propósito principal é atuar como camada de integração entre dispositivos industriais (CLP) e as camadas de apresentação (chatbot, front-end e mobile).

## 2. Tecnologias Utilizadas

- **Linguagem:** Python  
- **Framework:** FastAPI  
- **Banco de Dados:** PostgreSQL (RDS na AWS)  
- **ORM:** SQLAlchemy  
- **Validação de dados:** Pydantic  
- **Servidor ASGI:** Uvicorn  
- **Conteinerização:** Docker + Docker Compose  
- **Variáveis de ambiente:** python-dotenv (`.env`)

## 3. Arquitetura e Endpoints

### 3.1 Tipo de API

- API REST rodando sobre ASGI com Uvicorn.

### 3.2 Principais Endpoints

#### Stations (estações/CLPs)
- **GET** `/stations/` – Lista todas as estações.  
- **POST** `/stations/` – Cria ou registra nova estação.

#### Station States (estado das estações)
- **GET** `/station-states/` – Lista estados (ligada/desligada).  
- **POST** `/station-states/` – Registra novo estado de estação.

#### Devices (dispositivos conectados ao CLP)
- **GET** `/devices/` – Lista dispositivos.  
- **POST** `/devices/` – Registra novo dispositivo.

#### Device States (estado dos dispositivos)
- **GET** `/device-states/` – Lista estados de dispositivos.  
- **POST** `/device-states/` – Registra novo estado de dispositivo.

#### Parts (peças produzidas)
- **GET** `/parts/` – Lista todas as peças.  
- **POST** `/parts/` – Registra nova peça.  
- **GET** `/parts/quantity/{type}` – Quantidade de peças por tipo.

#### Production Parts (produção de peças)
- **POST** `/production-parts/` – Envia dados de produção.  
- **GET** `/production-parts/by-type/{part_type}` – Produção por tipo de peça.  
- **GET** `/production-parts/get_utilization` – Estatísticas de aproveitamento.  
- **GET** `/production-parts/parts/{part_type}/total` – Total produzido por tipo.  
- **GET** `/production-parts/summary` – Resumo para uso do chatbot.

#### Users (usuários do sistema)
- **GET** `/users/` – Lista usuários.  
- **POST** `/users/` – Cria novo usuário.  
- **PUT** `/users/password/{user_id}` – Atualiza senha de usuário.

### 3.3 Comunicação com Banco de Dados

No diretório `app/config`, há um módulo para carregar variáveis de ambiente e configurar a conexão SQLAlchemy:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 3.4 Integração com Outros Serviços
- CLP: comunicação via OPC-UA

- Chatbot: chamadas HTTP para /production-parts/summary com JSON

- Frontend & Mobile: consumo dos endpoints REST para mostrar dados

## 4. Estrutura de Pastas

```python
Back-end/
├── app
│   ├── auth         # Autenticação (JWT/OAuth2)
│   ├── config       # Configuração de ambiente e DB
│   ├── db           # Migrations e inicialização (Alembic)
│   ├── models       # Definições de tabelas SQLAlchemy
│   ├── repository   # Funções CRUD usando get_db()
│   ├── routes       # Definição de rotas FastAPI organizadas por recurso
│   ├── schemas      # DTOs Pydantic para validação de entrada/saída
│   │   └── dto
│   └── __init__.py  # Inicialização da aplicação
├── postgres_data    # Volume Docker (persistência para dev local)
├── Dockerfile       # Imagem do backend
├── docker-compose.yml # Orquestra containers backend + postgres
└── .env             # Variáveis de ambiente para dev local
```
## 5. Como Executar Localmente

- Crie um arquivo .env na raiz com as variáveis listadas na seção 6.

- Execute: docker-compose up --build


A API ficará disponível em http://localhost:8000.

