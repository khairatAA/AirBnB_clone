#!/usr/bin/python3
"""State module inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """The State class inherits from the BaseClass
    Public attribute:
    name(str): name of string
    """
    name = ""
