from flask import Flask, request

app = Flask(__name__)

@app.route('/calcular', methods=['POST'])
def calcular():
    dados = request.get_json()
    num1 = float(dados['num1'])
    num2 = float(dados['num2'])
    operacao = dados['operacao']

    if operacao == 'adicao':
        resultado = num1 + num2
    elif operacao == 'subtracao':
        resultado = num1 - num2
    elif operacao == 'multiplicacao':
        resultado = num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            resultado = num1 / num2
        else:
            return 'Erro: Divisão por zero não é permitida', 400
    else:
        return 'Operação inválida', 400

    return {'resultado': resultado}

if __name__ == '__main__':
    app.run(debug=True)