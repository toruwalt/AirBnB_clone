#!/usr/bin/python3

"""This is the base model of the entire AirBnB clone web app"""
import uuid
import datetime
from datetime import datetime as dateTime


class BaseModel:

    """This class  defines all common attributes \n
    and methods for the other classes"""

    def __init__(self, name="", my_number=0):
        """This runs anytime an object is instantiated"""
        self.__id = str(uuid.uuid4())
        self.__created_at = dateTime.now()
        self.__updated_at = dateTime.now()

    def __str__(self):
        """This is the string representation of the object"""
        """[<class name>] (<self.id>) <self.__dict__>"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.__id, self.__dict__))

    def save(self):
        self.__created_at = dateTime.now()

    def to_dict(self):
        self.__created_at = self.__created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__updated_at = self.__updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        new__dict = {}
        for key, value in self.__dict__.items():
            new__dict[key] = value
            new__dict["__class__"] = self.__class__.__name__
        return new__dict
