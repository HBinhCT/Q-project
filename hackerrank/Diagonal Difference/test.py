import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]), 15)


if __name__ == '__main__':
    unittest.main()
