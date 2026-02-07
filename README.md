# API Controle de Estoque

API REST para controle de estoque desenvolvida com Flask e MySQL.

## Tecnologias

- Python 3
- Flask
- MySQL
- mysql-connector-python

## Como rodar o projeto

### 1. Pré-requisitos

- Python 3 instalado
- MySQL instalado e rodando

### 2. Criar o banco de dados

Abra o MySQL e execute os comandos de 'schema.sql':


```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar a conexão

No arquivo `app.py`, ajuste as credenciais do MySQL se necessário:

```python
host='localhost',
user='root',
password='root',
database='estoque'
```

### 5. Rodar a aplicação

```bash
python app.py
```

O servidor vai iniciar em `http://localhost:5000`.

## Rotas da API

### Adicionar item — `POST /api/estoque`

Body (JSON):

```json
{
    "nome": "Teclado",
    "marca": "Logitech",
    "qtd_disponivel": 10,
    "valor_unitario": 89.90
}
```

### Listar estoque — `GET /api/estoque`

Retorna todos os produtos cadastrados.

### Editar item — `PUT /api/estoque/<id>`

Body (JSON):

```json
{
    "nome": "Teclado Mecânico",
    "marca": "Logitech",
    "qtd_disponivel": 8,
    "valor_unitario": 129.90
}
```

### Excluir item — `DELETE /api/estoque/<id>`

Remove o produto pelo ID.
