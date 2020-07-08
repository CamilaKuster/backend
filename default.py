from config import *
from modelo import Cliente

@app.route("/")
def inicio():
    return 'Sistema de cadastro de pessoas. '+\
        '<a href="/listar_clientes">Operação listar</a>'

@app.route("/listar_clientes")
def listar_clientes():
    clientes = db.session.query(Cliente).all()
    # aplicar o método json que a classe Pessoa possui a cada elemento da lista
    clientes_em_json = [ x.json() for x in clientes ]
    # converter a lista do python para json
    resposta = jsonify(clientes_em_json)
    # PERMITIR resposta para outras pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

app.run(debug=True)