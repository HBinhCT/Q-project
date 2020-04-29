import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.countingValleys(8, 'UDDDUDUU'), 1)

    def test_case_1(self):
        self.assertEqual(solution.countingValleys(12, 'DDUUDDUDUUUD'), 2)


if __name__ == '__main__':
    unittest.main()
