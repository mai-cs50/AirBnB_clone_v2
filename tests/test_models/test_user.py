#!/usr/bin/python3
'''Define unittests'''
from model.city import City
from tests.test_model.test_base_model import test_basemodel

class test_User(test_basemodel):
    ''' '''

    def __init__(self, *args, **kwargs):
        '''  '''
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = "User"

    def test_first_name(self):
        '''  '''
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        '''  '''
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        ''' '''
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        ''' '''
        new = self.value()
        self.assertEqual(type(new.password), str)
