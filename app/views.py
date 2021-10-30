from flask import render_template
from app import app
from .request import get_news_sources

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

@app.route('/news/<int:news_id>')
def news(news_id):
  '''
  View function that returns the news details page and its respective data.
  '''
  title = 'Headline Description'
  return render_template('news.html', id = news_id, title=title)