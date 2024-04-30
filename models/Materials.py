from config.db import app, db, ma

class Materials(db.Model):
    __tablename__ = "Materials"
    
    id = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
with app.app_context():
    db.create_all()

class MaterialsShema(ma.Schema):
    class Meta:
        fields = ('id','name', 'price')