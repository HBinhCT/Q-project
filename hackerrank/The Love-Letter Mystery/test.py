import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.theLoveLetterMystery('abc'), 2)
        self.assertEqual(my_code.theLoveLetterMystery('abcba'), 0)
        self.assertEqual(my_code.theLoveLetterMystery('abcd'), 4)
        self.assertEqual(my_code.theLoveLetterMystery('cba'), 2)

    def test_case_1(self):
        self.assertEqual(my_code.theLoveLetterMystery('lmnop'), 6)
        self.assertEqual(my_code.theLoveLetterMystery('adslkfjas'), 36)
        self.assertEqual(my_code.theLoveLetterMystery('bafhaef'), 13)
        self.assertEqual(my_code.theLoveLetterMystery('ofrhase'), 40)


if __name__ == '__main__':
    unittest.main()
