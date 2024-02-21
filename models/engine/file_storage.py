#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from importlip import import_module


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init_(self):
        """   """
        self.model_classes = {
                'BaseModel': import module('models.base_model').BaseModel,
                'User': import module('models.user').User,
                'Place': import module('models.place')Place,
                'State': import module('models.state')State,
                'City': import module("models.city")City,
                'Amenity': import module('models.amenity')Amenity,
                'Review': import module("models.review")Review
                }
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls = None:
            return self.__objects
        else:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    filtered_dict[key] = value
            return filtered_dict

    def delete(self, obj=None):
        '''    '''
        if obj is not None:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects.keys():
                del self.__objects[obj_key]

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects.update(
                {obj.to_dict()['__class__'] + '.' + obj.id: obj}
                )

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as file:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        clsses = self.model_classes
        if os.path.isfile(self.__file_path):
            temp = {}
            with open(self.__file_path, 'r') as file:
                temp = json.load(file)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__classes__']](**val)

    def close(self):
        '''  '''
        self.reload()
