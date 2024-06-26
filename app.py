from flask import Flask, render_template, request, redirect, url_for, session, make_response
from config.db import app, db

from api.Roles import ruta_rol
from api.Users import ruta_users
from api.Materials import ruta_materials

app.register_blueprint(ruta_rol, url_prefix="/api/roles")
app.register_blueprint(ruta_users, url_prefix="/api/users")
app.register_blueprint(ruta_materials, url_prefix="/api/materials")

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'),404



@app.route("/sale")
def sale():
    return render_template('sale.html')



if __name__ == '__main__': 
    app.run(debug=True, port=5000)