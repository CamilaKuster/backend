from app import json, app, jsonify, 
from modelo import Cliente
from app import db

@app.route("/")
def inicio():
    return 'Sistema de cadastro de pessoas. '+\
        '<a href="/listar_clientes">Operação listar</a>'

@app.route("/listar_clientes")
def listar_clientes():
    clientes = db.session.query(Cliente).all()
    clientes_em_json = [ x.json() for x in clientes ]
    resposta = jsonify(clientes_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

app.run(debug=True)