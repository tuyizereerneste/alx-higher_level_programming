0x0A. Python - Inheritance

TASKS:

1. Write a function that returns the list of available attributes and methods of an object

2. Write a class MyList that inherits from list

3. Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False

4. Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False

5. Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False

6. Write an empty class BaseGeometry

7. Write a class BaseGeometry (based on 5-base_geometry.py).
	Public instance method: def area(self): that raises an Exception with the message area() is not implemented

8. Write a class BaseGeometry (based on 6-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value): that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0

9. Write a class Rectangle that inherits from BaseGeometry

10. Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>

11. Write a class Square that inherits from Rectangle (9-rectangle.py):

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented

12. Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py)
