from config import json, app, os, 
from sqlalchemy import Column, Integer, String, Date, Text
from app import db


class Cliente(db.Model):
    # atributos do cliente
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String(300), unique=True, nullable=False) 
    cpf = db.Column(db.Integer, unique=True, nullable=False)
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
            "rg": self.rg,
            "celular": self.celular,
            "endereco": self.endereco,     


        }

# teste    

    # criar tabelas
    db.create_all()

    # teste da classe Pessoa
    p1 = Cliente(username='admin',password='123',name='camz',email='camilaa',cpf=123,data_nasc= 6/5/2004,rg=1233,celular=9643981,endereco="kfekfjgnqaeg")
        
    
    # persistir
    db.session.add(p1)
    db.session.commit()
    
    # exibir a pessoa
    print(p1)

    # exibir a pessoa no format json
    print(p1.json())