class  News:
  '''
  This is a news class that is used for defining a news object
  '''
  def __init__(self, id, name, category):
    '''
    Method that initializes the News object
    Args:
      id: The id of the news source
      name: The name of the news source
      category: The category of news offered by the source
    '''
    self.id = id
    self.name = name
    self.category = category
    
    