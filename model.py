from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()


class Product(db.Model):
    product_id = db.Column(db.Integer, unique=True, primary_key=True)
    product_price = db.Column(db.Float, nullable=False)
    product_name = db.Column(db.String(80), nullable=False)
    size = db.Column(db.Integer, nullable=False)

    def __init__(self, product_id, product_price, product_name, size):
        self.product_id = product_id
        self.product_price = product_price
        self.product_name = product_name
        self.size = size


class ProductSchema(ma.Schema):
    product_id = fields.Integer(required=True)
    product_price = fields.Float(required=True)
    product_name = fields.String(required=True)
    size = fields.Integer(required=True)
