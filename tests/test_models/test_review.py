#!/usr/bin/python3
'''Define unittests'''
from model.city import City
from tests.test_model.test_base_model import test_basemodel

class test_review(test_basemodel):
    ''' '''

    def __init__(self, *args, **kwargs):
        '''  '''
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = "Review"

    def test_place_id(self):
        '''  '''
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        '''  '''
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        ''' '''
        new = self.value()
        self.assertEqual(type(new.text), str)
