import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.timeInWords(5, 47), "thirteen minutes to six")

    def test_case_1(self):
        self.assertEqual(my_code.timeInWords(3, 00), "three o' clock")

    def test_case_2(self):
        self.assertEqual(my_code.timeInWords(7, 15), "quarter past seven")


if __name__ == '__main__':
    unittest.main()
