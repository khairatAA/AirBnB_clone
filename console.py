#!/usr/bin/python3
"""This contains the entry point of the command interpreter"""
import cmd
"""Imports the cmd module"""


class HBNBCommand(cmd.Cmd):
    """The class that handles the command line interperter"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """This method is called when the quit is tiggered.
        The program exits in a clean way.
        Args:
        line: the line been read at the moment
        """
        return True

    def help_quit(self):
        """documentation for when 'help quit' is called"""
        print('Quit command to exit the program\n')

    def do_EOF(self, line):
        """This method is called when the EOF is tiggered.
        The program exits in a clean way.
        Args:
        line: the line been read at the moment
        """
        return True

    def help_EOF(self):
        """documentation for when 'help EOF' is called"""
        print('EOF command to exit the program\n')

    def emptyline(self):
        """When an empty line + ENTER shouldn’t
        execute anything
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
