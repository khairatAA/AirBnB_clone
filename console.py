#!/usr/bin/python3
"""This contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """The class that handles the command line interperter"""

    prompt = '(hbnb) '

    class_mapping = {
        'BaseModel': BaseModel
        # Add more class mappings as needed
    }

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        cls_name = args[0]

        if cls_name in self.class_mapping:
            new_instance = self.class_mapping[cls_name]()
            new_instance.save()
            print('{}'.format(new_instance.id))
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """documentation for when 'help create' is called"""
        print('Creates a new instance of BaseModel, saves it')
        print('(to the JSON file) and prints the id\n')

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id"""

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return

        cls_name = args[0]
        instance_id = args[1]

        if cls_name in self.class_mapping:
            instance_key = '{}.{}'.format(cls_name, instance_id)
            all_objs = models.storage.all()

            if instance_key in all_objs:
                obj = all_objs[instance_key]
                print(obj)
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def help_show(self):
        """documentation for when 'help show' is called"""
        print('Prints the string representation of an instance')
        print('based on the class name and id\n')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        cls_name = args[0]
        instance_id = args[1]

        if cls_name in self.class_mapping:
            instance_key = '{}.{}'.format(cls_name, instance_id)
            all_objs = models.storage.all()
            
            if instance_key in all_objs:
                obj = all_objs[instance_key]
                del(all_objs[instance_key])
                self.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")
        
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
