from flask import Blueprint, jsonify, request,json, redirect, url_for, session
from config.db import db, app, ma
from models.Roles import Roles, RolesSchema

ruta_rol = Blueprint("ruta_rol",__name__)

rol_schema = RolesSchema()
roles_schema = RolesSchema(many=True)

@ruta_rol.route("/", methods=["GET"])
def roles():
    resultall = Roles.query.all()
    result = roles_schema.dump(resultall)    
    session['roles'] = result
    return result

@ruta_rol.route("/save", methods=["POST"])
def saverol():
    name = request.json['name'].title()
    rol = db.session.query(Roles.id).filter(Roles.type_user == name).all()
    result = roles_schema.dump(rol)

    if len(result)==0:
        new_rol = Roles(name)
        db.session.add(new_rol)
        db.session.commit()
        resultall = Roles.query.all()
        result = roles_schema.dump(resultall)    
        session['roles'] = result
        return jsonify({'mensaje': 'Registro exitoso'}) 
    else:
        return jsonify({'error': 'Opss... nombre en uso'}), 401 
        
@ruta_rol.route("/update", methods=["PUT"])
def updaterol():
    id = request.json['id']
    nrol = Roles.query.get(id) #Select * from Cliente where id = id
    nrol.type_user = request.json['name'].title()
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_rol.route("/delete/<id>", methods=["GET"])
def deleterol(id):
    rol = Roles.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(rol_schema.dump(rol))