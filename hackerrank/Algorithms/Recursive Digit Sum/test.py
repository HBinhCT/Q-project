import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.superDigit(148, 3), 3)

    def test_case_1(self):
        self.assertEqual(solution.superDigit(9875, 4), 8)

    def test_case_2(self):
        self.assertEqual(solution.superDigit(123, 3), 9)


if __name__ == '__main__':
    unittest.main()
