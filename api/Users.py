from flask import Blueprint, jsonify, request, json, redirect, url_for, session
from config.db import db, app, ma
from models.Users import Users, UsersSchema
from api.Roles import Roles, roles_schema

ruta_users = Blueprint("ruta_users",__name__)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

@ruta_users.route("/", methods=["GET"])
def User():
    resultall = Users.query.all()
    result = users_schema.dump(resultall)    
    session['users'] = result
    return result

@ruta_users.route("/save", methods=["POST"])
def saveUser():    
    user = request.json['user'].lower()
    User = db.session.query(Users.id).filter(Users.user == user).all()
    result = users_schema.dump(User)

    if len(result)==0:

        role = request.json['role'].title()

        ro = db.session.query(Roles.id).filter(Roles.type_user == role).all()
        role_result = roles_schema.dump(ro)  

        if len(role_result) > 0:
            id_role = role_result[0]['id']

            name = request.json['name'].title()        
            password = request.json['password']
            mail = request.json['mail']
            phone = request.json['phone']
            location = request.json['location']

            if role == "Seller":
                new_User = Users(name= name,id_roles= id_role, user= user, password= password, phone= phone, mail= mail, location= location)
            elif role == "Buyer":
                new_User = Users(name= name,id_roles= id_role, user= user, password= password, phone= phone, mail= mail, location= location, ability= 500)
            
            db.session.add(new_User)
            db.session.commit()
            resultall = Users.query.all()
            result = users_schema.dump(resultall)  
            session['users'] = result
            return jsonify({'mensaje': 'Registro exitoso'}) 
        else:
            return jsonify({'error': 'Opss... rol no disponible'}), 401
    else:
        return jsonify({'error': 'Opss... nombre en uso'}), 401 
        
@ruta_users.route("/update", methods=["PUT"])
def updateUsers():
    id = request.json['id']
    nUser = Users.query.get(id) #Select * from Cliente where id = id
    nUser.name = request.json['name'].title()        
    nUser.user = request.json['user'].lower()
    nUser.id_roles = request.json['role'].lower()
    nUser.password = request.json['password']
    nUser.mail = request.json['mail']
    nUser.phone = request.json['phone']
    nUser.location = request.json['location']
    nUser.ability = request.json['ability']
    db.session.commit()
    return "Datos Actualizado con exitos"

@ruta_users.route("/delete/<id>", methods=["GET"])
def deleteUser(id):
    User = Users.query.get(id)
    db.session.delete(User)
    db.session.commit()
    return jsonify(user_schema.dump(User))