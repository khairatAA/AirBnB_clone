#!/usr/bin/python3
""" Amenity module inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inheritd from the BaseModel class
    Public class attributes:
        name(str): the of the Amenity
    """

    name = ""
