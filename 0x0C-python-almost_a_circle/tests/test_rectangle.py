#!/usr/bin/python3
import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.Rectangle = Rectangle
        self.Rectangle._Base__nb_objects = 0

    def test_rectangle(self):
        """
        Test the Rectangle class functionality.
        """
        r0 = Rectangle(10, 2)
        self.assertEqual(r0.id, 1)

        r1 = Rectangle(10, 2, 0, 0, 23)
        self.assertEqual(r1.id, 23)

        r2 = Rectangle(23, 3, 5)
        self.assertEqual(r2.id, 2)


if __name__ == "__main__":
    unittest.main()
