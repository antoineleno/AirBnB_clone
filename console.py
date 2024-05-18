#!/usr/bin/python3
"""
console module
"""

import cmd
import models
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.city import City
from models.review import Review
from models import storage
import os


class BNBCommand(cmd.Cmd):
    """Console class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_EOF(self, line):
        """Handle End-of-File (EOF) condition to exit the program gracefully"""
        print()
        return True

    def do_create(self, args):
        """Create an instance of a class then save it to json file"""
        if args:
            arguments = args.split()
            class_name = arguments[0]
            if hasattr(globals().get(class_name), '__bases__') \
               and issubclass(globals().get(class_name), BaseModel):

                my_model = globals()[arguments[0]]()
                my_model.save()
                print(my_model.id)
            else:
                print("** class doesn't exist")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """show instance base on id and class name"""
        all_objects = storage.all()
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return

        if len(arguments) < 2:
            print("** instance id missing ** ")
            return

        my_id_dict = {}

        for obj_key in all_objects.keys():
            class_name, obj_id = obj_key.split('.')

            if class_name in my_id_dict.keys():
                my_id_dict[class_name].append(obj_id)
            else:
                my_id_dict[class_name] = [obj_id]

            if class_name == arguments[0] and obj_id == arguments[1]:
                print(all_objects[obj_key])
                return

        if arguments[0] not in my_id_dict.keys():
            print("** class doesn't exist **")
            return

        if arguments[1] not in my_id_dict[arguments[0]]:
            print("** no instance found **")
            return

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        all_objects = storage.all()
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return

        if len(arguments) < 2:
            print("** instance id missing ** ")
            return

        my_id_dict = {}

        try:
            for obj_key in all_objects.keys():
                class_name, obj_id = obj_key.split('.')

                if class_name in my_id_dict.keys():
                    my_id_dict[class_name].append(obj_id)
                else:
                    my_id_dict[class_name] = [obj_id]

                if class_name == arguments[0] and obj_id == arguments[1]:
                    del all_objects[obj_key]
                storage.save()

        except RuntimeError:
            return

        if arguments[0] not in my_id_dict.keys():
            print("** class doesn't exist **")

        if arguments[1] not in my_id_dict[arguments[0]]:
            print("** no instance found **")
            return

    def do_update(self, args):
        """update an instance base class name and id"""
        all_objects = storage.all()
        arguments = args.split()
        if len(arguments) == 0:
            print("** class name missing **")
            return

        if len(arguments) < 2:
            print("** instance id missing ** ")
            return

        if len(arguments) < 3:
            print("** attribute name missing ** ")
            return

        if len(arguments) < 4:
            print("** value missing **")
            return

        my_id_dict = {}

        try:
            for obj_key in all_objects.keys():
                class_name, obj_id = obj_key.split('.')

                if class_name in my_id_dict.keys():
                    my_id_dict[class_name].append(obj_id)
                else:
                    my_id_dict[class_name] = [obj_id]

                if class_name == arguments[0] and obj_id == arguments[1]:
                    try:
                        if type(eval(arguments[3].strip('"'))) in [int, float]:
                            setattr(all_objects[obj_key], arguments[2],
                                    eval(arguments[3].strip('"')))

                    except Exception:
                        setattr(all_objects[obj_key], arguments[2],
                                arguments[3].strip('"'))

                    storage.save()
        except RuntimeError:
            return

        if arguments[0] not in my_id_dict.keys():
            print("** class doesn't exist **")

        if arguments[1] not in my_id_dict[arguments[0]]:
            print("** no instance found **")
            return

    def do_all(self, args):
        """Prints all string representation of all i
        nstances based or not on the class name"""

        all_obj = storage.all()
        all_class_name = []

        for obj_key in all_obj.keys():
            class_name, obj_id = obj_key.split('.')
            all_class_name.append(class_name)

        if args:
            arguments = args.split()
            if arguments[0] not in all_class_name:
                print("** class doesn't exist **")
                return

            list_object = []
            for obj_id in all_obj.keys():
                cls_name, o_id = obj_id.split(".")
                if arguments[0] == cls_name:
                    list_object.append(str(all_obj[obj_id]))
            print(list_object)

        else:
            list_object = []
            for obj_id in all_obj.keys():
                obj = all_obj[obj_id]
                list_object.append(str(obj))
            print(list_object)

    def default(self, line):
        try:
            class_name, command = line.split(".")
        except Exception:
            print("**Not implemented**")
            return

        if hasattr(globals().get(class_name), '__bases__') \
           and issubclass(globals().get(class_name), BaseModel):

            if command == "all()":
                self.onecmd(f'all {class_name}')
            elif command == "count()":
                all_obj = storage.all()
                counter = 0
                for key in all_obj.keys():
                    cls_name, obj_id = key.split(".")
                    if class_name == cls_name:
                        counter += 1
                print(counter)
            elif command[:4] == "show":

                try:
                    garbage1, ob_id, garbage2 = line.split('"')
                    self.onecmd(f'show {class_name} {ob_id}')
                except Exception:
                    pass

            elif command[:7] == "destroy":

                try:
                    garbage1, ob_id, garbage2 = line.split('"')
                    self.onecmd(f'destroy {class_name} {ob_id}')
                except Exception:
                    pass

            elif command[:6] == "update":
                first_split = line.split("{", 1)

                if len(first_split) == 2:
                    split_str = line.split(',', 1)
                    obj_id = split_str[0].split('"')[1]
                    dictionary = split_str[1].rsplit(')', 1)[0]
                    dictionary = eval(dictionary)
                    attr_names = list(dictionary.keys())
                    for i in range(len(attr_names)):
                        self.onecmd(f'update {class_name} {obj_id} \
                            {attr_names[i]} {dictionary[attr_names[i]]}')

                else:
                    try:
                        list_split = []
                        list_split = command.split('"')
                        if len(list_split) == 7:
                            garbage1, obj_id, garbage2, attr_name, garbage3, \
                                attr_value, garbage4 = command.split('"')
                            garbage5, garbage, garbage6 = command.split(", ")
                            attr_value = garbage6.split(")")[0]
                            self.onecmd("update {} {} {} {}".format(class_name,
                                        obj_id, attr_name, attr_value))
                        else:
                            garbage1, obj_id, garbage2, attr_name, \
                                garbage3 = command.split('"')
                            garbage5, garbage, garbage6 = command.split(", ")
                            attr_value = garbage6.split(")")[0]
                            self.onecmd("update {} {} {} {}".format(class_name,
                                        obj_id, attr_name, attr_value))

                    except Exception:
                        pass

            else:
                print("** Not implemented yet **")
        else:
            print("** Class name does not exist **")


if __name__ == '__main__':
    BNBCommand().cmdloop()
