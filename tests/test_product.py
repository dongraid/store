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
        self.app.post('/products', headers={"Content-Type": "application/json"}, data=json.dumps(self.payload))

    def test_update_product(self):
        response = self.app.get('/products/132457', headers={"Content-Type": "application/json"})
        response.json['product_name'] = 'Phone'
        self.app.put('/products/132457', headers={"Content-Type": "application/json"}, data=json.dumps(response.json))
        response = self.app.get('/products/132457', headers={"Content-Type": "application/json"},
                                data=json.dumps(response.json))
        self.assertEqual(200, response.status_code)
        self.assertEqual('Phone', response.json['product_name'])

    def test_get_product(self):
        response = self.app.get('/products/132457', headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json in self.payload)

    def test_delete_product(self):
        response = self.app.delete('/products/132457', headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.json in self.payload)

    def test_wrong_id(self):
        response = self.app.get('/products/111111', headers={"Content-Type": "application/json"})
        self.assertEqual(404, response.status_code)
        self.assertEqual('Product not found with id: 111111', response.json['error'])
