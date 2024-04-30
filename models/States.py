from config.db import app, db, ma

class States(db.Model):
    __tablename__ = "States"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    state = db.Column(db.String(100))

    def __init__(self, state):
        self.state = state

with app.app_context():
    db.create_all()

class StatesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'state')