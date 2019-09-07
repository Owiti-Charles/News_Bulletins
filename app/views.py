from flask import render_template
from app import app
from .news_requests import get_sources

@app.route('/')
def HomePage():
    """
    Views thats renders the home page
    """
    general_news = get_sources("general")
    business_news = get_sources("business")
    sports_news = get_sources("sports")
    return render_template('sources.html',general_news = general_news,business_news=business_news,sports_news=sports_news )