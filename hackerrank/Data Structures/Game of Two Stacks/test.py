import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.twoStacks(10, [4, 2, 4, 6, 1], [2, 1, 8, 5]), 4)


if __name__ == '__main__':
    unittest.main()
