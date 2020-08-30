import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.maxMin(3, [10, 100, 300, 200, 1000, 20, 30]), 20)

    def test_case_1(self):
        self.assertEqual(solution.maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]), 3)

    def test_case_2(self):
        self.assertEqual(solution.maxMin(2, [1, 2, 1, 2, 1]), 0)


if __name__ == '__main__':
    unittest.main()
