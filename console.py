#!/usr/bin/python3
import cmd

"""the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Class that defines the interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        return True

    def help_quit(self):
        print("Quit command that exits the program\n")

    def help_EOF(self):
        print("Quit command that exit the program\n")

    def do_create(self, line):
        pass

    def help_create(self):
        print("Creates a new instance of BaseModel,\
                saves it (to the JSON file) and prints the id")

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
