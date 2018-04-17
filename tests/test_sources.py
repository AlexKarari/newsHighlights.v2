 import unittest
 from app.models import News_source
 

 class News_sources_Test(unittest.TestCase):
     '''
     Test Class to test the behaviour of the Newssource class

     '''

     def setUp(self):
         '''
         Set up method that will run before every Test

         '''
         self.new_source = News_source(1234,'ABC.com','Tom')

     def test_instance(self):
         self.assertTrue(isinstance(self.new_source,News_sources))



