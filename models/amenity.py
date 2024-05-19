#!/usr/bin/python3
"""This module Has class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class inherits from BaseModel class.

    Args:
        BaseModel (class): Base class for all other classes to inherit from
    """
    name = ''
