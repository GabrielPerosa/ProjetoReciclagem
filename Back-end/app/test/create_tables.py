from sqlalchemy import create_engine, inspect
from app.config.database import Base
import sys

DATABASE_URL = "postgresql://adm:123@postgres_db:5432/meu_banco"
engine = create_engine(DATABASE_URL)

def create_tables():
    print("Verificando tabelas existentes...")

    try:
        Base.metadata.create_all(bind=engine)
        print("Tabelas criadas com sucesso (se não existiam)!")
    except Exception as e:
        print("Erro ao criar tabelas:", e)
        sys.exit(1)

if __name__ == "__main__":
    create_tables()
