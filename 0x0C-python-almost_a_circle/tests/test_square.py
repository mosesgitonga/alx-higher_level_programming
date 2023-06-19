#!/usr/bin/python3
"""Unittest Square
Test cases for the class Square.
"""

import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """class TestSquare that inherits from unittest.TestCase"""

    def test_3_0(self):
        s0 = Square(5)
        self.assertEqual(s0.size, 5)
        self.assertEqual(s0.id, 2)
        self.assertEqual(s0.x, 0)
        self.assertEqual(s0.y, 0)

    def test_3_1(self):
        """class TestSquare: checks for __str__representation."""

        s1 = Square(3, 2, 1, 5)
        self.assertEqual(str(s1), "[Square] (5) 2/1 - 3")

    def test_3_2(self):
        """class TestSquare: checks for inheritence."""

        s1 = Square(3)
        self.assertTrue(isinstance(s1, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(s1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    def test_3_3(self):
        """class TestSquare: checks for missing args."""

        with self.assertRaises(TypeError) as x:
            s1 = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'", str(
                x.exception))

    def test_3_4(self):
        """Test for methods inherited from Rectangle."""

        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(3, 1, 3)
        s2.update(8)
        self.assertEqual(s2.id, 8)
        f = io.StringIO()
        s3 = Square(3)
        with contextlib.redirect_stdout(f):
            s3.display()
        s = f.getvalue()
        res = "###\n###\n###\n"
        self.assertEqual(s, res)

    def test_3_5(self):
        """class TestSquare: checks for size attribute."""

        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s2 = Square(3, 2, 4, 7)
        self.assertEqual(s2.size, 3)

    def test_3_10(self):
        """Test for public method to_dictionary with wrong args."""
        s = "to_dictionary() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as x:
            s1 = Square(10, 2, 1, 9)
            s1_dictionary = s1.to_dictionary("Hi")
        self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
