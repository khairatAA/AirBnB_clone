#!/usr/bin/python3
"""This contains the entry point of the command interpreter"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """The class that handles the command line interperter"""

    prompt = '(hbnb) '

    class_mapping = {
        'BaseModel': BaseModel,
        'User': User
        # Add more class mappings as needed
    }

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        cls_name = args[0]

        if cls_name in HBNBCommand.class_mapping:
            new_instance = HBNBCommand.class_mapping[cls_name]()
            print('{}'.format(new_instance.id))
            new_instance.save()
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

        if cls_name in HBNBCommand.class_mapping:
            instance_key = '{}.{}'.format(cls_name, instance_id)
            all_objs = models.storage.all()

            if instance_key in all_objs.keys():
                obj = all_objs[instance_key]
                print(obj)
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def help_show(self):
        """documentation for when 'help show' is called"""
        print("\n".join([
            "Usage: show [class_name e.g User] [id]",
            "Prints the string representation of an instance",
            "based on the class name and id"]))

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

        if cls_name in HBNBCommand.class_mapping:
            instance_key = '{}.{}'.format(cls_name, instance_id)
            all_objs = models.storage.all()

            if instance_key in all_objs.keys():
                del models.storage.all()[instance_key]
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def help_destroy(self):
        """documentation for when 'help destroy' is called"""
        print('Deletes an instance based on the class name and id '
              '(save the change into the JSON file).\n')

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name."""
        args = line.split()

        all_objs = models.storage.all()

        all_objs_list = []
        if not line:
            for obj in all_objs.values():
                all_objs_list.append(str(obj))
            print(all_objs_list)
            return

        cls_name = args[0]
        if cls_name not in HBNBCommand.class_mapping:
            print("** class doesn't exist **")
            return

        specific_objs_list = []
        for obj in all_objs.values():
            if type(obj).__name__ == cls_name:
                specific_objs_list.append(str(obj))
        print(specific_objs_list)

    def help_all(self):
        """documentation for when 'help all' is called"""
        print('Prints all string representation of all instances based '
              'or not on the class name.\n')

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not line:
            print("** class name missing **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        cls_name = args[0]

        if cls_name not in HBNBCommand.class_mapping:
            print("** class doesn't exist **")
            return

        instance_id = args[1]

        instance_key = '{}.{}'.format(cls_name, instance_id)
        all_objs = models.storage.all()

        if instance_key not in all_objs.keys():
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        attribute_type = type(eval(attribute_value))

        if attribute_type not in (str, int, float):
            return
        setattr(all_objs[instance_key], attribute_name, eval(attribute_value))
        models.storage.save()

    def help_update(self):
        """documentation for when 'help update' is called"""
        print('Updates an instance based on the class name and '
              'id by adding or updating attribute (save the '
              'change into the JSON file).'
              'Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com" \n'
              )

    def do_quit(self, line):
        """This method is called when the quit is tiggered.
        The program exits in a clean way.
        Args:
        line: the line been read at the moment
        """
        print()
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
        print()
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
    HBNB_instance = HBNBCommand()

    if HBNB_instance.stdin.isatty():
        HBNB_instance.cmdloop()
    else:
        while True:
            try:
                command = input("(hbnb)\n")
            except EOFError:
                break
            HBNB_instance.onecmd(command)
            