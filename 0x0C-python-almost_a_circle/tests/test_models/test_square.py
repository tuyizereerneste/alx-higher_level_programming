#!/usr/bin/python3
# test_square.py
"""Defines unittests for models/square.
Unittest classes:
    TestSquare_instantiation
    TestSquare_size
    TestSquare_x
    TestSquare_y
    TestSquare_area
    TestSquare_to_dictionary
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(8), Base)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        s = Square(1, 2, 3, 4)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(1, 2, 3, 4)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)


class TestSquare_size(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(7.5)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 3)

    def test_str_size(self):
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Square("invalid", 3)


class TestSquare_x(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, 7.5)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "invalid")

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -2, 0)


class TestSquare_y(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 7.5)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "invalid")

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 0, -2)


class TestSquare_area(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    def test_area(self):
        self.assertEqual(25, Square(5, 0, 0, 1).area())

    def test_area_changed_attributes(self):
        s = Square(3, 0, 0, 2)
        s.size = 4
        self.assertEqual(16, s.area())


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        s = Square(10, 2, 1, 1)
        output = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())


if __name__ == "__main__":
    unittest.main()
