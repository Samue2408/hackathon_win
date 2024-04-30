from flask import Blueprint, jsonify, request,json, redirect, url_for, session
from config.db import db, app, ma
from models.Materials import Materials, MaterialsShema

ruta_materials = Blueprint("ruta_materials", __name__)

material_schema = MaterialsShema()
materials_schema = MaterialsShema(many=True)

@ruta_materials.route("/", methods=["GET"])
def materials():
    resultall =  Materials.query.all()
    result = materials_schema.dump(resultall)
    session['materials'] = result
    return redirect(url_for("materials"))

@ruta_materials.route("/save", methods=["POST"])
def save_materials():  
    date_time = request.json['date_time']
    user = request.json['user']
    publication = request.json['publication']
    quotes = request.json['quotes']
    new_materials = Materials(date_time = date_time, user = user, publication = publication, quotes = quotes)
    db.session.add(new_materials)
    db.session.commit()
    resultall = materials_schema.dump(Materials.query.all())
    session['materials'] = resultall
    return jsonify({'mensaje' : 'Registro existoso'})

@ruta_materials.route("/update", methods=["PUT"])
def update_materials():
    id = request.json["id"]
    nMaterial = Materials.query.get(id)
    nMaterial.date_time = request.json['date_time']
    nMaterial.user = request.json['user']
    nMaterial.publication = request.json['publication']
    nMaterial.quotes = request.json['quotes']
    db.session.commit()
    return "Datos actualizados con exito"

@ruta_materials.route("/delete/<id>", methods=["GET"])
def delete_materials(id):
    material = Materials.query.get(id)
    db.session.delete(material)
    db.session.commit()
    return jsonify(material_schema.dump(material))