#!/usr/bin/python3
"""
file_storage module
"""


import json
import os.path
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.city import City
from models.review import Review
from datetime import datetime
import copy


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all: Method that return all the objects of a class

        Returns:
            dictionnary: dictionnary representation of all objects
        """
        return self.__objects

    def new(self, obj):
        """new: method to set in __objects the obj with key <obj class name>.id

        Args:
            obj (object): instance of a class
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        save: Method to save an object to
        a private class attribure __objects
        """
        all_objects = copy.deepcopy(self.__objects)
        for obj_id in all_objects.keys():
            all_objects[obj_id] = all_objects[obj_id].to_dict()
        for key, value in all_objects.items():
            for key1, value1 in value.items():
                if type(value1) is datetime:
                    new_value = copy.deepcopy(value1)
                    f_value = new_value.isoformat()
                    all_objects[key][key1] = f_value
        with open(self.__file_path, "w") as file:
            json.dump(all_objects, file)

    def reload(self):
        """
            reload: method to deserialise an object from an existing file
            then save it to private class attribute __object
        """
        if os.path.isfile(self.__file_path):
            try:
                with open(self.__file_path, "r") as file:
                    content = json.load(file)
                    for key, value in content.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        class_instance = cls(**value)
                        self.__objects[key] = class_instance

            except Exception:
                pass
