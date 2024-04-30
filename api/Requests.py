from flask import Blueprint, jsonify, request,json, redirect, url_for, session
from config.db import db, app, ma
from models.Requests import Requests, RequestsSchema


ruta_requests = Blueprint("ruta_requests", __name__)

request_schema = RequestsSchema()
requests_schema = RequestsSchema(many=True)

@ruta_requests.route("/", methods=["GET"])
def requests():
    resultall =  Requests.query.all()
    result = requests_schema.dump(resultall)
    session['requests'] = result
    return result

@ruta_requests.route("/save", methods=["POST"])
def save_requests():
    id_state = request.json['id_state']
    id_seller = request.json['id_seller']
    id_buyer = request.json['id_buyer']
    id_materials = request.json['id_materials']
    location = request.json['location']
    date_time = request.json['date_time']
    quantity = request.json['quantity']
    price = request.json['price']
    new_requets = Requests(id_state= id_state, id_seller= id_seller, id_buyer= id_buyer, id_materials= id_materials, location= location, date_time= date_time, quantity= quantity, price= price)
    db.session.add(new_requets)
    db.session.commit()
    resultall = requests_schema.dump(Requests.query.all())
    session['requests'] = resultall
    return jsonify({'mensaje' : 'Registro existoso'})

@ruta_requests.route("/update", methods=["PUT"])
def update_requests():
    id = request.json["id"]
    nRequest = Requests.query.get(id)
    nRequest.id_state = request.json['id_state']
    nRequest.id_seller = request.json['id_seller']
    nRequest.id_buyer = request.json['id_buyer']
    nRequest.id_materials = request.json['id_materials']
    nRequest.location = request.json['location']
    nRequest.date_time = request.json['date_time']
    nRequest.quantity = request.json['quantity']
    nRequest.price = request.json['price']
    db.session.commit()
    return "Datos actualizados con exito"

@ruta_requests.route("/delete/<id>", methods=["GET"])
def delete_requests(id):
    request = Requests.query.get(id)
    db.session.delete(request)
    db.session.commit()
    return jsonify(requests_schema.dump(request))