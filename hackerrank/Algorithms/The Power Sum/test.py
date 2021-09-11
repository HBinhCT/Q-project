import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.powerSum(10, 2), 1)

    def test_case_1(self):
        self.assertEqual(solution.powerSum(100, 2), 3)

    def test_case_2(self):
        self.assertEqual(solution.powerSum(100, 3), 1)


if __name__ == '__main__':
    unittest.main()
