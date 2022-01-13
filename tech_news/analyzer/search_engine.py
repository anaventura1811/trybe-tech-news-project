from tech_news.database import search_news
from tech_news.database import db
import datetime
from re import search


def format_result(result_list):
    return [(doc["title"], doc["url"]) for doc in result_list]


# Requisito 6
def search_by_title(title):
    query = {"title": {'$regex': title, '$options': 'i'}}
    options = {"title": 1, "url": 1, "_id": 0}
    news_list = db.news.find(query, options)
    data = format_result(news_list)
    return data


def validate_date_str(datestring):
    try:
        datetime.datetime.strptime(datestring, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
# Source:
# Sobre validação de datas:
# https://www.codegrepper.com/code-examples/python/how+to+check+if+it+is+a+date+in+any+format+in+python
# https://docs.python.org/3/library/datetime.html#datetime.date


# Requisito 7
def search_by_date(date):
    validate_date_str(date)
    query = {"timestamp": {"$regex": date}}
    news_list = search_news(query)
    data = format_result(news_list)
    return data


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
