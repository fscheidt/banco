from pprint import pprint
from pymongo.mongo_client import MongoClient
from database import get_connection

# FUNÇÕES DE CONSULTA:

def get_municipios_por_estado(db, _uf: str) -> list:
    res = db.municipios.find(
        { 'Uf': _uf}, { '_id': 0, 'Nome': 1 }
    )
    return list(res)

# Executa script:
if __name__ == "__main__":

    DB_NAME = "geobr"
    
    db = get_connection(DB_NAME)
    print(db.list_collection_names())

    print("="*40)
    print("Municípios do estado do Acre")
    result = get_municipios_por_estado(db, "AC")
    pprint(result) 
    print(f'total = {len(result)}') #  22
    print("="*40)
