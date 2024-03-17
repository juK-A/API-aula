from flask import Flask, request, jsonify
import json

app = Flask(__name__)

tarefas = []

@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    tarefa = request.get_json()
    tarefas.append(tarefa)
    with open('tarefas.json', 'w') as f:
        json.dump(tarefas, f)
    return jsonify(tarefa), 201

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas/<int:id>', methods=['PUT'])
def marcar_concluida(id):
    for tarefa in tarefas:
        if tarefa.get('id') == id:
            tarefa['concluida'] = True
            with open('tarefas.json', 'w') as f:
                json.dump(tarefas, f)
            return jsonify(tarefa)
    return 'Tarefa não encontrada', 404

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    for tarefa in tarefas:
        if tarefa.get('id') == id:
            tarefas.remove(tarefa)
            with open('tarefas.json', 'w') as f:
                json.dump(tarefas, f)
            return 'Tarefa excluída com sucesso'
    return 'Tarefa não encontrada', 404

if __name__ == '__main__':
    app.run(debug=True)