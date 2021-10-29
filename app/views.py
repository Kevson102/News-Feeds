from flask import render_template
from app import app

#Views
@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data.
  '''
  title = 'Welcome to the most credible news platform | NewsPap'
  return render_template('index.html', title=title)

@app.route('/news/<int:news_id>')
def news(news_id):
  '''
  View function that returns the news details page and its respective data.
  '''
  title = 'Headline Description'
  return render_template('news.html', id = news_id, title=title)