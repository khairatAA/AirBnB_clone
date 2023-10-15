"""This is the unittest file for place.py file"""
from datetime import datetime
from models.place import Place
import unittest
import os


class TestPlace(unittest.TestCase):
    """Run tests for the Place class"""

    def setUp(self):
        """Creates a simple object or instance of Place"""
        self.my_model = Place()

    def tearDown(self):
        """Clean up method"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_types(self):
        """Test the attribute type"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.city_id, str)
        self.assertIsInstance(self.my_model.user_id, str)
        self.assertIsInstance(self.my_model.name, str)
        self.assertIsInstance(self.my_model.description, str)
        self.assertIsInstance(self.my_model.number_rooms, int)
        self.assertIsInstance(self.my_model.number_bathrooms, int)
        self.assertIsInstance(self.my_model.max_guest, int)
        self.assertIsInstance(self.my_model.price_by_night, int)
        self.assertIsInstance(self.my_model.latitude, float)
        self.assertIsInstance(self.my_model.longitude, float)
        self.assertIsInstance(self.my_model.amenity_ids, list)

    def test_str_rep(self):
        """Test the string representation"""
        output = "[Place] ({}) {}".format(
            self.my_model.id,
            self.my_model.__dict__
        )
        self.assertEqual(str(self.my_model), output)
