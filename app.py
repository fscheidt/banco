import os
from pprint import pprint
import dotenv
from pymongo.mongo_client import MongoClient

env_file = ".env"
db_name = "geobr"
dotenv.load_dotenv(env_file)
URL = os.environ["db_url"]

def get_connection(database: str):
  """ obtem a conexao com o banco de dados """
  client = MongoClient(URL)
  db = client[database]
  return db

def get_municipios_estado(db, _uf: str) -> list:
    res = db.municipios.find(
        { 'Uf': _uf}, { '_id': 0, 'Nome': 1 }
    )
    return list(res)

if __name__ == "__main__":
    db = get_connection(db_name)
    print(db.list_collection_names()) # base geobr

    result = get_municipios_estado(db, "AC")
    print(f'total = {len(result)}')
    pprint(result) #  22
