from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id':0,
     'nome':'Rafael',
     'habilidades':['Python', 'Flask']},
    {'id':1,
     'nome':'Galleani',
     'habilidades':['Python', 'Django']}
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def deselvolvedor(id):
        if request.method == 'GET':
            try:
                response = desenvolvedores[id]
            except IndexError:
                mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
                response = {'status':'Erro', 'Mensagem':mensagem}
            except Exception:
                mensagem = 'Erro desconhecido. Procure o desenvolvedor da API'
                response = {'status':'Erro', 'Mensagem':mensagem}
            return jsonify(response)
        elif request.method == 'PUT':
            dados = json.loads(request.data)
            desenvolvedores[id]= dados
            return jsonify(dados)
        elif request.method == 'DELETE':
            desenvolvedores.pop(id)
            return jsonify({'Status':'Sucesso', 'Mensagem':'Registro Excluído'})

@app.route('/dev/', methods=['GET', 'POST'])
def lista_deselvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)