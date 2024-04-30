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

        role_result = roles_schema.dump(db.session.query(Roles.id).filter(Roles.type_user == role).all())  

        if len(role_result) > 0:
            id_role = role_result[0]['id']
            password = request.json['password']
            mail = request.json['mail']

            if role == "Seller":
                new_User = Users(id_roles= id_role, user= user, password= password, mail= mail)
            elif role == "Buyer":
                new_User = Users(id_roles= id_role, user= user, password= password, mail= mail, ability= 500)
            
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
    role_result = roles_schema.dump(db.session.query(Roles.id).filter(Roles.type_user == request.json['role'].lower()).all())  
    id_role = role_result[0]['id']
    nUser.id_roles = id_role
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

@ruta_users.route("/signin", methods=["POST"])
def signin():
    user = request.json['user'].lower()
    password = request.json['password']
    user_ = db.session.query(Users).filter(Users.user == user, Users.password == password).all()
    result = users_schema.dump(user_)

    if len(result)>0:
        usuario = result[0]

        ro = db.session.query(Roles.type_user).filter(Roles.id == usuario["id_roles"]).all()
        rol_result = roles_schema.dump(ro) 

        session['user'] = rol_result
            
        return jsonify({'mensaje': 'Bienvenido'})
    else:
        return jsonify({'error': 'Opss...'}), 401