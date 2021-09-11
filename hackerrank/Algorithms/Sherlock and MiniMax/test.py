import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.sherlockAndMinimax([5, 8, 14], 4, 9), 4)

    def test_case_1(self):
        self.assertEqual(solution.sherlockAndMinimax([3, 24, 35, 6, 7, 45], 15, 20), 15)


if __name__ == '__main__':
    unittest.main()
