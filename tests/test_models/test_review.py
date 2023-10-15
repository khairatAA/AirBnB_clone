"""This is the unittest file for review.py file"""
from datetime import datetime
from models.review import Review
import unittest
import os


class TestReview(unittest.TestCase):
    """Run tests for the Review class"""

    def setUp(self):
        """Creates a simple object or instance of Review"""
        self.my_model = Review()

    def tearDown(self):
        """Clean up method"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_types(self):
        """Test the attribute type"""
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.place_id, str)
        self.assertIsInstance(self.my_model.user_id, str)
        self.assertIsInstance(self.my_model.text, str)

    def test_str_rep(self):
        """Test the string representation"""
        output = "[Review] ({}) {}".format(
            self.my_model.id,
            self.my_model.__dict__
        )
        self.assertEqual(str(self.my_model), output)
