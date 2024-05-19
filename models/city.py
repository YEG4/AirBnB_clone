#!/usr/bin/python3
"""
    This module describes City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class inherits from BaseModel class.

    Args:
        BaseModel (class): Base class for all other classes to inherit from
    """
    name = ''
    state_id = ''
