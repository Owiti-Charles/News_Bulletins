from flask import render_template,redirect,request,url_for
from . import main
# from app import app
from ..news_requests import get_sources,get_articles

@main.route('/')
def HomePage():
    """
    Views thats renders the home page
    """
    general_news = get_sources('general')
    business_news = get_sources("business")
    sports_news = get_sources("sports")
    return render_template('sources.html',general=general_news,business=business_news,sports=sports_news )

@main.route('/News-Articles')
def NewsArticles():
    """
    View that would return news articles
     
    """
    health_articles = get_articles('health')
    education_articles = get_articles('technology')
    return render_template('articles.html',health=health_articles, tech =education_articles)