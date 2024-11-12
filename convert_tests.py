import convert
import unittest

import keyboard
from convert import str_to_float
from keyboard import gather_numbers


class TestCases(unittest.TestCase):
    # Task 1
    def test_str_to_float(self):
        input = str_to_float('10.56')
        expected = 10.56
        self.assertEqual(expected, input)
    def test_str_to_float2(self):
        input = str_to_float('11122421.624242')
        expected = 11122421.624242
        self.assertEqual(expected, input)
    # Task 2
if __name__ == '__main__':
    unittest.main()