from config.db import app, db, ma

class Roles(db.Model):
    __tablename__ = "Roles"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    type_user = db.Column(db.String(100))

    def __init__(self, type_user):
        self.type_user = type_user

with app.app_context():
    db.create_all()

class RolesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'type_user')