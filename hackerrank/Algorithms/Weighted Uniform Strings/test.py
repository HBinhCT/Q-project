import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(
            solution.weightedUniformStrings('abccddde', [1, 3, 12, 5, 9, 10]),
            ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'No']
        )

    def test_case_1(self):
        self.assertEqual(
            solution.weightedUniformStrings('aaabbbbcccddd', [9, 7, 8, 12, 5]),
            ['Yes', 'No', 'Yes', 'Yes', 'No']
        )


if __name__ == '__main__':
    unittest.main()
