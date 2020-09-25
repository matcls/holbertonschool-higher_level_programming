#!/usr/bin/python3
"""Unittest for max_integer([..])

Attributes:
    max_integer (TYPE): Description
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """Summary
    """
    def test_module_docstring(self):
        """Summary
        """
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def test_function_docstring(self):
            """Summary
            """
            self.assertTrue(len(max_integer.__doc__) > 1)

    def test_no_args(self):
        """Summary
        """
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        """Summary
        """
        self.assertIsNone(max_integer([]))

    def test_empty_string(self):
        """Summary
        """
        self.assertEqual(max_integer(""), None)

    def test_max_at_end(self):
        """Summary
        """
        self.assertEqual(max_integer([1, 1, 14, 25, 11, 55]), 55)

    def test_two_of_max(self):
        """Summary
        """
        test = [47, 1, 87, 12, 4, 87]
        self.assertEqual(max_integer(test), 87)

    def test_none(self):
        """Summary
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Summary
        """
        with self.assertRaises(TypeError):
            max_integer([1, "Betty", 3, 4, 5])

    def test_one_element(self):
        """Summary
        """
        self.assertEqual(max_integer([70]), 70)

    def test_max_at_beginning(self):
        """Summary
        """
        self.assertEqual(max_integer([420, 155, 12, 64, 0, 100]), 420)

    def test_max_at_middle(self):
        """Summary
        """
        self.assertEqual(max_integer([1, 10, 23, 30, 14, 12]), 30)

    def test_one_negative(self):
        """Summary
        """
        self.assertEqual(max_integer([14, -14, 5, 6, 4, 3]), 14)

    def test_all_same(self):
        """Summary
        """
        self.assertEqual(max_integer([2, 2, 2, 2, 2, 2]), 2)

    def test_all_negative(self):
        """Summary
        """
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_floats(self):
        """Summary
        """
        self.assertEqual(max_integer([0.1, -2.5, 122.12, 0, 2.3]), 122.12)
if __name__ == "__main__":
    unittest.main()
