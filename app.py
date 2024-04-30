from flask import Flask, render_template, request, redirect, url_for, session, make_response
from config.db import app, db

from api.Roles import ruta_rol
from api.Users import ruta_users

app.register_blueprint(ruta_rol, url_prefix="/api/roles")
app.register_blueprint(ruta_users, url_prefix="/api/users")

@app.route("/")
def index():
    return render_template('login.html')



if __name__ == '__main__': 
    app.run(debug=True, port=5000)