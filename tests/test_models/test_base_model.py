#!/usr/bin/python3
"""This is the unittest file for base_module.py file"""
from datetime import datetime
from models.base_model import BaseModel
import unittest
"""
Importing the BaseModle class and the unittest
"""


class TestBaseModel(unittest.TestCase):
    """Run tests for the BaseModel class"""

    def setUp(self):
        """Creates a imple object or instance of BaseModel"""
        self.my_model = BaseModel()

    def test_types(self):
        """Test the attribute type"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_str_rep(self):
        """Test the string representation"""
        output = "[BaseModel] ({}) {}".format(
            self.my_model.id,
            self.my_model.__dict__
        )
        self.assertEqual(str(self.my_model), output)

    def test_save(self):
        """Test the save() method method"""
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

        self.my_model.save()

        my_model_json = self.my_model.to_dict()

        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)

    def test_save_updated_at(self):
        """Test if the updated_at updates the time at every update"""
        initial_updated_at = self.my_model.updated_at
        self.my_model.save()
        updated_updated_at = self.my_model.updated_at

        self.assertNotEqual(initial_updated_at, updated_updated_at)

    def test_to_dict(self):
        """Converts the object to_dict
        Checks the types of JSON value
        """
        my_model_dict = self.my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('__class__', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], "BaseModel")
        self.assertEqual(my_model_dict['created_at'], str(
            self.my_model.created_at.isoformat()))
        self.assertEqual(my_model_dict['updated_at'], str(
            self.my_model.updated_at.isoformat()))
