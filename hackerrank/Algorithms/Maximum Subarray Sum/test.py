import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.maximumSum([3, 3, 9, 9, 5], 7), 6)

    def test_case_1(self):
        self.assertEqual(solution.maximumSum([1, 2, 3], 2), 1)

    def test_case_2(self):
        self.assertEqual(solution.maximumSum([1, 5, 9], 5), 4)


if __name__ == '__main__':
    unittest.main()
