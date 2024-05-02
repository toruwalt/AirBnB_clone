#!/usr/bin/python3
"""Model of the Place that inherits from BaseModel:"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines all common attributes for all places"""

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = 0
