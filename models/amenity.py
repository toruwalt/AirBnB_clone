#!/usr/bin/python3
"""Model of the Amenity that inherits from BaseModel:"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines all common attributes for all amenities"""

    name = ""
