from config.db import app, db, ma

class Users(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String(100))
    roles = db.Column(db.Integer, db.ForeignKey('Roles.id'))
    user = db.Column(db.String(100), unique= True)
    password = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    mail = db.Column(db.String(150))
    direction = db.Column(db.String(100))
    location = db.Column(db.String(100))
    ability = db.Column(db.Integer)

    def __init__(self, name, roles, user, password, phone, mail, direction, location, ability):
        self.name = name,
        self.roles = roles
        self.user = user,
        self.password = password,
        self.phone = phone,
        self.mail = mail,
        self.direction = direction,
        self.location = location,
        self.ability = ability,

with app.app_context():
    db.create_all()

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'roles', 'user', 'password', 'phone', 'mail','direction', 'location', 'ability')