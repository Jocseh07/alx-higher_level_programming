#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer."""

    def test_empty(self):
        """Test empty list."""
        list = []
        self.assertEqual(max_integer(list), None)

    def test_one(self):
        """Test list with one element."""
        list = [1]
        self.assertEqual(max_integer(list), 1)

    def test_two(self):
        """Test empty list."""
        list = [1, 2]
        self.assertEqual(max_integer(list), 2)

    def test_max_at_end(self):
        """Test max at end."""
        list = [2, 5, 1, 9]
        self.assertEqual(max_integer(list), 9)

    def test_max_at_beginning(self):
        """Test max at beginning."""
        list = [11, 2, 5, 1, 9]
        self.assertEqual(max_integer(list), 11)

    def test_max_at_middle(self):
        """Test max at midde."""
        list = [11, 2, 5, 40, 1, 9]
        self.assertEqual(max_integer(list), 40)

    def test_negative(self):
        """Test precense of negative."""
        list = [11, -2, 5, 40, 1, 9]
        self.assertEqual(max_integer(list), 40)

    def test_only_negative(self):
        """Test only precense of negative."""
        list = [-11, -2, -5, -40, -1, -9]
        self.assertEqual(max_integer(list), -1)


if __name__ == "__main__":
    unittest.main()
