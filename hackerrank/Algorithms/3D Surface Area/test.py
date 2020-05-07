import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.surfaceArea([[1]]), 6)

    def test_case_1(self):
        self.assertEqual(solution.surfaceArea([[1, 3, 4], [2, 2, 3], [1, 2, 4]]), 60)


if __name__ == '__main__':
    unittest.main()
