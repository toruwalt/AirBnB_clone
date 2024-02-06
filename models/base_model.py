#!/usr/bin/python3

"""This is the base model of the entire AirBnB clone web app"""
import uuid
import datetime


class BaseModel:

    """This class  defines all common attributes \n
    and methods for the other classes"""

    def __init__(self, name=None, my_number=None):
        """This runs anytime an object is instantiated"""
        self.__id = str(uuid.uuid4())
        self.__created_at = datetime.datetime.now()
        self.__updated_at = datetime.datetime.now()
        if type(name) != str:
            raise TypeError("name must be a string")
        else:
            self.__name = name
        if type(my_number) != int:
            raise TypeError("name must be a string")
        elif my_number <= 0:
            raise ValueError("number must be greater than 0")
        else:
            self.__my_number = my_number

    @property
    def id(self):
        return self.__id

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__id

    @property
    def name(self):
        """This is the getter of the name property"""
        return self.__name

    @name.setter
    def name(self, input):
        """This is the setter of the name porperty"""
        if type(input) != str:
            raise TypeError("name must be a string")
        else:
            self.__name = input

    @property
    def my_number(self):
        """This is the getter of the name property"""
        return self.__my_number

    @my_number.setter
    def my_number(self, value_number):
        """This is the setter of the name porperty"""
        if type(value_number) != int:
            raise TypeError("name must be a string")
        elif value_number <= 0:
            raise ValueError("number must be greater than 0")
        else:
            self.__my_number = value_number
