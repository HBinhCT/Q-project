import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.minimumAbsoluteDifference([3, -7, 0]), 3)

    def test_case_1(self):
        self.assertEqual(solution.minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]), 1)

    def test_case_2(self):
        self.assertEqual(solution.minimumAbsoluteDifference([1, -3, 71, 68, 17]), 3)


if __name__ == '__main__':
    unittest.main()
