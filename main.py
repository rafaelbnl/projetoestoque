import mysql.connector
from flask import Flask, jsonify, request


def criar_conexao():
    print("Iniciando conexão...")
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='estoque'
    )   
        print("Conexão estabelecida!")
        return conn
    except Exception as e:
        raise ConnectionError(f"Erro ao conectar: {e}")

app = Flask(__name__)


@app.route("/api/estoque", methods=['POST'])
def adicionar_item():
    dados = request.json
    nome = dados['nome']
    marca = dados['marca']
    qtd_disponivel = dados['qtd_disponivel']
    valor_unitario = dados['valor_unitario']

    with criar_conexao() as connect:
        with connect.cursor() as cursor:
            cursor.execute("""
                INSERT INTO produtos 
                            (nome, marca, qtd_disponivel, valor_unitario) 
                                VALUES (%s, %s, %s, %s)
                                    """, (nome, marca, qtd_disponivel, valor_unitario))
            connect.commit()
            return jsonify({"mensagem": "Item cadastrado."}), 200

@app.route("/api/estoque", methods=['GET'])
def visualizar_estoque():
    with criar_conexao() as connect:
        with connect.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT 
                                nome as 'Nome',
                                marca as 'Marca',
                                qtd_disponivel as 'Quantidade em Estoque',
                                valor_unitario as 'Valor unitário'
                                    FROM produtos""")
            estoque = cursor.fetchall()
            return jsonify(estoque)

@app.route("/api/estoque/<int:id>", methods=['PUT'])
def editar_item(id: int):
    dados = request.json
    nome = dados['nome']
    marca = dados['marca']
    qtd_disponivel = dados['qtd_disponivel']
    valor_unitario = dados['valor_unitario']

    with criar_conexao() as connect:
        with connect.cursor() as cursor:
            cursor.execute("""
                UPDATE produtos
                        SET nome = %s, marca = %s, qtd_disponivel = %s, valor_unitario = %s
                            WHERE id = %s
                                    """, (nome, marca, qtd_disponivel, valor_unitario, id))
            connect.commit()
            return jsonify({"mensagem": "Item alterado."}), 200

@app.route("/api/estoque/<int:id>", methods=['DELETE'])
def excluir_item(id:int):
    with criar_conexao() as connect:
        with connect.cursor() as cursor:
            cursor.execute("""
                DELETE FROM produtos
                            WHERE id = %s
                                    """, (id,))
            connect.commit()
            return jsonify({"mensagem": "Item excluído."})




if __name__ == "__main__":
    app.run(debug=True)