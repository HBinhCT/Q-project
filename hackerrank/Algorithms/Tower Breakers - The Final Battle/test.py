import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.towerBreakers(4), 6)
        self.assertEqual(solution.towerBreakers(2), 4)
        self.assertEqual(solution.towerBreakers(7), 8)


if __name__ == '__main__':
    unittest.main()
