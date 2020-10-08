import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.unboundedKnapsack(12, [1, 6, 9]), 12)
        self.assertEqual(solution.unboundedKnapsack(9, [3, 4, 4, 4, 8]), 9)

    def test_case_1(self):
        self.assertEqual(solution.unboundedKnapsack(13, [3, 7, 9, 11]), 13)
        self.assertEqual(solution.unboundedKnapsack(11, [3, 7, 9]), 10)


if __name__ == '__main__':
    unittest.main()
