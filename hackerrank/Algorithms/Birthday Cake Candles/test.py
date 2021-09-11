import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.birthdayCakeCandles([3, 2, 1, 3]), 2)


if __name__ == '__main__':
    unittest.main()
