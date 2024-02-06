#!/usr/bin/python3
"""This is the base model of the entire AirBnB clone web app"""
import uuid
import datetime

class BaseModel:
    """This class  defines all common attributes and methods for the other classes"""

    def __init__(self, name = None, my_number = None):
        """This runs anytime an object is instantiated"""
        BaseModel.__id = str(uuid.uuid4())
        self.__created_at = datetime.datetime.now()
        self.__updated_at = datetime.datetime.now()
        self.__name = name
        if type(my_number) != int:
            raise TypeError("number must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__my_number = my_number
        self.__name = name
