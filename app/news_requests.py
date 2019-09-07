import urllib.request,json
from app import app
from .models import news

Sources = news.Sources

api_key = app.config['API_KEY']

url = app.config['NEWS_API_BASE_URL']

def get_sources(category):
    """
    function that gets response from the api call
    """
    articles_url = url.format(category, api_key)

    with urllib.request.urlopen(articles_url) as url:
        sources_data = url.read()
        response = json.loads(sources_data)

        sources_outcome = None
        if response['sources']:
            sources_outcome_items = response['sources']
            sources_outcome = process_results(sources_outcome_items)
    return sources_outcome



