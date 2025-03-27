
import unittest
from app import create_app  




class AdminRoutesTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app(testing=True)
        cls.client = cls.app.test_client() 

    


if __name__ == '__main__':
    unittest.main()