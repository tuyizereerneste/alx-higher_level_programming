#!/usr/bin/python3
"""Defines unittests for base.py
Unittest classes:
    TestBase_instantiation
    TestBase_create
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_id_public(self):
        b = Base(10)
        b.id = 9
        self.assertEqual(9, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(10).__nb_instances)

    def test_float_id(self):
        self.assertEqual(7.5, Base(7.5).id)

    def test_str_id(self):
        self.assertEqual("invalid", Base("invalid").id)

class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method."""
    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""
    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""
    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 60, "width": 20, "height": 7, "x": 3}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))


if __name__ == "__main__":
    unittest.main()
