
import unittest

from app import create_app






class NewsTestRouter(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SECRET_KEY'] = 'your_secret_key'


    def test_add_news_get(self):
        response = self.client.get('/news/add_news')
        self.assertEqual(response.status_code, 302)

    def test_add_news_post(self):
        response = self.client.post('/news/add_news', data={'title': 'test', 'description': 'test'})
        self.assertEqual(response.status_code, 302)

    def test_delete_news_get(self):
        response = self.client.get('/news/delete_news/1')
        self.assertEqual(response.status_code, 302)

    def test_delete_news_post(self):
        response = self.client.post('/news/delete_news/1')
        self.assertEqual(response.status_code, 302)

    def test_edit_news_get(self):
        response = self.client.get('/news/edit_news/1')
        self.assertEqual(response.status_code, 302)
    
    def test_edit_news_post(self):
        response = self.client.post('/news/edit_news/1', data={'title': 'test', 'description': 'test'})
        self.assertEqual(response.status_code, 302)

    def test_get_all_news(self):
        response = self.client.get('/news/all_news')
        self.assertEqual(response.status_code, 200)
    

    def test_get_news_by_id(self):
        response = self.client.get('/news/detailed_news/1')
        self.assertEqual(response.status_code, 200)

    
