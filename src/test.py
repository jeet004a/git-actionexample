from unittest import result
from urllib import response
from app import app
import unittest
class MyTestCase(unittest.TestCase):
    def jack(self):
        result=self.app.get("/")
        self.assertEqual(result.status_code,200)


if __name__=="__main__":
    unittest.main()
