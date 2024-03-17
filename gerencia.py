from flask import Flask, request, jsonify
import json

app = Flask(__name__)

produtos = []
carrinho = []

@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    produto = request.get_json()
    produtos.append(produto)
    with open('produtos.json', 'w') as f:
        json.dump(produtos, f)
    return jsonify(produto), 201

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_estoque(id):
    estoque = request.get_json().get('estoque')
    for produto in produtos:
        if produto.get('id') == id:
            produto['estoque'] = estoque
            with open('produtos.json', 'w') as f:
                json.dump(produtos, f)
            return jsonify(produto)
    return 'Produto não encontrado', 404

@app.route('/produtos/<int:id>', methods=['DELETE'])
def excluir_produto(id):
    for produto in produtos:
        if produto.get('id') == id:
            produtos.remove(produto)
            with open('produtos.json', 'w') as f:
                json.dump(produtos, f)
            return 'Produto excluído com sucesso'
    return 'Produto não encontrado', 404

@app.route('/carrinho', methods=['POST'])
def adicionar_carrinho():
    item = request.get_json()
    carrinho.append(item)
    return jsonify(carrinho)

@app.route('/carrinho', methods=['GET'])
def listar_carrinho():
    return jsonify(carrinho)

if __name__ == '__main__':
    app.run(debug=True)