#!/usr/bin/python3
"""Unittest for Base() class
"""
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Utilizes unittest to evaluate possible outcomes of
    creating instances of Base class
    """
    def test_value_init1(self):
        """tests initialization value, if id updates"""
        rect_1 = Rectangle(10, 1)
        self.assertEqual(rect_1.id, 22)

    def test_value_init2(self):
        """tests whether height value inits correctly"""
        rect_1 = Rectangle(10, 1)
        self.assertEqual(rect_1.height, 1)

    def test_value_init3(self):
        """tests if id updates correctly"""
        rect_2 = Rectangle(1, 10)
        self.assertEqual(rect_2.id, 29)

    def test_value_init4(self):
        """tests if id inits correctly"""
        rect_3 = Rectangle(10, 1, 0, 0, 4)
        self.assertEqual(rect_3.id, 4)

    def test_value_init5(self):
        """raises value error if negative width/height"""
        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(10, -1)
        msg = "height must be > 0"
        self.assertEqual(str(err.exception), msg)

    def test_value_init6(self):
        """raises type error if non-number"""
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(10, "hi")
        msg = "height must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_value_init7(self):
        """raises value error if negative width/height"""
        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(-4, 5)
        msg = "width must be > 0"
        self.assertEqual(str(err.exception), msg)

    def test_value_init8(self):
        """raises type error if non-number"""
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle("hi", 10)
        msg = "width must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_value_init9(self):
        """raises type error if non-number"""
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle([1, 2], 8)
        msg = "width must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_value_init10(self):
        """raises value error if negative number"""
        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(10, 2, 3, -1)
        msg = "y must be >= 0"
        self.assertEqual(str(err.exception), msg)

    def test_value_init11(self):
        """raises value error if non-number"""
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(10, 2, {})
        msg = "x must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_value_init12(self):
        """raises value error if negative number"""
        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(10, 1, 17, -9)
        msg = "y must be >= 0"
        self.assertEqual(str(err.exception), msg)

    def test_value_init13(self):
        """raises type error if non-number"""
        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(1, (1, 2), 3)
        msg = "height must be an integer"
        self.assertEqual(str(err.exception), msg)

    def test_value_init14(self):
        """tests whether width is initialized correctly"""
        rect_4 = Rectangle(2, 3, 1, 1, 1)
        self.assertEqual(rect_4.width, 2)

    def test_value_init15(self):
        """raises value error if values less than one"""
        self.assertRaises(ValueError, Rectangle, 0, 0)

    def test_value_init16(self):
        """raises type error if too many values passed"""
        with self.assertRaises(TypeError):
            rect_5 = Rectangle(1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_area1(self):
        """checks whether area method calculates correctly"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_area2(self):
        """checks whether area method calculates correctly"""
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

    def test_area3(self):
        """checks whether area method calculates correctly"""
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_area4(self):
        """raises value error if negative value passed"""
        with self.assertRaises(ValueError):
            r4 = Rectangle(-1, 9)
            r4.area()

    def test_area5(self):
        """raises type error if too many values passed"""
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 2, 3, 4, 5, 6, 7)
            r5.area()

    def test_display_method1(self):
        """tests whether display method prints"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(4, 6)
        r1.display()
        sys.stdout = sys.__stdout__
        desired = '####\n####\n####\n####\n####\n####\n'
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_display_method2(self):
        """tests whether display method prints"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r2 = Rectangle(2, 2)
        r2.display()
        sys.stdout = sys.__stdout__
        desired = '##\n##\n'
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_display_method3(self):
        """raises value error if negative value is passed"""
        with self.assertRaises(ValueError):
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            r3 = Rectangle(-1, 2)
            r3.display()
            sys.stdout = sys.__stdout__

    def test_display_method4(self):
        """raises type error if too many values passed"""
        with self.assertRaises(TypeError):
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            r4 = Rectangle(5, 6, 7, 8, 9, 10, 11)
            r4.display()
            sys.stdout = sys.__stdout__

    def test_str1(self):
        """ checks whether string dunder method works"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        sys.stdout = sys.__stdout__
        str_r1 = "[Rectangle] (12) 2/1 - 4/6\n"
        self.assertEqual(capturedOutput.getvalue(), str_r1)

    def test_str2(self):
        """checks whether string dunder method works"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r2 = Rectangle(5, 5, 1, 0, 7)
        print(r2)
        sys.stdout = sys.__stdout__
        str_r2 = "[Rectangle] (7) 1/0 - 5/5\n"
        self.assertEqual(capturedOutput.getvalue(), str_r2)

    def test_str3(self):
        """checks whether string dunder method works"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r3 = Rectangle(1, 2, 3, 4, 5)
        print(r3)
        sys.stdout = sys.__stdout__
        str_r3 = "[Rectangle] (5) 3/4 - 1/2\n"
        self.assertEqual(capturedOutput.getvalue(), str_r3)

    def test_str4(self):
        """raises type error if too many values passed"""
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 1, 1, 1, 1, 1, 1, 1)

    def test_str5(self):
        """raises value error if negative value passed"""
        with self.assertRaises(ValueError):
            r5 = Rectangle(-1, 2)

    def test_str6(self):
        """raises type error if non-number passed"""
        with self.assertRaises(TypeError):
            r6 = Rectangle("hey", "there")

    def test_updated_display1(self):
        """checks whether display method updates properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        desired = '\n\n  ##\n  ##\n  ##\n'
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_updated_display2(self):
        """checks whether display method updates properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        sys.stdout = sys.__stdout__
        desired = ' ###\n ###\n'
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_updated_display3(self):
        """checks whether display method updates properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r3 = Rectangle(3, 2, 0, 1)
        r3.display()
        sys.stdout = sys.__stdout__
        desired = '\n###\n###\n'
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_updated_display4(self):
        """checks whether display method updates properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r4 = Rectangle(3, 2, 0, 0)
        r4.display()
        sys.stdout = sys.__stdout__
        desired = '###\n###\n'
        self.assertEqual(capturedOutput.getvalue(), desired)

    def test_update_attribute_method1(self):
        """checks whether update method updates attributes properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update()
        print(r1)
        sys.stdout = sys.__stdout__
        r1_str1 = "[Rectangle] (10) 10/10 - 10/10\n"
        self.assertEqual(capturedOutput.getvalue(), r1_str1)

    def test_update_attribute_method12(self):
        """checks whether update method updates attributes properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(89)
        print(r1)
        sys.stdout = sys.__stdout__
        r1_str2 = "[Rectangle] (89) 10/10 - 10/10\n"
        self.assertEqual(capturedOutput.getvalue(), r1_str2)

    def test_update_attribute_method3(self):
        """checks whether update method updates attributes properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        print(r1)
        sys.stdout = sys.__stdout__
        r1_str3 = "[Rectangle] (89) 10/10 - 2/10\n"
        self.assertEqual(capturedOutput.getvalue(), r1_str3)

    def test_update_attribute_method4(self):
        """checks whether update method updates attributes properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        print(r1)
        sys.stdout = sys.__stdout__
        r1_str4 = "[Rectangle] (89) 10/10 - 2/3\n"
        self.assertEqual(capturedOutput.getvalue(), r1_str4)

    def test_update_attribute_method5(self):
        """checks whether update method updates attributes properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        print(r1)
        sys.stdout = sys.__stdout__
        r1_str5 = "[Rectangle] (89) 4/10 - 2/3\n"
        self.assertEqual(capturedOutput.getvalue(), r1_str5)

    def test_update_attribute_method6(self):
        """checks whether update method updates attributes properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        print(r1)
        sys.stdout = sys.__stdout__
        r1_str6 = "[Rectangle] (89) 4/5 - 2/3\n"
        self.assertEqual(capturedOutput.getvalue(), r1_str6)

    def test_update_attribute_method6(self):
        """checks whether update method updates attributes properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10, 16)
        r1.update()
        print(r1)
        sys.stdout = sys.__stdout__
        r1_str7 = "[Rectangle] (16) 10/10 - 10/10\n"
        self.assertEqual(capturedOutput.getvalue(), r1_str7)

    def test_update_attribute_method7(self):
        """checks whether update method updates attributes properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(45, 23, 1, 2, 4, 7, 8, 9)
        print(r1)
        sys.stdout = sys.__stdout__
        r1_str8 = "[Rectangle] (45) 2/4 - 23/1\n"
        self.assertEqual(capturedOutput.getvalue(), r1_str8)

    def test_update_attribute_method8(self):
        """raises value error if negative value passed"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(2, -3)

    def test_update_attribute_method9(self):
        """raises type error if non-number passed"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 10, 10, 10)
            r1.update("put", "new")

    def test_update_attribute_method10(self):
        """checks whether update method updates attributes properly"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(42, x=7, y=6)
        print(r1)
        sys.stdout = sys.__stdout__
        r1_str9 = "[Rectangle] (42) 10/10 - 10/10\n"
        self.assertEqual(capturedOutput.getvalue(), r1_str9)

if __name__ == '__main__':
    unittest.main()
