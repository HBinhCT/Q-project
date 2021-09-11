import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.maximumToys([1, 12, 5, 111, 200, 1000, 10], 50), 4)

    def test_case_1(self):
        self.assertEqual(solution.maximumToys([1, 2, 3, 4], 7), 3)

    def test_case_2(self):
        self.assertEqual(solution.maximumToys([3, 7, 2, 9, 4], 15), 3)


if __name__ == '__main__':
    unittest.main()
