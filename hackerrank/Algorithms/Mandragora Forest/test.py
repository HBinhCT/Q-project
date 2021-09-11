import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.mandragora([3, 2, 2]), 10)

    def test_case_1(self):
        self.assertEqual(solution.mandragora([15]), 15)

    def test_case_2(self):
        self.assertEqual(solution.mandragora([5, 2, 6, 11, 29, 12, 7]), 260)


if __name__ == '__main__':
    unittest.main()
