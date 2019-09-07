import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    API_KEY=os.environ.get("API_KEY")
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?country=us&category={}&apiKey={}'
