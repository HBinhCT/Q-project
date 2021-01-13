import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.flippingMatrix([
            [112, 42, 83, 119],
            [56, 125, 56, 49],
            [15, 78, 101, 43],
            [62, 98, 114, 108],
        ]), 414)

    def test_case_1(self):
        self.assertEqual(solution.flippingMatrix([
            [107, 54, 128, 15],
            [12, 75, 110, 138],
            [100, 96, 34, 85],
            [75, 15, 28, 112],
        ]), 488)


if __name__ == '__main__':
    unittest.main()
