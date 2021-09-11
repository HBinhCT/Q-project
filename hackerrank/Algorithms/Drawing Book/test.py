import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.pageCount(6, 2), 1)

    def test_case_1(self):
        self.assertEqual(solution.pageCount(5, 4), 0)


if __name__ == '__main__':
    unittest.main()
