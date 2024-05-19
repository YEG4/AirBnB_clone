#!/usr/bin/python3
"""This module is used for storing class instances in a json file
"""
import json
import os
import ast
from datetime import datetime


class FileStorage():
    """This is the FileStorage class
    which is used to store instances in a json file
    and retrieve it
    """
    __file_path = "file.json"
    __objects = {}

    @staticmethod
    def to_str(obj):
        """This method is used to convert
        a datetime.datetime object into a string format

        Args:
            obj (class): an instance of a class

        Returns:
            obj: an instance of a class after it has been modified to a string
        """
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj

    def all(self):
        """This method is used to list all stored objects

        Returns:
            list: a list of class instances
        """
        return FileStorage.__objects

    def new(self, obj):
        """This method adds new instance to list of objects

        Args:
            obj (class instance): a class instance to be added to the list
        """
        key = f"{type(obj).__name__}.{obj.id}"
        my_dict = obj.__dict__
        my_dict["__class__"] = type(obj).__name__
        FileStorage.__objects[key] = my_dict

    def save(self):
        """This method is used to save instances to a json file
        """
        with open(FileStorage.__file_path, "w") as file:
            for key, value in FileStorage.__objects.items():
                if isinstance(value, str):
                    try:
                        value = ast.literal_eval(value[value.find('{'):])
                    except(SyntaxError, ValueError):
                        return None
                    FileStorage.__objects[key] = value
            json.dump(
                FileStorage.__objects,
                file, default=FileStorage.to_str, indent=4)

    def reload(self):
        """This method is used to retrieve what is inside json file in a list
        """
        if os.path.isfile(FileStorage.__file_path) and \
                FileStorage.__file_path.endswith(".json"):
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = json.load(file)
                for key, value in FileStorage.__objects.items():
                    cls_id = key.split(".")
                    cls = cls_id[0]
                    id = cls_id[1]
                    value['created_at'] = str(
                        datetime.fromisoformat(value['created_at']))
                    value['updated_at'] = str(
                        datetime.fromisoformat(value['updated_at']))
                    FileStorage.__objects[key] = f"[{cls}] ({id}) " \
                        + str(value)
        else:
            return
