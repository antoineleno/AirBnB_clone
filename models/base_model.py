#!/usr/bin/python3
"""
Base model module
"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base model class
        Instance attributes:
            id (str): unique id for each BaseModel
            created_at (date): current datetime when an instance is created
            updated_at (date): current datetime when an instance is created
                     and it will be updated every time you change your object
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor

            Args:
                args: (unused):
                kwargs (dictionary): only the "class" key will not
                        be added as attribute of the object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    time_format = "%Y-%m-%dT%H:%M:%S.%f"
                    if key == "created_at":
                        value = datetime.strptime(value, time_format)
                        setattr(self, key, value)
                    elif key == "updated_at":
                        value = datetime.strptime(value, time_format)
                        setattr(self, key, value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the object
        """
        obj_clas = type(self)
        return "[{}] ({}) {}".format(obj_clas.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        current_time = datetime.now()
        self.updated_at = current_time
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of dict of the instance
        """
        diction = {key: value for key, value in self.__dict__.items()}

        if 'created_at' in diction and \
                isinstance(diction['created_at'], datetime):

            diction['created_at'] = diction['created_at'].isoformat()

        if 'updated_at' in diction and \
                isinstance(diction['updated_at'], datetime):

            diction['updated_at'] = diction['updated_at'].isoformat()

        diction['__class__'] = self.__class__.__name__

        return diction
