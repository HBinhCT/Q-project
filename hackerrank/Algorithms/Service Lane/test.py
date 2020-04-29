import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.serviceLane([2, 3, 1, 2, 3, 2, 3, 3], [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]),
                         [1, 2, 3, 2, 1])

    def test_case_1(self):
        self.assertEqual(solution.serviceLane([1, 2, 2, 2, 1], [[2, 3], [1, 4], [2, 4], [2, 4], [2, 3]]),
                         [2, 1, 1, 1, 2])


if __name__ == '__main__':
    unittest.main()
