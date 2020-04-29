import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.highestValuePalindrome('3943', 4, 1), '3993')

    def test_case_1(self):
        self.assertEqual(solution.highestValuePalindrome('092282', 6, 3), '992299')

    def test_case_2(self):
        self.assertEqual(solution.highestValuePalindrome('0011', 4, 1), '-1')


if __name__ == '__main__':
    unittest.main()
