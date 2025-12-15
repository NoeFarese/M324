import unittest
from src.number import is_even

class TestNumber(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(4))

    def test_odd_number(self):
        self.assertFalse(is_even(3))


if __name__ == "__main__":
    unittest.main()
