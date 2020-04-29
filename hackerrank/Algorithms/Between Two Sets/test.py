import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.getTotalX([2, 4], [16, 32, 96]), 3)

    def test_case_1(self):
        self.assertEqual(solution.getTotalX([3, 4], [24, 48]), 2)


if __name__ == '__main__':
    unittest.main()
