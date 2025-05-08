from sqlalchemy import create_engine, inspect
from app.config.database import Base
from dotenv import load_dotenv
import app.models  # Pacote onde estão os arquivos de modelo
import importlib
import logging
import pkgutil
import os

# Carrega variáveis de ambiente do .env
load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# Importa automaticamente todos os módulos da pasta app/models
for _, module_name, _ in pkgutil.iter_modules(app.models.__path__):
    importlib.import_module(f"app.models.{module_name}")

def table_exists(table_name):
    """Verifica se uma tabela já existe no banco de dados"""
    inspector = inspect(engine)
    return inspector.has_table(table_name)

def create_tables():
    logging.info("Verificando tabelas existentes...")

    all_tables = Base.metadata.tables.keys()
    existing_tables = [name for name in all_tables if table_exists(name)]
    tables_to_create = [name for name in all_tables if name not in existing_tables]

    if existing_tables:
        logging.info(f"Tabelas que já existem no banco de dados: {', '.join(existing_tables)}")
    else:
        logging.info("Nenhuma tabela existente foi encontrada no banco de dados.")
    
    if not tables_to_create:
        logging.info("Todas as tabelas já existem no banco de dados.")
        return

    logging.info(f"Criando {len(tables_to_create)} tabelas: {', '.join(tables_to_create)}")
    
    for table_name in tables_to_create:
        table = Base.metadata.tables[table_name]
        table.create(bind=engine)
        logging.info(f"Tabela {table_name} criada com sucesso!")
    
    logging.info("Operação concluída!")

if __name__ == "__main__":
    create_tables()