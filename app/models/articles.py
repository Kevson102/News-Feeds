class Article:
  '''
  This is an article class that is used to define and article object.
  '''
  def __init__(self, id, author, description, urlToImage, url):
    '''
    Method that initializes an article object
    Args:
      id: The article id
      author: The author of the article
      description: A brief description of the article
      urlToImage: A link to the article image
      url: A link to the article content.
    '''
    self.id = id
    self.author = author
    self.description = description
    self.urlToImage = urlToImage
    self.url = url