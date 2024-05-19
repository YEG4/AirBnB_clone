#!/usr/bin/python3
"""This module has all the classes used in the project
BaseModel, State, Place, City, User
"""
from .engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .amenity import Amenity
from .city import City
from .place import Place
from .review import Review
from .state import State


storage = FileStorage()
storage.reload()
