import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]), 1)

    def test_case_1(self):
        self.assertEqual(solution.formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]]), 4)


if __name__ == '__main__':
    unittest.main()
