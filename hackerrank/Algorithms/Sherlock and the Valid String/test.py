import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.isValid('aabbcd'), 'NO')

    def test_case_1(self):
        self.assertEqual(solution.isValid('aabbccddeefghi'), 'NO')

    def test_case_2(self):
        self.assertEqual(solution.isValid('abcdefghhgfedecba'), 'YES')


if __name__ == '__main__':
    unittest.main()
