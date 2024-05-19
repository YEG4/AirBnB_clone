"""This module has all the classes used in the project
BaseModel, State, Place, City, User
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
