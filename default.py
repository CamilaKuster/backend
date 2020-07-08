from config import *
from modelo import Cliente
#importado tudo de config e importando a classe cliente

@app.route("/")
#quando possui somente a barra é normalmente o index ou o home (a pagina inicial do site)
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
#dar o código do debug e quando ir salvando Ctrl S ja ir atualizando 