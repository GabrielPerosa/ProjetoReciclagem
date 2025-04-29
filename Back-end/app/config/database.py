from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configurações do banco de dados
DB_USER = "postgres"
DB_PASSWORD = "minha_senha"
DB_HOST = "localhost"  # continua localhost porque o container mapeia para sua máquina
DB_PORT = "5433"
DB_NAME = "meu_banco"

# URL de conexão
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criação da engine e da sessão
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Função para fornecer a sessão do banco via Depends
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()