#!/usr/bin/python3
"""This is the model of the User that inherits from BaseModel:"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class  defines all common attributes \n
    and methods for users"""


    def __init__(self, email="", password="", first_name="", last_name=""):
        """This runs anytime an object is instantiated"""
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

        
