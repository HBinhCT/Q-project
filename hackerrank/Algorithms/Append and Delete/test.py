import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.appendAndDelete('hackerhappy', 'hackerrank', 9), 'Yes')

    def test_case_1(self):
        self.assertEqual(solution.appendAndDelete('aba', 'aba', 7), 'Yes')

    def test_case_2(self):
        self.assertEqual(solution.appendAndDelete('ashley', 'ash', 2), 'No')


if __name__ == '__main__':
    unittest.main()
