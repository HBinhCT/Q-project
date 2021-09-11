import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.coinOnTheTable(2, 3, ['RD', '*L']), 0)

    def test_case_1(self):
        self.assertEqual(solution.coinOnTheTable(2, 1, ['RD', '*L']), 1)


if __name__ == '__main__':
    unittest.main()
