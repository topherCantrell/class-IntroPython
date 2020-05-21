import unittest

class TestSomeStuff(unittest.TestCase):
    
    def setUp(self):
        print('IN SETUP')
        self.data = {'name' : 'chris', 'cool' : True}
        
    def tearDown(self):
        print('IN TEARDOWN')
    
    def test_one(self):
        print('here in one')
    
    def test_two(self):
        print('here in two')
        n = self.data['name']
        print('I see name is',n)
    
    def test_even_more(self):
        print('here in even more')
    