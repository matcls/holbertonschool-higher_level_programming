#!/usr/bin/python3
"""Summary."""
import json


class Base:
    """Summary."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Summary."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Summary."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Summary."""
        lists = []
        if list_objs is not None:
            for i in list_objs:
                lists.append(i.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(lists))

    @staticmethod
    def from_json_string(json_string):
        """Summary."""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Summary."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Summary."""
        file = str(cls.__name__) + ".json"
        try:
            with open(file, "r") as f:
                data = cls.from_json_string(f.read())
                return [cls.create(**i) for i in data]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Summary."""
        lists = []
        if len(list_objs) is not 0:
            for i in list_objs:
                lists.append(i.to_dictionary())
        with open(cls.__name__ + ".csv", "w+") as f:
            f.write(cls.to_json_string(lists))

    @classmethod
    def load_from_file_csv(cls):
        """Summary."""
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                cvs = Base.from_json_string(f.read())
                lists = []
                for i in cvs:
                    lists.append(cls.create(**i))
                return lists
        except IOError:
            return []
