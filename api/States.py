from flask import Blueprint, jsonify, request,json, redirect, url_for, session
from config.db import db, app, ma
from models.States import States, StatesSchema

ruta_states = Blueprint("ruta_states", __name__)

state_schema = StatesSchema()
states_schema = StatesSchema(many=True)

@ruta_states.route("/", methods=["GET"])
def states():
    resultall =  States.query.all()
    result = states_schema.dump(resultall)
    session['states'] = result
    return result

@ruta_states.route("/save", methods=["POST"])
def save_states():
    state = request.json['state'].title()
    new_state = States(state= state)
    db.session.add(new_state)
    db.session.commit()
    resultall = states_schema.dump(States.query.all())
    session['states'] = resultall
    return jsonify({'mensaje' : 'Registro existoso'})

@ruta_states.route("/update", methods=["PUT"])
def update_states():
    id = request.json["id"]
    nState = States.query.get(id)
    nState.state = request.json['state']
    db.session.commit()
    return "Datos actualizados con exito"

@ruta_states.route("/delete/<id>", methods=["GET"])
def delete_states(id):
    states = States.query.get(id)
    db.session.delete(states)
    db.session.commit()
    return jsonify(state_schema.dump(states))