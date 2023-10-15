"""This is the unittest file for amenity.py file"""
from datetime import datetime
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Run tests for the Amenity class"""

    def setUp(self):
        """Creates a simple object or instance of Amenity"""
        self.my_model = Amenity()

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
