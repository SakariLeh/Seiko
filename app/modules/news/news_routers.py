
# flask 
from flask import Blueprint, render_template, request, redirect, url_for

# config 
from .news_config import newsConf

# types 
from app.types import ERoleUser
from app.types import EMethod

# middlewares
from app.middlewares import role_required_middleware

# services 
from .news_service import get_all_news_service
from .news_service import get_news_by_id_service
from .news_service import add_news_service
from .news_service import delete_news_service
from .news_service import edit_news_service

# utils 
from datetime import datetime

news_bp = Blueprint("news", __name__)


@news_bp.route(
    newsConf.r.get_path("Получение всех новостей"),
    methods = newsConf.r.get_methods("Получение всех новостей")
)
def all_news():

    news = get_all_news_service()

    return render_template(newsConf.r.get_temp("Получение всех новостей"), news=news)


@news_bp.route(
    newsConf.r.get_path("Подробная новость"),
    methods = newsConf.r.get_methods("Подробная новость")
)
def detailed_news(id: int):

    news = get_news_by_id_service(id)

    return render_template(newsConf.r.get_temp("Подробная новость"), news=news)


@news_bp.route(
    newsConf.r.get_path("Добавление новой новости"),
    methods = newsConf.r.get_methods("Добавление новой новости")
)
@role_required_middleware(ERoleUser.ADMIN)
def add_news():

    if request.method == EMethod.POST:
        title = request.form["title"]
        description = request.form["description"]
        created_date = datetime.now()
        update_date = datetime.now()
        add_news_service(title, description, created_date, update_date)

        return redirect(url_for("news.all_news"))

    return render_template(newsConf.r.get_temp("Добавление новой новости"))


@news_bp.route(
    newsConf.r.get_path("Удаление новости"),
    methods = newsConf.r.get_methods("Удаление новости")
)
@role_required_middleware(ERoleUser.ADMIN)
def delete_news(id: int):

    if request.method == EMethod.POST:
        delete_news_service(id)
        return redirect(url_for("news.all_news"))

    

    return render_template(newsConf.r.get_temp("Удаление новости"), id=id)


@news_bp.route(
    newsConf.r.get_path("Изменения новости"),
    methods = newsConf.r.get_methods("Изменения новости")
)
@role_required_middleware(ERoleUser.ADMIN)
def edit_news(id: int):

    if request.method == EMethod.POST:
        title = request.form["title"]
        description = request.form["description"]
        update_date = datetime.now()
        edit_news_service(id, title, description, update_date)

        return redirect(url_for("news.all_news"))

    news = get_news_by_id_service(id)


    return render_template(newsConf.r.get_temp("Изменения новости"), news = news)







