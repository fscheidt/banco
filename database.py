import os
import dotenv
from pymongo.mongo_client import MongoClient
from pathlib import Path
import argparse

project_path = Path(__file__).resolve().parent
env_file = project_path / ".env"

dotenv.load_dotenv(env_file)
URL = os.environ["db_url"]

def get_connection(db_name: str) -> MongoClient:
    """ 
    Obtem a conexao com mongodb atlas
        @param db_name: nome da base de dados
    """
    client = MongoClient(URL)
    db = client[db_name]
    return db

# informações sobre as collections no banco de dados
def show_info(db: MongoClient):
    if db is not None:
        print(f"database: {db.name}")
        print([f"{c} => {db[c].count_documents({})}" for c in db.list_collection_names()])
    else:
        print("Erro: sem conexão com o banco de dados")

if __name__ == "__main__":
    """
    informações sobre a base de dados
        python database.py geobr
        python database.py booksdb
    """
    parser = argparse.ArgumentParser("database")
    parser.add_argument("dbname", help="nome do banco de dados", type=str)
    args = parser.parse_args()
    db = get_connection(args.dbname)
    show_info(db)
