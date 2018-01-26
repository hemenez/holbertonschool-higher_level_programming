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

    def test_value_init3(self):
        """raises value error if negative size"""
        with self.assertRaises(ValueError) as err:
            s1 = Square(-4)
        msg = "width must be > 0"
        self.assertEqual(str(err.exception), msg)

    def test_value_init4(self):
        """raises type error if non number is passed"""
        with self.assertRaises(TypeError) as err:
            s1 = Square("hey")
        msg = "width must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_value_init5(self):
        """raises value error if size of zero is given to square"""
        with self.assertRaises(ValueError) as err:
            s1 = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(err.exception), msg)

    def test_value_init6(self):
        """raises type error if too many values passed"""
        self.assertRaises(TypeError, Square, 2, 4, 6, 8, 10, 12)

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

    def test_display_print2(self):
        """tests if square prints given coordinates"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s2 = Square(3, 1, 3, 3)
        s2.display()
        sys.stdout = sys.__stdout__
        desired = '\n\n\n ###\n ###\n ###\n'
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_update_size_val1(self):
        """tests if size attribute is publicly available"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s1 = Square(5, 0, 0, 1)
        print(s1.size)
        sys.stdout = sys.__stdout__
        desired = '5\n'
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_update_args1(self):
        """tests with no argument given"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s1 = Square(5, 0, 0, 1)
        s1.update()
        print(s1)
        sys.stdout = sys.__stdout__
        desired = "[Square] (1) 0/0 - 5\n"
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_update_args2(self):
        """tests with one argument given as update"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s1 = Square(5, 0, 0, 1)
        s1.update(10)
        print(s1)
        sys.stdout = sys.__stdout__
        desired = "[Square] (10) 0/0 - 5\n"
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_update_args3(self):
        """tests with two args given as update"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s1 = Square(5, 0, 0, 1)
        s1.update(1, 2)
        print(s1)
        sys.stdout = sys.__stdout__
        desired = "[Square] (1) 0/0 - 2\n"
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_update_args4(self):
        """tests if both arg and kwarg are given as update"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s1 = Square(5, 0, 0, 1)
        s1.update(4, x=9)
        print(s1)
        sys.stdout = sys.__stdout__
        desired = "[Square] (4) 0/0 - 5\n"
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_update_args5(self):
        """tests if too many args are passed"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s1 = Square(5, 0, 0, 1)
        s1.update(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
        print(s1)
        sys.stdout = sys.__stdout__
        desired = "[Square] (10) 8/7 - 9\n"
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_update_args6(self):
        """tests if args are assigned given key"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s1 = Square(5, 0, 0, 1)
        s1.update(size=7, y=1, x=12)
        print(s1)
        sys.stdout = sys.__stdout__
        desired = "[Square] (1) 12/1 - 7\n"
        self.assertEqual(capturedOutput.getvalue(), desired)

if __name__ == '__main__':
    unittest.main()
