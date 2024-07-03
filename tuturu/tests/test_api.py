import unittest
from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

class TestMemesAPI(unittest.TestCase):

    def test_read_memes(self):
        response = client.get("/memes")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_read_meme(self):
        response = client.get("/memes/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], 1)

    # Другие тесты для POST, PUT, DELETE
