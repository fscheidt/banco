# Configuração inicial do projeto

## Banco de dados

### arquivo .env

criar arquivo chamado `.env` na pasta raiz do projeto contendo a url de conexão com o banco de dados, obtido no site do mongodb atlas.

Exemplo: 

```
db_url = "mongodb+srv://felippe:SECRET@cluster0.9nif1fg.mongodb.net/?retryWrites=true&w=majority"

```

### Restaurar

O script `restaurar.py` restaura uma base de dados no mongodb atlas. Caso essa base não exista, ela será gerada automaticamente. O comando para criar a base:

```bash

python restaurar.py municipios

```

Restaura a base de dados de books

```bash

python restaurar.py books

```


## Configuração do python

Criar o ambiente virtual na mesma pasta do projeto:

```bash

python3 -m venv env

```

Ativar o ambiente:

```bash

source env/bin/activate

```

## Instalar as bibliotecas (dependências)

```bash

pip install pymongo python-dotenv requests

```

Ou, instalar as bibliotecas usando o arquivo requirements.txt:

```bash

pip install -r requirements.txt

```

## Consultas

Script com exemplos de consultas no banco de dados `paisesdb`:

```bash
python3 consultas/paises.py
```
