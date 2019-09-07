import urllib.request,json
from app import app
from .models import news

Sources = news.Sources

api_key = app.config['API_KEY']

url = app.config['NEWS_API_BASE_URL']

def get_news(sources):
    """
    function that gets response from the api call
    """
    
