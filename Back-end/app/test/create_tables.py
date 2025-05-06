from sqlalchemy import create_engine, inspect
from app.config.database import Base
import sys
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

def table_exists(table_name):
    """Verifica se uma tabela já existe no banco de dados"""
    inspector = inspect(engine)
    return inspector.has_table(table_name)

def list_tables():
    """Lista todas as tabelas existentes no banco de dados."""
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    if tables:
        print("Tabelas existentes no banco de dados:")
        for table in tables:
            print(f"- {table}")
    else:
        print("Nenhuma tabela encontrada no banco de dados.")

def create_tables():
    print("Verificando tabelas existentes...")
    
    # Lista de todas as tabelas definidas nos modelos
    all_tables = Base.metadata.tables.keys()
    
    # Filtra apenas tabelas que não existem
    tables_to_create = [name for name in all_tables if not table_exists(name)]
    
    if not tables_to_create:
        print("Todas as tabelas já existem no banco de dados.")
        return
    
    print(f"Criando {len(tables_to_create)} tabelas: {', '.join(tables_to_create)}")
    
    # Cria apenas as tabelas que não existem
    for table_name in tables_to_create:
        table = Base.metadata.tables[table_name]
        table.create(bind=engine)
        print(f"Tabela {table_name} criada com sucesso!")
    
    print("Operação concluída!")
    
if __name__ == "__main__":
    list_tables()
    create_tables()
