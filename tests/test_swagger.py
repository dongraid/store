from tests.base_case import BaseCase


class TestSwagger(BaseCase):

    def test_docs(self):
        response = self.app.get('/docs.html', headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
