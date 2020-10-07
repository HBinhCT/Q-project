import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.gridWalking(3, [1, 1], [2, 3]), 12)

    def test_case_1(self):
        self.assertEqual(solution.gridWalking(3, [1, 3], [3, 5]), 32)
        self.assertEqual(solution.gridWalking(2, [3, 3], [3, 5]), 10)


if __name__ == '__main__':
    unittest.main()
