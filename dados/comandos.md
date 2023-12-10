# Comandos

## Exporta dados para o atlas cloud

Abrir o terminal na pasta do projeto. Acessar a pasta dados:

```bash
cd dados
```

Salva na máquina local os dados do banco `booksdb` armazenados na cloud.

```bash
mongodump --uri mongodb+srv://felippe:SECRET@cluster0.9nif1fg.mongodb.net/booksdb
```
este comando gera o arquivo `dump/booksdb/booksdb.bson`


salva `paisesdb` e `geobr`:

```bash
mongodump --uri mongodb+srv://felippe:SECRET@cluster0.9nif1fg.mongodb.net/paisesdb
mongodump --uri mongodb+srv://felippe:SECRET@cluster0.9nif1fg.mongodb.net/geobr
```

## Import dados do arquivo bson para o atlas

```bash
mongorestore --uri mongodb+srv://felippe:SECRET@cluster0.9nif1fg.mongodb.net -d booksdb dump/booksdb/books.bson
```

```bash
mongorestore --uri mongodb+srv://felippe:SECRET@cluster0.9nif1fg.mongodb.net -d paisesdb dump/paisesdb/paises.bson
```

```bash
mongorestore --uri mongodb+srv://felippe:SECRET@cluster0.9nif1fg.mongodb.net -d geobr dump/geobr/municipios.bson
```
