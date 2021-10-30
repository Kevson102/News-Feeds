from flask import render_template
from app import app
from .request import get_news_sources,get_news_source_articles

#Views
@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data.
  '''
  # Getting all the news sources
  news_sources = get_news_sources()
  title = 'Welcome to the most credible news platform | NewsPap'
  return render_template('index.html', title=title, sources = news_sources)

@app.route('/articles/<id>')
def articles(id):
  '''
  View function that returns the news details page and its respective data.
  '''
  articles = get_news_source_articles(id)
  title = 'Source Articles'
  return render_template('articles.html', title=title, articles = articles)