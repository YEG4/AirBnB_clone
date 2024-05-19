#!/usr/bin/python3
'''
    This module describes User class
'''
from models.base_model import BaseModel


class User(BaseModel):
    """This class inherits from BaseModel class.

    Args:
        BaseModel (class): Base class for all other classes to inherit from
    """
    first_name = ''
    last_name = ''
    email = ''
    password = ''
