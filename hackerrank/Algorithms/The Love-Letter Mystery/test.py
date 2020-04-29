import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.theLoveLetterMystery('abc'), 2)
        self.assertEqual(solution.theLoveLetterMystery('abcba'), 0)
        self.assertEqual(solution.theLoveLetterMystery('abcd'), 4)
        self.assertEqual(solution.theLoveLetterMystery('cba'), 2)

    def test_case_1(self):
        self.assertEqual(solution.theLoveLetterMystery('lmnop'), 6)
        self.assertEqual(solution.theLoveLetterMystery('adslkfjas'), 36)
        self.assertEqual(solution.theLoveLetterMystery('bafhaef'), 13)
        self.assertEqual(solution.theLoveLetterMystery('ofrhase'), 40)


if __name__ == '__main__':
    unittest.main()
