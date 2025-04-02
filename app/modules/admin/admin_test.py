import unittest
from app import create_app


# types 
from app.types import ERoleUser

# models
from app.models.user import User

class TestAdminRoutes(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Создаем приложение для тестирования
        cls.app = create_app()  # Предположим, что у вас есть функция create_app для создания приложения
        cls.client = cls.app.test_client()
        cls.app.config['TESTING'] = True
        cls.app.config['SECRET_KEY'] = 'your_secret_key'

    def setUp(self):
        """Настройка сессии для каждого теста"""
        # Эмулируем контекст запроса с тестовым клиентом
        with self.client:
            # Эмулируем сессию для запросов
            with self.client.session_transaction() as sess:
                sess['user_id'] = 1  # Эмулируем ID пользователя в сессии
                sess['role'] = ERoleUser.ADMIN  # Эмулируем роль администратора

    def tearDown(self):
        """Очистка сессии после каждого теста"""
        with self.client:
            with self.client.session_transaction() as sess:
                sess.clear()

    def test_add_new_partners_get(self):
        """Тест для GET запроса на добавление нового клиента"""
        response = self.client.get('/admin/add_new_partner')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"add_new_partner", response.data)
    
    def test_add_new_partner_post(self):
        """Тест для POST запроса на добавление нового клиента"""
        data = {
            'phone': '998991234100',
            'password': '1234',
            'name': 'Timur',
            'company': 'NabievOptics',
            'location': 'Tashkent',
            'role': ERoleUser.STORE
        }
        
        response = self.client.post('/admin/add_new_partner', data=data)
        self.assertEqual(response.status_code, 302)  # Expecting redirect
        self.assertIn('partner_added_successfully', response.location)

    def test_partner_added_successfully(self):
        """Тест для страницы успешного добавления партнера"""
        response = self.client.get('/admin/partner_added_successfully/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'all_partner', response.data)

    def test_delete_partner_get(self):
        """Тест GET запроса на удаление партнера"""
        response = self.client.get('/admin/delete_partner/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'delete_partner', response.data)

    def test_delete_partner_post(self):
        """Тест POST запроса на удаление партнера"""
        response = self.client.post('/admin/delete_partner/1')
        self.assertEqual(response.status_code, 302)  # Expecting redirect
        self.assertEqual(response.location, '/admin/all_partner')

    def test_edit_partner_get(self):
        """Тест GET запроса на редактирование партнера"""
        response = self.client.get('/admin/edit_partner/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'\xd0\xa0\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c \xd0\xbf\xd0\xb0\xd1\x80\xd1\x82\xd0\xbd\xd0\xb5\xd1\x80\xd0\xb0', response.data)

    def test_all_partners(self):
        """Тест для получения всех партнеров"""
        response = self.client.get('/admin/all_partner')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(partner_data in response.data for partner_data in [
            b'NabievOptics',
            b'delete_partner',
            b'edit_partner'
        ]))

    def test_role_required_middleware_forbidden(self):
        """Тест для роли пользователя, не имеющего доступа"""
        with self.client.session_transaction() as sess:
            sess['user_id'] = 1
            sess['role'] = ERoleUser.STORE

        response = self.client.get('/admin/all_partner')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/dashboard', response.location)

if __name__ == '__main__':
    unittest.main()
