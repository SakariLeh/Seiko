
from app.models import NewsModel

from typing import List

from datetime import datetime

"""
временная база данных для новостей
"""

news_db: List[NewsModel] = [
    NewsModel(
        id=1,
        title="test",
        description="""
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Quisquam, quos.
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Quisquam, quos.
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Quisquam, quos.
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Quisquam, quos.
        """,
        created_date=datetime.now(),
        update_date=datetime.now(),
    ),
    NewsModel(
        id=2,
        title="test2",
        description="""
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Quisquam, quos.
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Quisquam, quos.
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Quisquam, quos.
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Quisquam, quos.
        """,
        created_date=datetime.now(),
        update_date=datetime.now(),
    ),
    NewsModel(
        id=3,
        title="test3",
        description="""
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Quisquam, quos.
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Quisquam, quos.
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Quisquam, quos.
        Lorem ipsum dolor sit amet consectetur 
        adipisicing elit. Quisquam, quos.
        """,
        created_date=datetime.now(),
        update_date=datetime.now(),
    ),
]