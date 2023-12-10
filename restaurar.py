import argparse
import requests
from database import get_connection

dados = {  # <== adicionar outras bases de dados aqui
    "municipios" : {
        "db_name": "geobr",
        "collection": "municipios",
        "url": "https://raw.githubusercontent.com/fscheidt/iotdb-23/master/dados/municipios.json",
    },
    "books" : {
        "db_name": "booksdb",
        "collection": "books",
        "url": "https://raw.githubusercontent.com/fscheidt/iotdb-23/master/dados/books.json",
    },
    "paises" : {
        "db_name": "paisesdb",
        "collection": "paises",
        "url": "https://raw.githubusercontent.com/fscheidt/iotdb-23/master/dados/paises.json",
    },
}

def download_json_file(url: str):
    with requests.get(url) as r:
        data = r.json()
        for row in data:
            if "_id" in row:
                del row["_id"]  # <= remove campo _id se existir
        return data

def restore(perfil: str, drop_db: bool = True):
    """
    Importa dados do arquivo json para o mongodb atlas  
        @param perfil: nome do perfil de dados (ex.: municipios)
    """

    print(f"Restaurando dados de [{perfil}] ")
    recurso = dados[perfil]  
    collection = recurso['collection']

    data = download_json_file(recurso['url'])
    db = get_connection(recurso['db_name'])

    db[collection].drop()
    db[collection].insert_many(data)
    documents = db[collection].count_documents({})
    print(f"documentos importados: {documents}")


if __name__ == "__main__":
    """
    Exemplos para restaturar: 
        python restaurar.py municipios
        python restaurar.py books
        python restaurar.py paises
    """
    parser = argparse.ArgumentParser("restaurar")
    parser.add_argument("perfil", help="municipios/books/paises", type=str)
    args = parser.parse_args()
    restore(args.perfil)
