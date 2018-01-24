#!/usr/bin/python3
"""Unittest for Base() class
"""
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Utilizes unittest to evaluate possible outcomes of
    creating instances of a Square class
    """
    def test_value_init1(self):
        """tests initialization val, if id updates"""
        sq_1 = Square(5, 2, 1, 1)
        self.assertEqual(sq_1.id, 1)

    def test_value_init2(self):
        """tests initialization with three values"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s2 = Square(3, 1, 3, 3)
        print(s2)
        sys.stdout = sys.__stdout__
        desired = "[Square] (3) 1/3 - 3\n"
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_area1(self):
        """tests if area of square is calculated correctly"""
        sq_1 = Square(5)
        self.assertEqual(sq_1.area(), 25)

    def test_display_print1(self):
        """tests if square is printed properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        sq_1 = Square(2)
        sq_1.display()
        sys.stdout = sys.__stdout__
        desired = '##\n##\n'
        self.assertEqual(capturedOutput.getvalue(), desired)

if __name__ == '__main__':
    unittest.main()
