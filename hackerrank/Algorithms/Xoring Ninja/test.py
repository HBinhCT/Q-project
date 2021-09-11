import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.xoringNinja([1, 2, 3]), 12)

    def test_case_1(self):
        self.assertEqual(solution.xoringNinja([1, 2, 4, 8]), 120)
        self.assertEqual(solution.xoringNinja([1, 2, 3, 5, 100]), 1648)


if __name__ == '__main__':
    unittest.main()
