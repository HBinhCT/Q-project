import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.minimumNumber(3, 'Ab1'), 3)

    def test_case_1(self):
        self.assertEqual(solution.minimumNumber(11, '#HackerRank'), 1)


if __name__ == '__main__':
    unittest.main()
