from app import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100))
    marca = db.Column(db.String(100))
    ano = db.Column(db.Integer)
    km = db.Column(db.Integer)
    cambio = db.Column(db.String(100))
    combustivel = db.Column(db.String(100))
    final_da_placa = db.Column(db.String(100))
    cor = db.Column(db.String(100))
    preco = db.Column(db.Float)
    image_url = db.Column(db.String(200))


    def __repr__(self):
        return f'<Car {self.name}>'
