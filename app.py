from flask import Flask
from flask_restful import Api
from model import db
from flask_restful_swagger import swagger
from healthcheck import HealthCheck
from common.request_logger import start_timer, log_request
from resources.product_list import ProductListResource
from resources.product import ProductResource


app = Flask(__name__)
app.config.from_object('config')
api = Api(app)
api = swagger.docs(Api(app), apiVersion='1', api_spec_url='/docs')
db.init_app(app)

# init healthcheck
health = HealthCheck(app, '/health')

# decorators for request logger
app.before_request = app.before_request(start_timer)
app.after_request = app.after_request(log_request)

# routes
api.add_resource(ProductListResource, '/products')
api.add_resource(ProductResource, '/products/<int:product_id>')

if __name__ == '__main__':
    app.run(debug=True)
