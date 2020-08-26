import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.toys([1, 2, 3, 21, 7, 12, 14, 21]), 4)

    def test_case_1(self):
        self.assertEqual(solution.toys([12, 15, 7, 8, 19, 24]), 4)


if __name__ == '__main__':
    unittest.main()
