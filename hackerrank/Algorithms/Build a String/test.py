import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.buildString(4, 5, 'aabaacaba'), 26)
        self.assertEqual(solution.buildString(8, 9, 'bacbacacb'), 42)

    def test_case_1(self):
        self.assertEqual(solution.buildString(1, 2, 'cbaasgcbiikaegcbiidcbaasgcbiikaegcbiidir'), 20)
        self.assertEqual(solution.buildString(1, 3, 'cabcjpsdaedsasedsascabcjpsddsdaedsasedsa'), 24)
        self.assertEqual(solution.buildString(2, 3, 'cbacojcrojcrlidickjcjcrojcrlijcrojcrrojq'), 45)


if __name__ == '__main__':
    unittest.main()
