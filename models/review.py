#!/usr/bin/python3
"""Model of the Review that inherits from BaseModel:"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines all common attributes for all reviews"""

    place_id = ""
    user_id = ""
    text = ""
