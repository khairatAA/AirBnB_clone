#!/usr/bin/python3
""" Review module inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from the BaseModel class
    """
    place_id = ""
    user_id = ""
    text = ""
