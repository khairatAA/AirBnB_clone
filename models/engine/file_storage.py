#!/usr/bin/env python3
"""
FileStorage class is a simple class and it handles how data is stored & persisted
Within our application
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage Class
    This class attempts to persist data through the serialization and
    deserialization of a Python or JSON string respectively.

    Attributes:
        objects: This is a private instance of the class which holds
                 ALL the instance objects created
        file_path: This is a private instance of the class and depicts
                   The pcath where the data will be stored
    """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns All instance objects saved"""

        return FileStorage.__objects

    def new(self, obj):
        """
        This method populates the __objects dict with objects 
        where key is clase_name_of_instance.id

        Args:
            obj: Object to be saved in __objects dictionary

        Return:
            NIL
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """JSON SERIALIZATION
        This method serialies a Python instance to a JSON representation
        """
        obj_data = FileStorage.__objects
        file_path = FileStorage.__file_path
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(obj_data, json_file)

    def reload(self):
        """JSON DESERIALIZATION
        This method deserializes a JSON string rep. of a Python object
        This object should be transformed back to a Python object

        Raises:
            FileNotFoundError: If file does not exist do nothing
        """
        try:
            file_path = FileStorage.__file_path
            with open(file_path, "r", encoding="utf-8") as json_file:
               FileStorage.__objects = json.load(json_file)
        except FileNotFoundError:
            pass



        
