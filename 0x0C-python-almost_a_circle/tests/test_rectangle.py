#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        Base._Base__nb_objects = 0

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
    def test_validation(self):
        """
        Test to validate setters
        """
        r0 = Rectangle(-1, 2)
        self.assertRaises(ValueError, setattr, r0, 'width', -1)

    def test_area(self):
        """
        testing area
        """
        r0 = Rectangle(2, 2)
        self.assertEqual(r0.area(), 4)

    def test_display(self):
        r0 = Rectangle(2, 2)
        res = r0.display()
        expected = "##\n##\n"
        self.assertEqual(res, None)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(r1.__str__(), expected)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(1, 2, 3, 4, 5)
        expected = "[Rectangle] (1) 4/5 - 2/3"
        self.assertEqual(str(r1), expected)

    def test_kwargUpdate(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        expected = "[Rectangle] (1) 10/10 - 10/1"
        self.assertEqual(str(r1), expected)

if __name__ == "__main__":
    unittest.main()
