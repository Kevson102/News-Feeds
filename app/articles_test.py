import unittest
from models import articles
Articles = articles.Article

class NewsTest (unittest.TestCase):
  '''
  Test case for the behaviour of the News class.
  '''
  def setUp(self):
    '''
    set up method which will be running before every testcase.
    '''
    self.new_source_article = Articles("kevson", "kelvin kimani", "technology", "qwertyu", "trewq", '1254')
  
  def test_init(self):
    '''
    test instance to check whether the object is initialized as expected
    ''' 
    self.assertEqual(self.new_source_article.id, 'kevson')
    self.assertEqual(self.new_source_article.author, 'kelvin kimani')
    self.assertEqual(self.new_source_article.description, 'technology')
    self.assertEqual(self.new_source_article.urlToImage, 'qwertyu')
    self.assertEqual(self.new_source_article.url, 'trewq')
    self.assertEqual(self.new_source_article.publishedAt, '1254')
    
    
    
if __name__ == '__main__':
  unittest.main()