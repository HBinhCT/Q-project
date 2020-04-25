import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]), 5)


if __name__ == '__main__':
    unittest.main()
