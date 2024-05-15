#!/usr/bin/python3
import cmd
import json
import os, sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        "BaseModel":BaseModel
    }
    file_path = "file.json"
    def emptyline(self):
        pass

    def do_quit(self, line):
        '''Quit command to exit the program\n'''
        return True

    def do_EOF(self, line):
        '''Terminates the console'''
        return True
    
    def do_create(self, cls):
        if cls:
            if cls in self.classes:
                instance = self.classes[cls]()
                instance.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        if os.path.isfile(self.file_path) and self.file_path.endswith(".json"):
            with open(self.file_path, "r") as file:
                instances = json.load(file)
        keys= instances.keys()
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
                        print(f"[{cls}] ({id}) " f"{instances[joined_string]}" )
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
