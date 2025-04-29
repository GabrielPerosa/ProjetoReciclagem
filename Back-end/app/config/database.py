from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os # Importando o dotenv para carregar variáveis de ambiente

# Configurações do banco de dados
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")  
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")  

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