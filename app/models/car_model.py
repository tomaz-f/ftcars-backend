from conn_db import db


class Car(db.Model):
    __tablename__ = "Cars"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String(255))
    name = db.Column(db.String(255))
    year = db.Column(db.Integer)
    color = db.Column(db.String(255))
    type = db.Column(db.String(255))

    def __init__(self, brand, name, year, color, type):
        self.brand = brand
        self.name = name
        self.year = year
        self.color = color
        self.type = type
