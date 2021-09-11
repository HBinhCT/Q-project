import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.twoSubsequences([1, 1, 1, 4], 5, 3), 3)


if __name__ == '__main__':
    unittest.main()
