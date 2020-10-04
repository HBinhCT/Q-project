import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.arraySplitting([3, 3, 3]), 0)
        self.assertEqual(solution.arraySplitting([2, 2, 2, 2]), 2)
        self.assertEqual(solution.arraySplitting([4, 1, 0, 1, 1, 0, 1]), 3)

    def test_case_1(self):
        self.assertEqual(solution.arraySplitting([2, 2, 2, 3, 3]), 2)
        self.assertEqual(solution.arraySplitting([2, 3, 2, 3]), 1)
        self.assertEqual(solution.arraySplitting([3, 2, 3, 2, 2, 2, 2]), 3)


if __name__ == '__main__':
    unittest.main()
