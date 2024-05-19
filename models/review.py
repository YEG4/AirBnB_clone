#!/usr/bin/python3
'''
    This module describes Review class
'''
from models.base_model import BaseModel


class Review(BaseModel):
    """This class inherits from BaseModel class.

    Args:
        BaseModel (class): Base class for all other classes to inherit from
    """
    place_id = ''
    user_id = ''
    text = ''
