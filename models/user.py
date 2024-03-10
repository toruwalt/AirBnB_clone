#!/usr/bin/python3
"""This is the model of the User that inherits from BaseModel:"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class  defines all common attributes \n
    and methods for users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
