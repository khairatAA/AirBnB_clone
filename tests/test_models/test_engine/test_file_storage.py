#!/usr/bin/python3
"""This is the unittest file for file_storage.py file"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """Run tests for the FileStorage class"""

    def setUp(self):
        """Creates a imple object or instance of FileStorage"""
        self.my_storage = FileStorage()

    def tearDown(self):
        """Clean up method"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_types(self):
        """Test the attribute type"""
        # self.assertIsInstance(self.my_storage.__file_path, str)
        # self.assertIsInstance(self.my_storage.__objec, dict)
        self.assertEqual(type(self.my_storage.all()), dict)

    def test_all_when_its_none(self):
        """Test the all method"""
        self.assertEqual(len(self.my_storage.all()), 12)

    def test_when_a_new_instance_is_created(self):
        """test_when_a_new_instance_is_created"""
        obj = BaseModel()
        self.my_storage.new(obj)
        obj_key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertIn(obj_key, self.my_storage.all())
