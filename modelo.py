
from config import *


class Cliente(db.Model):
    # atributos do cliente
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String(300), unique=True, nullable=False) 
    cpf = db.Column(db.Integer, unique=True, nullable=False)
    data_nasc = db.Column(db.Date, unique=True, nullable=False)
    rg = db.Column(db.Integer, unique=True, nullable=False)
    celular = db.Column(db.Integer, unique=True, nullable=False)
    endereco = db.Column(db.Text, unique=True, nullable=False)

 
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "email": self.email,
            "cpf": self.cpf,
            "data_nasc": self.data_nasc,
            "rg": self.rg,
            "celular": self.celular,
            "endereco": self.endereco,     


        }

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe Pessoa
    p1 = Cliente(username='admin',password='123',name='camz',email='camilaa',cpf=123,data_nasc=6/5/2002,rg=1233,celular=9643981,endereco="kfekfjgnqaeg")
        
    
    # persistir
    db.session.add(p1)
    db.session.commit()
    
    # exibir a pessoa
    print(p1)

    # exibir a pessoa no format json
    print(p1.json())