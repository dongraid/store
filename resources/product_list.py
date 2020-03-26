from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger
from model import db, Product, ProductSchema


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


class ProductListResource(Resource):
    @swagger.model
    @swagger.operation(notes='Get list of products')
    def get(self):
        products = Product.query.all()
        return products_schema.dump(products)

    @swagger.model
    @swagger.operation(notes='Load products to database')
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        payload = products_schema.load(json_data)
        for item in payload:
            product = Product(product_id=item['product_id'], product_price=item['product_price'],
                              product_name=item['product_name'], size=item['size'])
            db.session.add(product)
        db.session.commit()
        products = Product.query.all()
        return products_schema.dump(products)
