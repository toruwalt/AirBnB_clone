#!/usr/bin/python3
"""Model of the City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines all common attributes for all cities """

    name = ""
    state_id = ""
