from app import app
import unittest


class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        """Assert that user successfully lands on homepage"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
    
    def test_home_status_code1(self):
        """Assert that user successfully lands on homepage"""
        result = self.app.get('/jeet')
        self.assertEqual(result.status_code, 200)

    


if __name__ == '__main__':
    unittest.main()