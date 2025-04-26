test_user_names = {
        'admin': {
            'name': 'Николай Владеев',
            'company': 'Vision Trend',
        },
        'support': {
            'name': 'Анна Поддержкина',
            'company': 'Vision Trend',
        },
        'store': {
            'name': 'Сергей Магазинов',
            'company': 'Оптика Плюс',
        },
        'branch': {
            'name': 'Иван Филиалов',
            'company': 'Оптика Плюс',
            'location': 'ТЦ Мега'
        }
    }


test_role_titles = {
    'admin': 'Владелец',
    'support': 'Сотрудник',
    'store': 'Партнёр',
    'branch': 'Отдел партнёра'
}


test_recent_orders = [
        {'id': '4311', 'status_text': 'Отправлен', 'status_class': 'sent', 'customer': 'Оптика Плюс'},
        {'id': '4299', 'status_text': 'Доставлен', 'status_class': 'delivered', 'customer': 'Линзы и очки'},
        {'id': '4287', 'status_text': 'В обработке', 'status_class': 'processing', 'customer': 'ОчкиМаркет'}
    ]



test_orders = [
        {
            'id': '4311',
            'status_text': 'Отправлен',
            'status_class': 'sent',
            'customer': 'Оптика Плюс',
            'date': '10.03.2025',
            'amount': '150,000'
        },
        {
            'id': '4299',
            'status_text': 'Доставлен',
            'status_class': 'delivered',
            'customer': 'Линзы и очки',
            'date': '25.02.2025',
            'amount': '78,500'
        },
        {
            'id': '4287',
            'status_text': 'В обработке',
            'status_class': 'processing',
            'customer': 'ОчкиМаркет',
            'date': '15.02.2025',
            'amount': '95,200'
        },
        {
            'id': '4265',
            'status_text': 'Одобрен',
            'status_class': 'approved',
            'customer': 'Оптика Центр',
            'date': '01.02.2025',
            'amount': '120,000'
        },
        {
            'id': '4243',
            'status_text': 'Отклонен',
            'status_class': 'rejected',
            'customer': 'СуперОчки',
            'date': '20.01.2025',
            'amount': '65,000'
        }
    ]