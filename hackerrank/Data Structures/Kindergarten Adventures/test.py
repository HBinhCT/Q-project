import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.solve([1, 0, 0]), 2)

    def test_case_1(self):
        self.assertEqual(solution.solve([0, 1, 2]), 1)


if __name__ == '__main__':
    unittest.main()
