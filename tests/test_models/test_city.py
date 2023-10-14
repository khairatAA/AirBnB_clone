"""This is the unittest file for city.py file"""
from datetime import datetime
from models.city import City
import unittest


class TestState(unittest.TestCase):
    """Run tests for the City class"""

    def setUp(self):
        """Creates a simple object or instance of City"""
        self.my_model = City()

    def test_types(self):
        """Test the attribute type"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.name, str)
        self.assertIsInstance(self.my_model.state_id, str)

    def test_str_rep(self):
        """Test the string representation"""
        output = "[City] ({}) {}".format(
            self.my_model.id,
            self.my_model.__dict__
        )
        self.assertEqual(str(self.my_model), output)