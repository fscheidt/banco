
# Configuração inicial do projeto

## Restaurar base de dados:

restaura base de dados de municipios
```bash
python restaurar.py municipios
```

restaura base de dados de books
```bash
python restaurar.py books
```


## Criar o ambiente virtual

```bash
python3 -m venv env
```

Ativar o ambiente:
```bash
source env/bin/activate
```

## Instalar as bibliotecas (dependências)
```
pip install pymongo python-dotenv requests
```
