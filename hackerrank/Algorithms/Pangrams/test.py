import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.pangrams('We promptly judged antique ivory buckles for the next prize'), 'pangram')

    def test_case_1(self):
        self.assertEqual(solution.pangrams('We promptly judged antique ivory buckles for the prize'), 'not pangram')


if __name__ == '__main__':
    unittest.main()
