#aquì colocamos los comandos para la configuraciòn con la bd de mysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Realizar la conexión
app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root@localhost/bdhackathon"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app.secret_key = "BDbdhackathon"

#creamos los objetos de transferencias a la bd

db = SQLAlchemy(app)
ma = Marshmallow(app)