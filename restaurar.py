import argparse
import requests
from app import get_connection

dados = {
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
}

def restore(perfil: str):
    # perfil = "municipios"

    print(f"Restaurando dados de [{perfil}] ")

    recurso = dados[perfil]  
    collection = recurso['collection']

    def download_json_file(file_url):
        with requests.get(file_url, stream=True) as r:
            data = r.json()
        return data

    data = download_json_file(recurso['url'])

    db = get_connection(recurso['db_name'])

    db[collection].drop()

    db[collection].insert_many(data)

    documents = db[collection].count_documents({})
    print(f"{documents = }")


if __name__ == "__main__":
    """
    python restaurar.py municipios
    python restaurar.py books
    """
    parser = argparse.ArgumentParser("restaurar")
    parser.add_argument("perfil", help="municipios ou books", type=str)
    args = parser.parse_args()
    restore(args.perfil)
