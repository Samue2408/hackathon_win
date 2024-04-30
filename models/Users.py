from config.db import app, db, ma

class Users(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String(100))
    id_roles = db.Column(db.Integer, db.ForeignKey('Roles.id'))
    user = db.Column(db.String(100), unique= True)
    password = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    mail = db.Column(db.String(150))
    location = db.Column(db.String(100))
    ability = db.Column(db.Integer)

    def __init__(self, name, id_roles, user, password, phone, mail, location, ability= None):
        self.name = name,
        self.id_roles = id_roles
        self.user = user,
        self.password = password,
        self.phone = phone,
        self.mail = mail,
        self.location = location,
        self.ability = ability,

with app.app_context():
    db.create_all()

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'id_roles', 'user', 'password', 'phone', 'mail', 'location', 'ability')