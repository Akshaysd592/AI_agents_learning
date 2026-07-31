import unittest
from add import add_two_numbers

class TestAdd(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(1, 2), 3)
        self.assertEqual(add_two_numbers(-1, 1), 0)
        self.assertEqual(add_two_numbers(0, 0), 0)
        self.assertAlmostEqual(add_two_numbers(1.5, 2.5), 4.0)

if __name__ == "__main__":
    unittest.main()
