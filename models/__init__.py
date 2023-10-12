#!/usr/bin/python3
"""
The special init file for running python packages

Initializing our FileStorage class
which calls the reload method, which persists our data objects
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
