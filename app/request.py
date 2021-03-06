from app import app
import urllib.request,json
from .models import news, articles
from instance import config

News = news.News
Article = articles.Article

# Getting the api key
api_key = config.NEWS_API_KEY

# Getting the news source base url
sources_base_url = app.config['NEWS_SOURCES_API_BASE_URL']
source_base_url = app.config['NEWS_SOURCE_API_BASE_URL']


def get_news_sources():
  '''
  Function that gets the json response to the url request.
  '''
  get_news_source_url = sources_base_url.format(api_key)
    
  with urllib.request.urlopen(get_news_source_url) as url:
    get_news_source_data = url.read()
    get_news_source_response = json.loads(get_news_source_data)
    
    news_source_results = None
    
    if get_news_source_response['sources']:
      news_source_results_list = get_news_source_response['sources']
      news_source_results =  process_source_results (news_source_results_list)
      
  return news_source_results

def process_source_results(news_source_list):
  '''
  function that process the news source results and transforms them into a list of objects.
  Args:
    news_source_list: A list of news source objects
  Returns:
    news_source_results: A list of news source objects
  '''
  news_source_results = []
  for news_source_item in news_source_list:
    id = news_source_item.get('id')
    name = news_source_item.get('name')
    category = news_source_item.get('category')
    
    if id:
      news_source_object = News(id, name, category)
      news_source_results.append(news_source_object)
      
  return news_source_results

def get_news_source_articles(id):
  '''
  Function that gets the json response to the url request.
  '''
  get_news_source_articles_url = source_base_url.format(id,api_key)
  
  with urllib.request.urlopen(get_news_source_articles_url) as url:
    get_news_source_articles_data = url.read()
    get_news_source_articles_response = json.loads(get_news_source_articles_data)
    
    news_source_article_results = None
    
    if get_news_source_articles_response['articles']:
      news_source_article_results_list = get_news_source_articles_response['articles']
      news_source_article_results = process_article_results(news_source_article_results_list)
      
  return news_source_article_results

def process_article_results(news_source_article_list):
  
  news_source_article_results = []
  
  for news_source_article_item in news_source_article_list:
    title = news_source_article_item.get('title')
    id = news_source_article_item.get('id')
    author = news_source_article_item.get('author')
    description = news_source_article_item.get('description')
    image = news_source_article_item.get('urlToImage')
    link = news_source_article_item.get('url')
    publishedAt = news_source_article_item.get('publishedAt')
    
    if image:
      news_source_article_object = Article(title, id, author, description, image, link, publishedAt)
      news_source_article_results.append(news_source_article_object)
  return news_source_article_results