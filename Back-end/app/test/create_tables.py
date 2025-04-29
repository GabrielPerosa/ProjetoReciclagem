from sqlalchemy import create_engine, inspect
from app.config.database import Base
from app.models.sensor import SensorDB
from app.models.cycle import CycleDB
from app.models.part import PartDB

DATABASE_URL = "postgresql://postgres:minha_senha@localhost:5433/meu_banco"
engine = create_engine(DATABASE_URL)

def table_exists(table_name):
    """Verifica se uma tabela já existe no banco de dados"""
    inspector = inspect(engine)
    return inspector.has_table(table_name)

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
    create_tables()