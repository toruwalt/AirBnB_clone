#!/usr/bin/python3
import re
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

"""the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Class that defines the interpreter"""
    prompt = '(hbnb) '
    obj = ''
    all_classes = {"BaseModel"}

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True

    def help_quit(self):
        """Help doc for quit function"""
        print("Quit command that exits the program\n")

    def help_EOF(self):
        """Help for the EOF function"""
        print("Quit command that exit the program\n")

    def do_create(self, line):
        """Creates a new instance of BaseModel,\
                saves it (to the JSON file) and prints the id"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif len(args) > 1:
            pass
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            line = BaseModel()
            print(line.id)
            storage.save()

    def help_create(self):
        """Help doc for create function"""
        print("Creates a new instance of BaseModel,\
                saves it (to the JSON file) and prints the id")

    def do_show(self, line):
        """Prints string of an instance based on the class name and id"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            command = args[1]
            key = "{}.{}".format(args[0], command)
            all_objs = storage.all()
            if key in all_objs.keys():
                obj = all_objs[key]
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            command = args[1]
            key = "{}.{}".format(args[0], command)
            all_objs = storage.all()
            if key in all_objs.keys():
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name"""
        all_in_list = []
        args = line.split()
        if not line:
            all_objs = storage.all()
            for key in all_objs.keys():
                obj = str(all_objs[key])
                all_in_list.append(obj)
            print(all_in_list)
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            print("Comeback when you have User, Review, Amenities, etc.")

    def help_all(self):
        """Help doc for create function"""
        print("Prints all string representation of all \
                instances based or not on the class name.")

    def do_update(self, line):
        """Adds or updates attribute (save the change into the JSON file)."""
        args = line.split()
        all_objs = storage.all()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            key = "{}.{}".format(args[0], args[1])
            if key not in all_objs.keys():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
            return False
        elif len(args) == 3:
            print("** value missing **")
        else:
            new_attr = args[3][1:-1]
            key = "{}.{}".format(args[0], args[1])
            setattr(all_objs[key],args[2],new_attr)
            storage.save()

    def emptyline(self):
        """Outputs when the line is empty"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
