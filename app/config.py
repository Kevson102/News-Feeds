class Config():
  '''
  This is the general configuration class
  '''
  pass

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