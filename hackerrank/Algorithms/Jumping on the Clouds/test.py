import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]), 4)

    def test_case_1(self):
        self.assertEqual(solution.jumpingOnClouds([0, 0, 0, 1, 0, 0]), 3)


if __name__ == '__main__':
    unittest.main()
