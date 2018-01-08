#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Utilizes unittest to evaluate max_integer module
    """
    def outcome_pos_ints(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def outcome_neg_ints(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def outcome_duplicate_numbers(self):
        self.assertEqual(max_integer([9, 8, 7, 7], 7))

    def outcome_empty_list(self):
        self.assertEqual(max_integer([None]), None)

    def test_if_string(self):
        self.assertNotIsInstance(max_integer("hi"), int)

    def test_if_no_parameter(self):
        self.assertEqual(max_integer(), None)

    def test_if_list_empty(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
