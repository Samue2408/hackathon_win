from config.db import app, db, ma
from datetime import datetime


class Requests(db.Model):
    __tablename__ = "Requests"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    id_state = db.Column(db.Integer, db.ForeignKey('States.id'))
    id_seller = db.Column(db.Integer, db.ForeignKey('Users.id'))
    id_buyer = db.Column(db.Integer, db.ForeignKey('Users.id'))
    location = db.Column(db.String(100))
    date_time = db.Column(db.DateTime, default=datetime.utctimetuple)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __init__(self, id_state, id_seller, id_buyer, location, date_time, quantity, price):
        self.id_state = id_state,
        self.id_seller = id_seller
        self.id_buyer = id_buyer,
        self.location = location,
        self.date_time = date_time,
        self.quantity = quantity,
        self.price = price,

with app.app_context():
    db.create_all()

class RequestsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_state', 'id_seller', 'id_buyer', 'location', 'date_time', 'quantity','price')