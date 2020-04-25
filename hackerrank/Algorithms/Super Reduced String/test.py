import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.superReducedString('aaabccddd'), 'abd')

    def test_case_1(self):
        self.assertEqual(my_code.superReducedString('aa'), 'Empty String')

    def test_case_2(self):
        self.assertEqual(my_code.superReducedString('baab'), 'Empty String')


if __name__ == '__main__':
    unittest.main()
