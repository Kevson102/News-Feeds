from flask import Flask
from app import app

#Views
@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data.
  '''
  return render_template('index.html')