import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.kangaroo(0, 3, 4, 2), 'YES')

    def test_case_1(self):
        self.assertEqual(solution.kangaroo(0, 2, 5, 3), 'NO')


if __name__ == '__main__':
    unittest.main()
