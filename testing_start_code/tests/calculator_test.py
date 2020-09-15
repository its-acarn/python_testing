import unittest
from src.calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    def _test_add(self):
        self.assertEqual(5, add(2, 3))
