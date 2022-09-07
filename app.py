from enum import unique
from flask import Flask, flash, render_template, redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SECRET_KEY'] = 'clave_secretaa'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:contrasenia@host/nombreDB'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/migrate-db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    idTipodni = db.Column(db.Integer, ForeignKey('tipodni.id'), nullable=False)
    tipodni = db.relationship('TipoDni', backref='persona')
    dni =  db.Column(db.String(8), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    idLocalidad = db.Column(db.Integer, ForeignKey('localidad.id'), nullable=False)
    localidad = db.relationship('Localidad')
    idPais = db.Column(db.Integer, ForeignKey('pais.id'), nullable=False)
    pais = db.relationship('Pais')
    f_nacimiento = db.Column(db.Date, nullable=False)
    idSexo = db.Column(db.Integer, ForeignKey('sexo.id'), nullable=False)
    sexo = db.relationship('Sexo')
    telefono = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    f_carga = db.Column(db.Date, nullable=False)
    activo = db.Column(db.Boolean, nullable=False)

class TipoUsuario(db.Model):
    __tableame__ = 'tipousuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    contrasenia = db.Column(db.String(50), nullable=False)
    idTipoUsuario = db.Column(db.Integer, ForeignKey('tipo_usuario.id'), nullable=False)
    tipousuario = db.relationship('TipoUsuario')
    idPersona = db.Column(db.Integer, ForeignKey('persona.id'), nullable=False)
    persona = db.relationship('Persona')
    f_carga = db.Column(db.Date, nullable=False)
    
    
    
class Sexo(db.Model):
    __tablename__ = 'sexo'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class TipoDni(db.Model):
    __tablename__ = 'tipodni'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    
class Pais(db.Model):
    __tablename__ = 'pais'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))
    
    
class Provincia(db.Model):
    __tablename__ = 'provincia'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    idPais = db.Column(db.Integer, ForeignKey('pais.id'), nullable=False)
    pais = db.relationship('Pais')

class Localidad(db.Model):
    __tablename__ = 'localidad'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    idProvincia = db.Column(db.Integer, ForeignKey("provincia.id"))
    provincia = db.relationship("Provincia")
    



if __name__ == '__main':
    app.run(debug=True)