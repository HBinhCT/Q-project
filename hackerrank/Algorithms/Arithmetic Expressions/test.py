import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertIn(solution.arithmeticExpressions([22, 79, 21]), ['22+79*21', '22*79-21'])

    def test_case_1(self):
        self.assertEqual(solution.arithmeticExpressions([55, 3, 45, 33, 25]), '55+3-45*33-25')


if __name__ == '__main__':
    unittest.main()
