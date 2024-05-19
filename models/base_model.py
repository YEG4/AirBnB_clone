#!/usr/bin/python3
"""This file has BaseModel and is inherited by all other classes
"""
import uuid
from datetime import datetime
from .engine.file_storage import FileStorage
storage = FileStorage()


class BaseModel():
    """This is the BaseModel that is used by all other classes
    """
    def __init__(self, *args, **kwargs):
        """This method is automatically called when a new instance is created
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """This method returns the representation of an instance when used
        in a print statement

        Returns:
            fstring: Modelname + id + dict of it's attributes
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This method updates the time when it was last edited and saves
        the instance in a json file
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This method convert the instance.__dict__ into a dict with an
        added attribute
        and modified the created_at and updated_at attribute

        Returns:
            dict: a dictionary of all the attribute of that instance
        """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        mydict = dict(self.__dict__)
        mydict['__class__'] = type(self).__name__
        return mydict
