from config.db import app, db, ma

class Negotiations(db.Model):
    __tablename__ = "Negotiations"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    id_request = db.Column(db.Integer, db.ForeignKey('Requests.id'))
    proposal = db.Column(db.Integer)

    def __init__(self, id_request, proposal):
        self.id_request = id_request
        self.proposal = proposal

with app.app_context():
    db.create_all()

class NegotiationsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_request' 'proposal')