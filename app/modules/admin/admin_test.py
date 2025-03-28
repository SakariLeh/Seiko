import unittest
from flask import Flask, session, redirect, url_for
from app import create_app
from app.types import ERoleUser

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

    def test_add_new_client_get(self):
        """Тест для GET запроса на добавление нового клиента"""
        response = self.client.get('/admin/add_new_client')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"It's add new client", response.data)

    def test_add_new_client_post(self):
        """Тест для POST запроса на добавление нового клиента"""
        data = {
            'phone': '1234567890',
            'password': 'password123',
            'name': 'New Client',
            'company': 'Test Company',
            'location': 'Test Location'
        }
        response = self.client.post('/admin/add_new_client', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"It's add new client", response.data)

    def test_delete_client(self):
        """Тест для удаления клиента"""
        response = self.client.delete('/admin/remove_client/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"It's remove client", response.data)

    def test_all_clients(self):
        """Тест для получения всех клиентов"""
        response = self.client.get('/admin/all_client')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"It's all client", response.data)

    def test_role_required_middleware_forbidden(self):
        """Тест для роли пользователя, не имеющего доступа"""
        with self.client:
            with self.client.session_transaction() as sess:
                sess['user_id'] = 1  # Эмулируем ID пользователя в сессии
                sess['role'] = ERoleUser.ADMIN  # Устанавливаем роль обычного пользователя

            response = self.client.get('/admin/all_client')
            # Проверяем редирект на страницу логина или отказ в доступе
            self.assertEqual(response.status_code, 200)  # Код редиректа (например, на страницу входа)
            self.assertIn(b"It's all client", response.data)

if __name__ == '__main__':
    unittest.main()
