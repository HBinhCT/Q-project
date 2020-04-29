import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.gameOfThrones('aaabbbb'), 'YES')

    def test_case_1(self):
        self.assertEqual(solution.gameOfThrones('cdefghmnopqrstuvw'), 'NO')

    def test_case_2(self):
        self.assertEqual(solution.gameOfThrones('cdcdcdcdeeeef'), 'YES')


if __name__ == '__main__':
    unittest.main()
