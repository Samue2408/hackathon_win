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
    return result

@ruta_materials.route("/save", methods=["POST"])
def save_materials():  
    name = request.json['name']
    price = request.json['price']
    new_materials = Materials(name= name, price= price)
    db.session.add(new_materials)
    db.session.commit()
    resultall = materials_schema.dump(Materials.query.all())
    session['materials'] = resultall
    return jsonify({'mensaje' : 'Registro existoso'})

@ruta_materials.route("/update", methods=["PUT"])
def update_materials():
    id = request.json["id"]
    nMaterial = Materials.query.get(id)
    nMaterial.name = request.json['name']
    nMaterial.price = request.json['price']
    db.session.commit()
    return "Datos actualizados con exito"

@ruta_materials.route("/delete/<id>", methods=["GET"])
def delete_materials(id):
    material = Materials.query.get(id)
    db.session.delete(material)
    db.session.commit()
    return jsonify(material_schema.dump(material))