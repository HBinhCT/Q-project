import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.highestValuePalindrome('3943', 4, 1), '3993')

    def test_case_1(self):
        self.assertEqual(my_code.highestValuePalindrome('992299', 6, 3), '092282')

    def test_case_2(self):
        self.assertEqual(my_code.highestValuePalindrome('0011', 4, 1), '-1')


if __name__ == '__main__':
    unittest.main()
