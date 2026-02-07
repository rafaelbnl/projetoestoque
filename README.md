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