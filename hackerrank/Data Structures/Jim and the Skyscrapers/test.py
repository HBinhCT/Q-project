import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.solve([3, 2, 1, 2, 3, 3]), 8)

    def test_case_1(self):
        self.assertEqual(solution.solve([1, 1000, 1]), 0)


if __name__ == '__main__':
    unittest.main()
