# Comandos

## Exporta dados do atlas

Salva na máquina local os dados do banco de dados booksdb armazenados na cloud.

```bash
mongodump --uri mongodb+srv://felippe:SECRET@cluster0.9nif1fg.mongodb.net/booksdb
```
este comando gera o arquivo `dump/booksdb.bson`

## Import dados do arquivo para o atlas

```bash
mongoimport --uri mongodb+srv://felippe:SECRET@cluster0.9nif1fg.mongodb.net/booksdb dump/booksdb.bson
```

