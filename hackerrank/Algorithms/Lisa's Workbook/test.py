import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.workbook(5, 3, [4, 2, 6, 1, 10]), 4)

    def test_case_1(self):
        self.assertEqual(solution.workbook(10, 5, [3, 8, 15, 11, 14, 1, 9, 2, 24, 31]), 8)


if __name__ == '__main__':
    unittest.main()
