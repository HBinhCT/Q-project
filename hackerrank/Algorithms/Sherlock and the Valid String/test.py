import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.isValid('aabbcd'), 'NO')

    def test_case_1(self):
        self.assertEqual(my_code.isValid('aabbccddeefghi'), 'NO')

    def test_case_2(self):
        self.assertEqual(my_code.isValid('abcdefghhgfedecba'), 'YES')


if __name__ == '__main__':
    unittest.main()
