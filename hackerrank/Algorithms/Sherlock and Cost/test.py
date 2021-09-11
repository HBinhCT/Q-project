import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.cost([100, 2, 100, 2, 100]), 396)

    def test_case_1(self):
        self.assertEqual(solution.cost([3, 15, 4, 12, 10]), 50)
        self.assertEqual(solution.cost([4, 7, 9]), 12)


if __name__ == '__main__':
    unittest.main()
