from models.base_model import BaseModel
import os, json
file_path = "file.json"
classes = {
    "BaseModel": BaseModel
}

if os.path.isfile(file_path) and file_path.endswith(".json"):
            with open(file_path, "r") as file:
                instances = json.load(file)



def func(cls,  id:str):
    print(str(id))
    joined_string = f"{cls}.{id}"
    print(joined_string)

func("Class", 2310-31231-31)
