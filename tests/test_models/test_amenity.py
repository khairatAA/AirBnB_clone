"""This is the unittest file for amenity.py file"""
from datetime import datetime
from models.amenity import Amenity
import unittest
import os


class TestAmenity(unittest.TestCase):
    """Run tests for the Amenity class"""

    def setUp(self):
        """Creates a simple object or instance of Amenity"""
        self.my_model = Amenity()

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
        output = "[Amenity] ({}) {}".format(
            self.my_model.id,
            self.my_model.__dict__
        )
        self.assertEqual(str(self.my_model), output)
