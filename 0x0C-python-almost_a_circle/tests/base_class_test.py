#!/usr/bin/python3
"""Unittest for Base() class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    """Utilizes unittest to evaluate possible outcomes of
    creating instances of Base class
    """
    def test_id_value1(self):
        instance1 = Base()
        self.assertEqual(instance1.id, 1)

    def test_id_value2(self):
        instance2 = Base(10)
        self.assertEqual(instance2.id, 10)

    def test_id_value3(self):
        instance3 = Base(-10)
        self.assertEqual(instance3.id, -10)

    def test_id_value4(self):
        instance4 = Base([1, 2, 3])
        self.assertEqual(instance4.id, [1, 2, 3])

    def test_id_value5(self):
        instance5 = Base("hi")
        self.assertEqual(instance5.id, "hi")

    def test_id_value6(self):
        instance6 = Base()
        self.assertEqual(instance6.id, 2)

    def test_value_of_JSON_string1(self):
        if __name__ == "__main__":
            rectangle_1 = Rectangle(10, 7, 2, 8)
            dictionary = rectangle_1.to_dictionary()
            json_dictionary = Base.to_json_string([dictionary])
            dict_val = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
            self.assertEqual(json_dictionary, dict_val)

    def test_value_of_JSON_string2(self):
        if __name__ == "__main__":
            rectangle_2 = Rectangle()
            dictionary1 = rectangle_2.to_dictionary()
            json_dictionary1 = Base.to_json_string([dictionary1])
            self.assertEqual(json_dictionary1, "[]")

if __name__ == '__main__':
    unittest.main()
