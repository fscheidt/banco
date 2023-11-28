from app import get_connection
from pprint import pprint
db = get_connection(database="paisesdb")
def consulta_codigo_area(cod):
  """ Qual o pais com codigo de chamada "cod" ? """
  doc = db.paises.find_one(
    {"callingCode": cod}, 
    {"name.common": 1, "_id": 0}
  )
  pprint(doc)
consulta_codigo_area("55") # => Brazil
consulta_codigo_area("595") # => Py
# rodar no terminal:
# python3 paises_consultas.py