from urllib import response
from app import app
import unittest
import requestes

class FlaskAppTest(unittest.TestCase):
    

    def test_home_status_code(self):
        """Assert that user successfully lands on homepage"""
        tester= app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200) 
    
    def test_home_status_code1(self):
        """Assert that user successfully lands on homepage"""
        tester= app.test_client(self)
        response = tester.get('/cloudbuild', content_type='html/text')
        self.assertEqual(response.status_code, 200) 

    


if __name__ == '__main__':
    unittest.main()