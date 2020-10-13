#!/usr/bin/python3
import unittest
import json
import pep8
import inspect
import io
import os
from contextlib import redirect_stdout
from models import square
from models.base import Base
Square = square.Square


class TestDocs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sq_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_pep8_conformance_square(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstring(self):
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstrings(self):
        for func in self.sq_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class SquareTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)
        cls.s3 = Square(4, 5, 6)
        cls.s4 = Square(7, 8, 9, 10)

    def test_id(self):
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 10)

    def test_size(self):
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 4)
        self.assertEqual(self.s4.size, 7)

    def test_width(self):
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s3.width, 4)
        self.assertEqual(self.s4.width, 7)

    def test_height(self):
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s3.height, 4)
        self.assertEqual(self.s4.height, 7)

    def test_x(self):
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s3.x, 5)
        self.assertEqual(self.s4.x, 8)

    def test_y(self):
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 9)

    def test_area(self):
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 16)
        self.assertEqual(self.s4.area(), 49)

    def test_area_args(self):
        with self.assertRaises(TypeError):
            a = self.s1.area(1)

    def test_basic_display(self):
        s = Square(3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.s1.display()
            output = buf.getvalue()
            self.assertEqual(output, "#\n")
        with io.StringIO() as buf, redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 3 + "\n") * 3)

    def test_size_typeerror(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True)

    def test_x_typeerror(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, True)

    def test_y_typeerror(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, True)

    def test_str(self):
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.s2), "[Square] (2) 3/0 - 2")
        self.assertEqual(str(self.s3), "[Square] (3) 5/6 - 4")
        self.assertEqual(str(self.s4), "[Square] (10) 8/9 - 7")

    def test_update_args(self):
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")
        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 2")
        s.update(89, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 3/0 - 2")
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_update_no_args(self):
        s = Square(1, 0, 0, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_update_kwargs(self):
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(size=10)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")
        s.update(size=11, x=2)
        self.assertEqual(str(s), "[Square] (1) 2/0 - 11")
        s.update(y=3, size=4, x=5, id=89)
        self.assertEqual(str(s), "[Square] (89) 5/3 - 4")

    def test_both_args_kwargs(self):
        s = Square(1, 0, 0, 1)
        s.update(2, 2, 2, 2, size=3, x=3, y=3, id=3)
        self.assertEqual(str(s), "[Square] (2) 2/2 - 2")

    def test_to_dict(self):
        d1 = self.s1.to_dictionary()
        self.assertEqual({"id": 1, "size": 1, "x": 0, "y": 0}, d1)
        d2 = self.s2.to_dictionary()
        self.assertEqual({"id": 2, "size": 2, "x": 3, "y": 0}, d2)
        d3 = self.s3.to_dictionary()
        self.assertEqual({"id": 3, "size": 4, "x": 5, "y": 6}, d3)
        d4 = self.s4.to_dictionary()
        self.assertEqual({"id": 10, "size": 7, "x": 8, "y": 9}, d4)
        self.assertTrue(type(d1) is dict)
        self.assertTrue(type(d2) is dict)
        self.assertTrue(type(d3) is dict)
        self.assertTrue(type(d4) is dict)
        s = Square(1, 1, 1, 1)
        s.update(**d4)
        self.assertEqual(str(s), str(self.s4))
        self.assertNotEqual(s, self.s4)

    def test_create(self):
        s1 = {"id": 2, "size": 3, "x": 4, "y": 0}
        s2 = {"id": 9, "size": 6, "x": 7, "y": 8}
        s1c = Square.create(**s1)
        s2c = Square.create(**s2)
        self.assertEqual("[Square] (2) 4/0 - 3", str(s1c))
        self.assertEqual("[Square] (9) 7/8 - 6", str(s2c))
        self.assertIsNot(s1, s1c)
        self.assertIsNot(s2, s2c)
        self.assertNotEqual(s1, s1c)
        self.assertNotEqual(s2, s2c)

    def test_save_to_file(self):
        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        l = [s1, s2]
        Square.save_to_file(l)
        with open("Square.json", "r") as f:
            ls = [s1.to_dictionary(), s2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_stf_empty(self):
        l = []
        Square.save_to_file(l)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_from_file(self):
        s1 = Square(2, 3, 4, 5)
        s2 = Square(7, 8, 9, 10)
        li = [s1, s2]
        Square.save_to_file(li)
        lo = Square.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        s1c = lo[0]
        s2c = lo[1]
        self.assertTrue(type(s1c) is Square)
        self.assertTrue(type(s2c) is Square)
        self.assertEqual(str(s1), str(s1c))
        self.assertEqual(str(s2), str(s2c))
        self.assertIsNot(s1, s1c)
        self.assertIsNot(s2, s2c)
        self.assertNotEqual(s1, s1c)
        self.assertNotEqual(s2, s2c)
