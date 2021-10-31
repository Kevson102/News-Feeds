class Article:
  '''
  This is an article class that is used to define and article object.
  '''
  def __init__(self, title, id, author, description, urlToImage, url, publishedAt):
    '''
    Method that initializes an article object
    Args:
      name: The name of the news source
      title: The title of the article
      id: The article id
      author: The author of the article
      description: A brief description of the article
      urlToImage: A link to the article image
      url: A link to the article content.
    '''
    self.title = title
    self.id = id
    self.author = author
    self.description = description
    self.urlToImage = urlToImage
    self.url = url
    self.publishedAt = publishedAt