#!/usr/bin/python3
'''Define unittests'''
from model.amenity import Amenity
from tests.test_model.test_base_model import test_basemodel

class test_State(test_basemodel):
    ''' '''

    def __init__(self, *args, **kwargs):
        '''  '''
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = "State"

    def test_name3(self):
        ''' '''
        new = self.value()
        self.assertEqual(type(new.name), str)
