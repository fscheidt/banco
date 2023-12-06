import sys
from pprint import pprint
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import database

db = database.get_connection(db_name="paisesdb")

def consulta_codigo_area(cod):
    """ Qual o pais com codigo de chamada "cod" ? """
    doc = db.paises.find_one(
        {"callingCode": cod}, 
        {"name.common": 1, "_id": 0}
    )
    return doc

doc = consulta_codigo_area("55") # => Brazil
pprint(doc)

print("="*40)

doc = consulta_codigo_area("595") # => Py
pprint(doc)

print("="*40)
print("Paises com fronteira com Brazil:")
paises = list(
  db.paises.find(
    # operador in pesquisa nos valores dentro do vetor
    { "borders": { "$in": ["BRA"] } },
    {"name.common":1, "_id":0}
    )
)
print("fazem fronteira:", len(paises))
pprint(paises)

# rodar no terminal:
# python3 paises_consultas.py


consulta = db.paises.aggregate( 
[
  # ESTAGIO 1 
  { # WHERE
    "$match": { "region": "Americas" } 
  }, 
  # ESTAGIO 2
  { 
    "$project": { # SELECT
        "pais": "$name.common", 
        "capital": 1, 
        #"region": "$region",
        "_id": 0,
    }
  },
  # ESTAGIO 3
  { "$sort": { "capital": 1 }}
])

pprint(list(consulta))


# (12) Países que possuem mais de um idioma oficial:
q = db.paises.aggregate([
  { 
    "$addFields": {
      "lang_count": {
        "$size": {
          "$objectToArray": "$languages"
        }
      }
    }
  },
  {
    "$match": {
        "lang_count": {"$gte": 5}
    }
  },
  {
    "$project": {
        "_id": 0,
        "country": "$name.common",
        "langs": "$lang_count",
        #"languages": 1
    }
  }
])
res = list(q)
print(len(res))
pprint(res)

# Quais são os idiomas oficiais dos paises com mais
# de 4 idiomas


## GROUP BY

# (13) Sumarização: Total de países por `subregion`
query = db.paises.aggregate([ 
  {"$group": 
    {
      "_id": "$subregion",
      "paises": { 
          "$sum": 1 
      }
    }
   }
])
pprint(list(query))
