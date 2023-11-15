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

db = get_connection(db_name)
print(db.list_collection_names()) # base geobr

# executar o arquivo pelo terminal:
# python3 app.py

def get_municipios_estado(_uf: str) -> list:
  # res = resultado da consulta
  res = db.municipios.find(
    { 'Uf': _uf}, { '_id': 0, 'Nome': 1 }
  )
  return list(res)

# ATIVIDADEs: 
# 1. Consulta todos os municipios do Acre

result = get_municipios_estado("AC")
print(f'total = {len(result)}')
pprint(result) #  22

# 2. Consulta municipios Roraima (total = )
# get_municipios_estado("RR")

# 3. Consulta municipios com nome Cascavel, remover o _id do result

# 4. Municipios que começam com a letra W

# 5. Municípios da região Norte

# 6. Ranking dos estados com maior quantidade de municipios