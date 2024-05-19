import json
import os
import ast
from datetime import datetime


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    @staticmethod
    def to_str(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj
    
    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        my_dict = obj.__dict__
        my_dict["__class__"] = type(obj).__name__
        FileStorage.__objects[key] = my_dict

    def save(self):
        with open(FileStorage.__file_path, "w") as file:
            for key,value in FileStorage.__objects.items():
                if isinstance(value, str):
                    try:
                        value = ast.literal_eval(value[value.find('{'):])
                    except(SyntaxError, ValueError):
                        return None
                    FileStorage.__objects[key] = value
            json.dump(FileStorage.__objects, file, default= FileStorage.to_str, indent=4)
    
    def reload(self):
        if os.path.isfile(FileStorage.__file_path) and FileStorage.__file_path.endswith(".json"):
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = json.load(file)
                for key,value in FileStorage.__objects.items():
                    cls_id = key.split(".")
                    cls = cls_id[0]
                    id = cls_id[1]
                    value['created_at'] = str(datetime.fromisoformat(value['created_at']))
                    value['updated_at'] = str(datetime.fromisoformat(value['updated_at']))
                    FileStorage.__objects[key] = f"[{cls}] ({id}) " + str(value)
        else:
            return 