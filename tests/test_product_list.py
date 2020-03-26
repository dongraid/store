import json
from tests.base_case import BaseCase


class TestProductList(BaseCase):

    def setUp(self):
        self.payload = [{
            "product_id": 132456,
            "product_price": 5.05,
            "product_name": "Flex",
            "size": 42
        }, {
            "product_id": 132457,
            "product_price": 1000,
            "product_name": "Yeezy",
            "size": 36
        }]
        super().setUp()

    def test_add_products(self):
        response = self.app.post('/products', headers={"Content-Type": "application/json"}, data=json.dumps(self.payload))
        self.assertEqual(200, response.status_code)
        self.assertListEqual(self.payload, response.json)

    def test_get_products(self):
        self.app.post('/products', headers={"Content-Type": "application/json"}, data=json.dumps(self.payload))
        response = self.app.get('/products', headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertListEqual(self.payload, response.json)

    def test_empty_products(self):
        response = self.app.post('/products', headers={"Content-Type": "application/json"}, data=json.dumps([]))
        self.assertEqual(400, response.status_code)
        self.assertEqual('No input data provided', response.json['message'])
