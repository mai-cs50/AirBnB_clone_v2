#!/usr/bin/python3
'''Define unittests'''
from model.city import City
from tests.test_model.test_base_model import test_basemodel

class test_City(test_basemodel):
    ''' '''

    def __init__(self, *args, **kwargs):
        '''  '''
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = "City"

    def test_state_id(self):
        '''  '''
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        ''' '''
        new = self.value()
        self.assertEqual(type(new.name), str)
