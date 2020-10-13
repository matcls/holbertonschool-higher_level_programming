#!/usr/bin/python3
"""Summary.
"""
import unittest
from models.base import Base
import json


class TestBase(unittest.TestCase):
    """Summary.
    """

    def test_base(self):
        """Summary.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        self.assertIsInstance(b1, Base)

        b2 = Base()
        self.assertEqual(b2.id, 2)
        self.assertIsInstance(b2, Base)

    def test_ids(self):
        """Summary
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_str(self):
        """Summary
        """
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_uid(self):
        """Summary
        """
        self.assertEqual(4, Base(4).id)

    def test_type(self):
        """Summary
        """
        b1 = Base()
        self.assertTrue(type(b1) == Base)

    def test_nb_objects(self):
        """Summary
        """
        b0 = Base()
        self.assertTrue(hasattr(b0, '_Base__nb_objects'))
        Base._Base__nb_objects = 0

    def test_b_objects_private(self):
        """Summary
        """
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_docstring(self):
        """Summary
        """
        self.assertIsNotNone(Base.__doc__)

    def test_docmodule(self):
        """Summary
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    class TestBaseFunctions(unittest.TestCase):

        """Summary
        """

    def test_init(self):
        """Summary
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertIsInstance(b1, Base)

    def test_id(self):
        """Summary
        """
        Base._Base__nb_objects = 0
        b2 = Base(1)
        self.assertIsNotNone(id(b2))
        self.assertEqual(b2.id, 1)

    def test_id1(self):
        b0 = Base()
        self.assertTrue(hasattr(b0, 'id'))
        Base._Base__nb_objects = 0

    def test_json_string(self):
        """Summary
        """
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 9, "x": 7, "y": 8}
        d2 = {"id": 10, "width": 3, "height": 15, "x": 4, "y": 0}
        json_string = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_string) is str)
        d = json.loads(json_string)
        self.assertEqual(d, [d1, d2])

    def test_empty_json_string(self):
        """Summary
        """
        Base._Base__nb_objects = 0
        json_string = Base.to_json_string([])
        self.assertTrue(type(json_string) is str)
        self.assertEqual(json_string, "[]")

    def test_None_to_json_String(self):
        """Summary
        """
        Base._Base__nb_objects = 0
        json_string = Base.to_json_string(None)
        self.assertTrue(type(json_string) is str)
        self.assertEqual(json_string, '[]')

    def test_from_json_string(self):
        """Summary
        """
        Base._Base__nb_objects = 0
        json_str = '[{"id": 9, "width": 5, "height": 9, "x": 7, "y": 8}, \
                    {"id": 10, "width": 3, "height": 15, "x": 4, "y": 0}]'
        jason_list = Base.from_json_string(json_str)
        self.assertTrue(type(jason_list) is list)
        self.assertEqual(len(jason_list), 2)
        self.assertTrue(type(jason_list[0]) is dict)
        self.assertTrue(type(jason_list[1]) is dict)
        self.assertEqual(jason_list[0],
                         {"id": 9, "width": 5, "height": 9, "x": 7, "y": 8})
        self.assertEqual(jason_list[1],
                         {"id": 10, "width": 3, "height": 15, "x": 4, "y": 0})

    def test_none_to_json(self):
        json_str = Base.to_json_string(None)
        self.assertTrue(type(json_str) is str)
        self.assertEqual(json_str, "[]")

    def test_from_json_string_empty(self):
        """Summary
        """
        self.assertEqual([], Base.from_json_string(""))

    def test_fjs_None(self):
        """Summary
        """
        self.assertEqual([], Base.from_json_string(None))

    def test_json_to_string(self):
        Base._Base__nb_objects = 0
        ob1 = {"id": 12, "width": 4, "height": 3, "x": 8, "y": 12}
        ob2 = {"id": 14, "width": 6, "height": 2, "x": 4, "y": 3}
        json_str = Base.to_json_string([ob1, ob2])
        self.assertTrue(type(json_str) is str)
        ob = json.loads(json_str)
        self.assertEqual(ob, [ob1, ob2])

    def test_more_args(self):
        with self.assertRaises(TypeError):
            b4 = Base(1, 1)

    def test_nb_private(self):
        base = Base(56)
        with self.assertRaises(AttributeError):
            print(base.nb_objects)
        with self.assertRaises(AttributeError):
            print(base.__nb_objects)

    def test_class(self):
        b1 = Base()
        self.assertTrue(isinstance(b1, Base))
