import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.maxSubarray([1, 2, 3, 4]), [10, 10])
        self.assertEqual(solution.maxSubarray([2, -1, 2, 3, 4, -5]), [10, 11])

    def test_case_1(self):
        self.assertEqual(solution.maxSubarray([-2, -3, -1, -4, -6]), [-1, -1])


if __name__ == '__main__':
    unittest.main()
