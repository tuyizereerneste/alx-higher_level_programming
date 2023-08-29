#!/usr/bin/python3
"""Definition of a class Square."""
class Square:
    """Represention a square."""
    def __init__(self, size=0):
        """Initialize a new Square.
        Arguments:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
