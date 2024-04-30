from config.db import app, db, ma

class Roles(db.Model):
    __tablename__ = "Roles"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    type_user = db.Column(db.String(100))

    def __init__(self, type_user):
        self.type_user = type_user
        
def agregar_rol(tipo):
    usuario_existente = Roles.query.filter_by(type_user= tipo).first()
    if usuario_existente is None:
        nuevo_rol = Roles(type_user= tipo)
        db.session.add(nuevo_rol)
        db.session.commit()

with app.app_context():
    db.create_all()
    agregar_rol("Reciclador")
    agregar_rol("Vendedor")
    agregar_rol("administrador")

class RolesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type_user')