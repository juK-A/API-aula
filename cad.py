from flask import Flask, request, jsonify
import json

app = Flask(__name__)

usuarios = []

@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    usuario = request.get_json()
    usuarios.append(usuario)
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)
    return jsonify(usuario), 201

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario_atualizado = request.get_json()
    for usuario in usuarios:
        if usuario.get('id') == id:
            usuarios[usuarios.index(usuario)] = usuario_atualizado
            with open('usuarios.json', 'w') as f:
                json.dump(usuarios, f)
            return jsonify(usuario_atualizado)
    return 'Usuário não encontrado', 404

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    for usuario in usuarios:
        if usuario.get('id') == id:
            usuarios.remove(usuario)
            with open('usuarios.json', 'w') as f:
                json.dump(usuarios, f)
            return 'Usuário excluído com sucesso'
    return 'Usuário não encontrado', 404

if __name__ == '__main__':
    app.run(debug=True)