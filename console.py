#!/usr/bin/python3
"""Console 
"""
import cmd
import json
import os
import sys
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "State": State,
        "Review": Review
    }
    path = "file.json"

    def emptyline(self):
        pass

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True

    def do_EOF(self, line):
        '''Terminates the console'''
        return True

    def do_create(self, cls):
        """creates new instances
        """
        if cls:
            if cls in self.classes:
                instance = self.classes[cls]()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """lists all class instances stored in a json file

        Args:
            line (string): command line arguements
        """
        if line:
            if line in self.classes:
                if os.path.isfile(self.path) and self.path.endswith(".json"):
                    with open(self.path, "r") as file:
                        instances = json.load(file)
                        my_list = []
                        for key, value in instances.items():
                            if key.startswith(line):
                                key, id = key.split(".", 1)
                                formatted_string = f"[{key}] ({id}) {value}"
                                my_list.append(formatted_string)
                        print(my_list)

            else:
                print("** class doesn't exist **")
        else:
            if os.path.isfile(self.path) and self.path.endswith(".json"):
                with open(self.path, "r") as file:
                    instances = json.load(file)
                    my_list = []
                    for key, value in instances.items():
                        key, id = key.split(".", 1)
                        formatted_string = f"[{key}] ({id}) {value}"
                        my_list.append(formatted_string)
                    print(my_list)

    def do_update(self, line):
        """updates an instance of a class and saves it to a json file

        Args:
            line (string): command line arguements
        """
        if os.path.isfile(self.path) and self.path.endswith(".json"):
            with open(self.path, "r") as file:
                instances = json.load(file)
        line = line.split(" ")
        print(len(line))
        if len(line) == 1 and not line[0]:
            print("** class name missing **")
        elif len(line) == 1:
            if line[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(line) == 2:
            cls = line[0]
            id = line[1]

            if line[0] not in self.classes:
                print("** class doesn't exist **")
                return

            if f"{cls}.{id}" in instances:
                print("** attribute name missing **")
            else:
                print("** no instance found **")

        elif len(line) == 3:
            cls = line[0]
            id = line[1]
            if line[0] not in self.classes:
                print("** class doesn't exist **")
                return
            if f"{cls}.{id}" in instances:
                print("** value missing **")
            else:
                print("** no instance found **")
        elif len(line) >= 4:
            cls = line[0]
            id = line[1]
            if line[0] not in self.classes:
                print("** class doesn't exist **")
                return
            key = f"{cls}.{id}"
            if key in instances:
                instances[key][line[2]] = line[3].strip('\"')
                with open(self.path, "w") as file:
                    json.dump(instances, file, indent=4)
            else:
                print("** no instance found **")

    def do_show(self, line):
        """lists specific class instances

        Args:
            line (string): command line arguements
        """
        if os.path.isfile(self.path) and self.path.endswith(".json"):
            with open(self.path, "r") as file:
                instances = json.load(file)
        keys = instances.keys()
        cls = ''
        id = ''
        # print(type(line))
        if line:
            my_list = line.split(" ", 1)
            # print(my_list)
            if len(my_list) > 1:
                cls = my_list[0]
                id = my_list[1]
            elif len(my_list) == 1:
                cls = my_list[0]
        if cls:
            if cls in self.classes:
                if id:
                    if f"{cls}.{id}" in instances:
                        joined_string = f"{cls}.{id}"
                        print(f"[{cls}] ({id}) " f"{instances[joined_string]}")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """removes a class instance from a json file

        Args:
            line (string): id of the instance to be deleted
        """
        if os.path.isfile(self.path) and self.path.endswith(".json"):
            with open(self.path, "r+") as file:
                instances = json.load(file)
        if line:
            my_list = line.split(' ')
            if len(my_list) > 1:
                cls = my_list[0]
                id = my_list[1]
            elif len(my_list) == 1:
                cls = my_list[0]
                id = ''
        else:
            cls = ''
            id = ''
        if cls:
            if cls in self.classes:
                if id:
                    if f"{cls}.{id}" in instances:
                        joined_string = f"{cls}.{id}"
                        del instances[joined_string]
                        with open(self.path, "w") as file:
                            json.dump(instances, file, indent=4)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
