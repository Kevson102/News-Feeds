import unittest
from models import news
News = news.News

class NewsTest (unittest.TestCase):
  '''
  Test case for the behaviour of the News class.
  '''
  def setUp(self):
    '''
    set up method which will be running before every testcase.
    '''
    self.new_news_source = News("ars-technica", "Ars Technica", "technology")
  
  def test_init(self):
    '''
    test instance to check whether the object is initialized as expected
    ''' 
    self.assertEqual(self.new_news_source.id, 'ars-technica')
    self.assertEqual(self.new_news_source.name, 'Ars Technica')
    self.assertEqual(self.new_news_source.category, 'technology')
    
    
if __name__ == '__main__':
  unittest.main()