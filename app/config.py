class Config():
  '''
  This is the general configuration class
  '''
  NEWS_SOURCES_API_BASE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
  NEWS_SOURCE_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

class ProdConfig(Config):
  '''
  This is the configuration configuration class
  Args:
    Config: The parent configuration class that holds the general configurations
  '''
  pass

class  DevConfig(Config):
  '''
  This is the development configuration class.
  Args:
    Config: The parent configuration class that holds the general configurations
  '''
  DEBUG = True