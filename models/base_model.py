#!/usr/bin/python3
"""This is the base model of the entire AirBnB clone web app"""
import uuid
import datetime
from datetime import datetime as dateTime
import models


class BaseModel:
    """This class  defines all common attributes \n
    and methods for the other classes"""

    def __init__(self, *args, **kwargs):
        """This runs anytime an object is instantiated"""

        self.id = str(uuid.uuid4())
        self.created_at = dateTime.now()
        self.updated_at = dateTime.now()

        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.__dict__["created_at"] = dateTime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = dateTime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            models.storage.new(self)

    def __str__(self):
        """This is the string representation of the object"""
        """[<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.updated_at = dateTime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dict of all keys/values of __dict__ of the instance"""
        new__dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                value = value.isoformat()
            new__dict[key] = value
            new__dict["__class__"] = self.__class__.__name__
        return new__dict
