#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5]), -5)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -15, -3]), -3)

    def test_mixed_numbers(self):
        """Test with positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-10, 5, -3, 8]), 8)
        self.assertEqual(max_integer([10, -5, 3, -8]), 10)

    def test_duplicates(self):
        """Test with duplicate numbers"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 1, 2, 2]), 2)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_max_at_beginning(self):
        """Test when max element is at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)
        self.assertEqual(max_integer([100, 50, 25]), 100)

    def test_max_in_middle(self):
        """Test when max element is in the middle"""
        self.assertEqual(max_integer([1, 10, 2]), 10)
        self.assertEqual(max_integer([5, 100, 50]), 100)

    def test_max_at_end(self):
        """Test when max element is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
        self.assertEqual(max_integer([25, 50, 100]), 100)

    def test_two_elements(self):
        """Test with two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([5, 5]), 5)


if __name__ == '__main__':
    unittest.main()
