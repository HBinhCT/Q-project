import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.bricksGame([999, 1, 1, 1, 0]), 1001)
        self.assertEqual(solution.bricksGame([0, 1, 1, 1, 999]), 999)

    def test_case_1(self):
        self.assertEqual(solution.bricksGame([123, 4, 56, 19, 20]), 183)
        self.assertEqual(solution.bricksGame([15, 17, 25, 128, 95]), 110)
        self.assertEqual(solution.bricksGame([15, 17, 19, 10, 100]), 115)


if __name__ == '__main__':
    unittest.main()
