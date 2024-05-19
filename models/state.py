'''
    This module describes State class
'''
from models.base_model import BaseModel


class State(BaseModel):
    """This class inherits from BaseModel class.

    Args:
        BaseModel (class): Base class for all other classes to inherit from
    """
    name = ''
