import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.towerBreakers(2, 2), 2)
        self.assertEqual(solution.towerBreakers(1, 4), 1)

    def test_case_1(self):
        self.assertEqual(solution.towerBreakers(1, 7), 1)
        self.assertEqual(solution.towerBreakers(3, 7), 1)


if __name__ == '__main__':
    unittest.main()
