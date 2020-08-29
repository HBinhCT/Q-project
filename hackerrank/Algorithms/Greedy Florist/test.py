import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.getMinimumCost(3, [2, 5, 6]), 13)

    def test_case_1(self):
        self.assertEqual(solution.getMinimumCost(2, [2, 5, 6]), 15)

    def test_case_2(self):
        self.assertEqual(solution.getMinimumCost(3, [1, 3, 5, 7, 9]), 29)


if __name__ == '__main__':
    unittest.main()
