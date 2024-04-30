from config.db import app, db, ma

class States(db.Model):
    __tablename__ = "States"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    state = db.Column(db.String(100))

    def __init__(self, state):
        self.state = state

def agregar_state(state):
    usuario_existente = States.query.filter_by(state= state).first()
    if usuario_existente is None:
        nuevo_state = States(state= state)
        db.session.add(nuevo_state)
        db.session.commit()

with app.app_context():
    db.create_all()
    agregar_state("Inactivo")
    agregar_state("En espera")
    agregar_state("Cancelado")

class StatesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'state')