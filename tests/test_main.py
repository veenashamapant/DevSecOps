import unittest
from fastapi.testclient import TestClient
from main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World"})

    def test_read_item(self):
        response = self.client.get("/items/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"item_id": 1})

if __name__ == "__main__":
    unittest.main()
