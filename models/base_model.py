#!/usr/bin/python3
"""This is the base_model module"""
from datetime import datetime
import uuid
"""
This is the base model of the Airbnb clone project
Import the uuid model
"""


class BaseModel:
    """The base BaseModel class
    The base for the Airbnb clone project
    """

    def __init__(self, *args, **kwargs):
        """The class constructor
        Args:
            args(tuple): arbituary positional arguments
            kwargs(dict): arbituary keyworded arguments
            id(str): assign with an uuid when an instance is created
            created_at: current datetime when an instance is created
            updated_at: current datetime when an instance is created and
            it will be updated every time you change your object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        format = '%Y-%m-%dT%H:%M:%S.%f'

                        setattr(self, key, datetime.strptime(value, format))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """A special method that prints a string"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        custom_dict = self.__dict__.copy()

        custom_dict['__class__'] = self.__class__.__name__
        custom_dict['created_at'] = str(self.created_at.isoformat())
        custom_dict['updated_at'] = str(self.updated_at.isoformat())

        return custom_dict
