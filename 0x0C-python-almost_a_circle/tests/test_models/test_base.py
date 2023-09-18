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


if __name__ == "__main__":
    unittest.main()
