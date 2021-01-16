import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertIn(solution.bonetrousle(12, 8, 3), [[2, 3, 7], [3, 4, 5]])
        self.assertEqual(solution.bonetrousle(10, 3, 3), [-1])
        self.assertIn(solution.bonetrousle(9, 10, 2), [[5, 4], [4, 5]])
        self.assertIn(solution.bonetrousle(9, 10, 2), [[1, 8], [4, 5]])

    def test_case_1(self):
        self.assertIn(solution.bonetrousle(15, 25, 3), [[12, 1, 2], [4, 5, 6]])
        self.assertIn(solution.bonetrousle(12, 6, 3), [[5, 1, 6], [3, 4, 5]])
        self.assertIn(solution.bonetrousle(51, 18, 6), [[10, 1, 2, 3, 17, 18], [6, 7, 8, 9, 10, 11]])


if __name__ == '__main__':
    unittest.main()
