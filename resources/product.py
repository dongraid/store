from flask import request
from flask_restful import Resource
from flask_restful_swagger import swagger
from model import db, Product, ProductSchema


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


class ProductResource(Resource):
    @swagger.model
    @swagger.operation(notes='Get product by ID')
    def get(self, product_id):
        product = Product.query.filter(Product.product_id == product_id).one_or_none()
        if not product:
            return {"error": 'Product not found with id: {product_id}'.format(product_id=product_id)}, 404
        return product_schema.dump(product)

    @swagger.model
    @swagger.operation(notes='Update product')
    def put(self, product_id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        item = product_schema.load(json_data)
        product = Product.query.filter(Product.product_id == product_id).one_or_none()
        if not product:
            return {"error": 'Product not found with id: {product_id}'.format(product_id=product_id)}, 404
        product.product_name = item['product_name']
        product.product_price = item['product_price']
        product.size = item['size']
        db.session.commit()
        return product_schema.dump(product)

    @swagger.model
    @swagger.operation(notes='Delete product')
    def delete(self, product_id):
        product = Product.query.filter(Product.product_id == product_id).one_or_none()
        if not product:
            return {"error": 'Product not found with id: {product_id}'.format(product_id=product_id)}, 404
        db.session.delete(product)
        db.session.commit()
        return product_schema.dump(product)
