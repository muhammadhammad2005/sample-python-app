#!/usr/bin/env python3
"""
Unit tests for the sample Python application
"""

import unittest
from app import add_numbers, multiply_numbers

class TestApp(unittest.TestCase):
    
    def test_add_numbers(self):
        """Test addition function"""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
    
    def test_multiply_numbers(self):
        """Test multiplication function"""
        self.assertEqual(multiply_numbers(3, 4), 12)
        self.assertEqual(multiply_numbers(-2, 5), -10)
        self.assertEqual(multiply_numbers(0, 10), 0)

if __name__ == '__main__':
    unittest.main()
