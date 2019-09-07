import urllib.request,json
from app import app
from .models import news

Sources = news.Sources
Articles = news.Articles



def get_sources(category):
    """
    function that gets response from the api call
    """
    api_key = app.config['API_KEY']

    url = app.config['NEWS_API_BASE_URL']
    
    sources_url = url.format(category, api_key)

    with urllib.request.urlopen(sources_url) as url:
        sources_data = url.read()
        response = json.loads(sources_data)

        sources_outcome = None

        if response['sources']:
            sources_outcome_items = response['sources']
            sources_outcome = process_new_sources(sources_outcome_items)
    return sources_outcome

def process_new_sources(sources_list):
    sources_outcome = []

    for one_source in sources_list:
        id = one_source.get("id")
        name = one_source.get("name")
        description = one_source.get("description")
        url = one_source.get("url")
        category = one_source.get("category")
        language = one_source.get("language")
        country = one_source.get("country")
        
        new_source = Sources(id,name,description,url,category,language,country)
        sources_outcome.append(new_source)
    
    return sources_outcome

def get_articles(article):
    
    api_key = app.config['API_KEY']

    url = app.config['NEWS_ARTICLES_APL_URL']

    articles_url = url.format(article,api_key)
    with urllib.request.urlopen(articles_urll) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)

        articles_outcome = None

        if articles_response['articles']:
            articles_outcome_items = articles_response['articles']
            articles_outcome = process_new_articles(articles_outcome_items)
    return articles_outcome

def process_new_articles(articles_list):
    articles_outcome = []

    for one_article in articles_list:
        source = one_article.get("source")
        author = one_article.get("author")
        description = one_article.get("description")
        title = one_article.get("title")
        url = one_article.get("url")
        image_url = one_article.get("image_url")
        publish_time = one_article.get("publish_time")
        
        new_article = Articles(source, author, title, description, url, image_url, publish_time)
        articles_outcome.append(new_source)
    
    return articles_outcome








