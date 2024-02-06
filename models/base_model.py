#!/usr/bin/python3
"""This is the base model of the entire AirBnB clone web app"""
import uuid
import datetime

class BaseModel:
    """This class  defines all common attributes and methods for the other classes"""

    def __init__(self):
        BaseModel.id = str(uuid.uuid4())
        created_at
