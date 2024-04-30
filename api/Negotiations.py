from flask import Blueprint, jsonify, request,json, redirect, url_for, session
from config.db import db, app, ma
from models.Negotiations import Negotiations, NegotiationsSchema
from api.Requests import requests_schema
from models.Requests import Requests, RequestsSchema

ruta_negotiations = Blueprint("ruta_negotiations", __name__)

negotiation_schema = NegotiationsSchema()
negotiations_schema = NegotiationsSchema(many=True)

@ruta_negotiations.route("/", methods=["GET"])
def negotiations():
    resultall =  Negotiations.query.all()
    result = negotiations_schema.dump(resultall)
    session['negotiations'] = result
    return result

@ruta_negotiations.route("/save", methods=["POST"])
def save_negotiation():
    id_request = request.json['id_request']
    req = db.session.query(Requests.id).filter(Requests.id == id_request).all()
    req_result = requests_schema.dump(req)
    
    if len(req_result)!=0:
        proposal = request.json['proposal']
        new_request = Negotiations(id_request= id_request, proposal= proposal)
        db.session.add(new_request)
        db.session.commit()
        resultall = negotiations_schema.dump(Negotiations.query.all())
        session['negotiations'] = resultall
        return jsonify({'mensaje' : 'Registro existoso'})
    else:
        return jsonify({'mensaje' : 'No se encontro request'})

@ruta_negotiations.route("/update", methods=["PUT"])
def update_negotiations():
    id = request.json["id"]
    nNegotiation = Negotiations.query.get(id)
    nNegotiation.id_request = request.json['id_request']
    nNegotiation.proposal = request.json['proposal']
    db.session.commit()
    return "Datos actualizados con exito"

@ruta_negotiations.route("/delete/<id>", methods=["GET"])
def delete_negotiations(id):
    Negot = Negotiations.query.get(id)
    db.session.delete(Negot)
    db.session.commit()
    return jsonify(negotiation_schema.dump(Negot))