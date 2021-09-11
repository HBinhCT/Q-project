import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.towerBreakers([1, 2]), 1)
        self.assertEqual(solution.towerBreakers([1, 2, 3]), 2)


if __name__ == '__main__':
    unittest.main()
