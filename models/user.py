#!/usr/bin/python3
"""
This class helps us create a user
The User class inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """USER CLASS
    This class helps us create a User

    Inherits:
        BaseModel: User class relies on the BaseModel class for it's ID
                   created_at, updated_at, and it's methods

    Class Attributes - PUBLIC:
        email: Holds the email of the user
        password: Holds the password of the user
        first_name: Holds the first name of user
        last_name: Holds the last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
