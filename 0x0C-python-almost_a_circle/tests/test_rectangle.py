#!/usr/bin/python3
"""Unittest for Base() class
"""
import unittest
import io
import sys
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    """Utilizes unittest to evaluate possible outcomes of
    creating instances of Base class
    """
#    def test_value_init1(self):
#        rect_1 = Rectangle(10, 1)
#        self.assertEqual(rect_1.id, 1)

    def test_value_init2(self):
        rect_1 = Rectangle(10, 1)
        self.assertEqual(rect_1.height, 1)

#    def test_value_init3(self):
#        rect_2 = Rectangle(1, 10)
#        self.assertEqual(rect_2.id, 7)

    def test_value_init4(self):
        rect_3 = Rectangle(10, 1, 0, 0, 4)
        self.assertEqual(rect_3.id, 4)

    def test_value_init5(self):
        self.assertRaises(ValueError, Rectangle, 10, -1)

    def test_value_init6(self):
        self.assertRaises(TypeError, Rectangle, 10, "hi")

    def test_value_init7(self):
        self.assertRaises(ValueError, Rectangle, -4, 5)

    def test_value_init8(self):
        self.assertRaises(TypeError, Rectangle, "hi", 10)

    def test_value_init9(self):
        self.assertRaises(TypeError, Rectangle, [1, 2], 8)

    def test_value_init10(self):
        self.assertRaises(ValueError, Rectangle, 10, 2, 3, -1)

    def test_value_init11(self):
        self.assertRaises(TypeError, Rectangle, 10, 2, {})

    def test_value_init12(self):
        self.assertRaises(ValueError, Rectangle, 10, 1, 17, -9)

    def test_value_init13(self):
        self.assertRaises(TypeError, Rectangle, 1, (1, 2), 3)

    def test_value_init14(self):
        rect_4 = Rectangle(2, 3, 1, 1, 1)
        self.assertEqual(rect_4.width, 2)

    def test_value_init15(self):
        self.assertRaises(ValueError, Rectangle, 0, 0)

    def test_value_init16(self):
        with self.assertRaises(TypeError):
            rect_5 = Rectangle(1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_area1(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_area2(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

    def test_area3(self):
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_area4(self):
        with self.assertRaises(ValueError):
            r4 = Rectangle(-1, 9)
            r4.area()

    def test_area5(self):
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 2, 3, 4, 5, 6, 7)
            r5.area()

    def test_display_method1(self):
        if __name__ == "__main__":
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            r1 = Rectangle(4, 6)
            rl.display()
            sys.stdout = sys.__stdout__
            desired = '####\n####\n####\n####\n####\n####'
            print(desired, capturedOutput.getvalue())

    def test_display_method2(self):
        if __name__ == "__main__":
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            r2 = Rectangle(2, 2)
            r2.display()
            sys.stdout = sys.__stdout__
            desired = '##\n##\n'
            print(desired, capturedOutput.getvalue())

    def test_display_method3(self):
        if __name__ == "__main__":
            with self.assertRaises(ValueError):
                capturedOutput = io.StringIO()
                sys.stdout = capturedOutput
                r3 = Rectangle(-1, 2)
                r3.display()
                sys.stdout = sys.__stdout__

    def test_display_method4(self):
        if __name__ == "__main__":
            with self.assertRaises(TypeError):
                capturedOutput = io.StringIO()
                sys.stdout = capturedOutput
                r4 = Rectangle(5, 6, 7, 8, 9, 10, 11)
                r4.display()
                sys.stdout = sys.__stdout__

    def test_str1(self):
        if __name__ == "__main__":
            r1 = Rectangle(4, 6, 2, 1, 12)
            str_r1 = "[Rectangle] (12) 2/1 - 4/6"
            self.assertEqual(print(r1), str_r1)

    def test_str2(self):
        if __name__ == "__main__":
            r2 = Rectangle(5, 5, 1)
            str_r2 = "[Rectangle] (1) 1/0 - 5/5"
            self.assertEqual(print(r2), str_r2)

    def test_str3(self):
        if __name__ == "__main__":
            r3 = Rectangle(1, 2, 3, 4, 5)
            str_r3 = "[Rectangle] (5) 3/4 - 1/2"
            self.assertEqual(print(r3), str_r3)

    def test_str4(self):
        if __name__ == "__main__":
            with self.assertRaises(TypeError):
                r4 = Rectangle(1, 1, 1, 1, 1, 1, 1, 1)

    def test_str5(self):
        if __name__ == "__main__":
            with self.assertRaises(ValueError):
                r5 = Rectangle(-1, 2)

    def test_str6(self):
        if __name__ == "__main__":
            with self.assertRaises(TypeError):
                r6 = Rectangle("hey", "there")

    def test_updated_display1(self):
        if __name__ == "__main__":
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            r1 = Rectangle(2, 3, 2, 2)
            r1.display()
            sys.stdout = sys.__stdout__
            desired = '\n\n  ##\n  ##\n  ##\n'
            print(desired, capturedOutput.getvalue())

    def test_updated_display2(self):
        if __name__ == "__main__":
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            r2 = Rectangle(3, 2, 1, 0)
            r2.display()
            sys.stdout = sys.__stdout__
            desired = ' ###\n ###\n'
            print(desired, capturedOutput.getvalue())

    def test_updated_display3(self):
        if __name__ == "__main__":
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            r3 = Rectangle(3, 2, 0, 1)
            r3.display()
            sys.stdout = sys.__stdout__
            desired = '\n###\n###\n'
            print(desired, capturedOutput.getvalue())

    def test_updated_display4(self):
        if __name__ == "__main__":
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            r4 = Rectangle(3, 2, 0, 0)
            r4.display()
            sys.stdout = sys.__stdout__
            desired = '###\n###\n'
            print(desired, capturedOutput.getvalue())

    def test_update_attribute_method1(self):
        if __name__ == "__main__":
            r1 = Rectangle(10, 10, 10, 10)
            r1_str1 = "[Rectangle] (1) 10/10 - 10/10"
            self.assertEqual(print(r1), r1_str1)

    def test_update_attribute_method12(self):
        if __name__ == "__main__":
            r1 = Rectangle(10, 10, 10, 10)
            r1_str2 = "Rectangle] (89) 10/10 - 10/10"
            self.assertEqual(rl.update(89), r1_str2)

    def test_update_attribute_method3(self):
        if __name__ == "__main__":
            r1 = Rectangle(10, 10, 10, 10)
            r1_str3 = "[Rectangle] (89) 10/10 - 2/10"
            self.assertEqual(r1.update(89, 2), r1_str3)

    def test_update_attribute_method4(self):
        if __name__ == "__main__":
            r1 = Rectangle(10, 10, 10, 10)
            r1_str4 = "[Rectangle] (89) 10/10 - 2/3"
            self.assertEqual(r1.update(89, 2, 3), r1_str4)

    def test_update_attribute_method5(self):
        if __name__ == "__main__":
            r1 = Rectangle(10, 10, 10, 10)
            r1_str5 = "[Rectangle] (89) 4/10 - 2/3"
            self.assertEqual(rl.update(89, 2, 3, 4), r1_str5)

    def test_update_attribute_method6(self):
        if __name__ == "__main__":
            r1 = Rectangle(10, 10, 10, 10)
            r1_str6 = "[Rectangle] (89) 4/5 - 2/3"
            self.assertEqual(rl.update(89, 2, 3, 4, 5), r1_str6)

if __name__ == '__main__':
    unittest.main()