from config.db import app, db, ma


class StatesMaterials(db.Model):
    __tablename__ = "StatesMaterials"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    id_request = db.Column(db.Integer, db.ForeignKey('Requests.id'))
    id_materials = db.Column(db.Integer, db.ForeignKey('Materials.id'))

    def __init__(self, id_request, id_materials):
        self.id_request = id_request,
        self.id_materials = id_materials
        
with app.app_context():
    db.create_all()

class StatesMaterialsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_request', 'id_materials')