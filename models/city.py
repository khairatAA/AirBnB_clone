#!/usr/bin/python3
"""City module inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inheritd from the BaseModel class
    Public class attributes:
        state_id(str): it will be the State.id
        name(str): the of the city
    """
    state_id = ""
    name = ""
