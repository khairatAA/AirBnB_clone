"""This is the unittest file for state.py file"""
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
import unittest
import os


class TestState(unittest.TestCase):
    """Run tests for the State class"""

    def setUp(self):
        """Creates a simple object or instance of BaseModel"""
        self.my_model = State()

    def tearDown(self):
        """Clean up method"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_types(self):
        """Test the attribute type"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.name, str)

    def test_str_rep(self):
        """Test the string representation"""
        output = "[State] ({}) {}".format(
            self.my_model.id,
            self.my_model.__dict__
        )
        self.assertEqual(str(self.my_model), output)
