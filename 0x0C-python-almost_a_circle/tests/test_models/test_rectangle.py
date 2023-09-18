#!/usr/bin/python3
# test_rectangle.py
"""Defines unittests for models/rectangle.py

Unittest classes:
    TestRectangle_instantiation
    TestRectangle_width
    TestRectangle_height
    TestRectangle_x
    TestRectangle_y
    TestRectangle_area
    TestRectangle_to_dictionary
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the class Rectangle."""

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 8, 0, 0, 4).__width)

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 8, 0, 0, 4).__height)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 8, 0, 0, 4).__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 8, 0, 0, 4).__y)

    def test_width_getter(self):
        r = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 4, 3, 2, 1)
        r.width = 8
        self.assertEqual(8, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(4, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 4, 3, 5, 1)
        r.height = 8
        self.assertEqual(8, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(3, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 4, 3, 2, 1)
        r.x = 8
        self.assertEqual(8, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 4, 3, 2, 1)
        self.assertEqual(2, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 4, 3, 2, 1)
        r.y = 8
        self.assertEqual(8, r.y)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(5, 7, 4, 9)
        r2 = Rectangle(1, 8, 2, 6)
        self.assertEqual(r1.id, r2.id - 1)


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing initialization of
    Rectangle width attribute.
    """

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 3)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(7.5, 3)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 3)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 3)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization
    of Rectangle height attribute.
    """

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, 0)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, 7.5)

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, None)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -2)


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing initialization
    of Rectangle x attribute.
    """

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 3)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 7.5, 3)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 3)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 4, -1, 3)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "Invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 4.5)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 0, -4)


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""
    def test_area(self):
        r = Rectangle(5, 5, 0, 0, 0)
        self.assertEqual(25, r.area())

    def test_area_changed_attributes(self):
        r = Rectangle(5, 5, 1, 1, 1)
        r.width = 10
        r.height = 3
        self.assertEqual(30, r.area())


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary_output(self):
        r = Rectangle(5, 4, 3, 2, 1)
        output = {'x': 3, 'y': 2, 'id': 1, 'height': 4, 'width': 5}
        self.assertDictEqual(output, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
