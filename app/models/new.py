

import datetime


class NewsModel:
    id: int 
    title: str 
    description: str 

    created_date: datetime.datetime
    update_date: datetime.datetime


    def __init__(self, id: int, title: str, description: str, created_date: datetime.datetime, update_date: datetime.datetime):
        self.id = id
        self.title = title
        self.description = description
        self.created_date = created_date
        self.update_date = update_date