import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.superReducedString('aaabccddd'), 'abd')

    def test_case_1(self):
        self.assertEqual(solution.superReducedString('aa'), 'Empty String')

    def test_case_2(self):
        self.assertEqual(solution.superReducedString('baab'), 'Empty String')


if __name__ == '__main__':
    unittest.main()
