
# types 
from typing import List

# utils 
import datetime

# models 
from .news_model import NewsModel

# news db 
from app.database import news_db

# получение всех новостей
def get_all_news_service() -> List[NewsModel]:
    return news_db 

# получение новости по id
def get_news_by_id_service(id: int) -> NewsModel | None:
    for news in news_db:
        if news.id == id:
            return news
    return None

# добавление новости
def add_news_service(title: str, description: str, created_date: datetime.datetime, update_date: datetime.datetime) -> NewsModel:
    news = NewsModel(len(news_db) + 1, title, description, created_date, update_date)
    news_db.append(news)
    return news

# удаление новости
def delete_news_service(id: int) -> NewsModel | None:
    for news in news_db:
        if news.id == id:
            news_db.remove(news)
            return news 
    return None

# редактирование новости
def edit_news_service(id: int, title: str, description: str, update_date: datetime.datetime) -> NewsModel | None:
    
    news = get_news_by_id_service(id)

    if news is None:
        return None
    
    news.title = title
    news.description = description
    news.update_date = update_date

    return news



