import json
from tests.base_case import BaseCase


class TestHealth(BaseCase):

    def test_healthcheck(self):
        response = self.app.get('/health', headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertEqual('success', response.json["status"])
