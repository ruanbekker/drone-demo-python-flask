import unittest
import server as myapi
import json
import sys

class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = myapi.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(
            json.loads(response.get_data().decode(sys.getdefaultencoding())),
            {"message": "ok"}
        )

if __name__ == '__main__':
    unittest.main()
